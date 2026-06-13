#!/usr/bin/env python3
"""Genera index.html — Mallorca · 6 días · Playas, paisajes y pueblos · Google Maps."""
import urllib.parse
from pathlib import Path

BASE = Path(__file__).parent
from images_data import DAYS, MAINS, DAY_TAB_LABELS  # noqa: E402

HERO = "https://images.unsplash.com/photo-1651918858137-d3d484d35854?w=1920&q=80"


def site(key):
    m = MAINS[key]
    return m["url"], m["url"].replace("w=800", "w=1600"), m["cap"]


def gmaps_embed(stops):
    enc = [urllib.parse.quote_plus(s) for s in stops]
    if len(enc) == 1:
        return f"https://maps.google.com/maps?q={enc[0]}&z=11&output=embed"
    if len(enc) == 2:
        return f"https://maps.google.com/maps?saddr={enc[0]}&daddr={enc[1]}&dirflg=d&output=embed"
    mid = "+to:".join(enc[1:-1])
    return f"https://maps.google.com/maps?saddr={enc[0]}&daddr={mid}+to:{enc[-1]}&dirflg=d&output=embed"


def gallery(*keys):
    items = []
    for k in keys:
        url, full, cap = site(k)
        items.append(
            f'<button type="button" class="gallery-item" data-full="{full}" data-cap="{cap}" '
            f'aria-label="Ampliar: {cap}"><img src="{url}" alt="{cap}" loading="lazy" decoding="async"></button>'
        )
    return "".join(items)


def spot(key, title, desc):
    url, full, cap = site(key)
    return f"""<li class="spot-item">
                  <button type="button" class="spot-img spot-zoom" data-full="{full}" data-cap="{cap}" aria-label="Ampliar {title}">
                    <img src="{url}" alt="{cap}" loading="lazy" decoding="async">
                  </button>
                  <div class="spot-body"><strong>{title}</strong><span class="spot-desc">{desc}</span></div>
                </li>"""


def tranquility_dots(n):
    return "".join(f'<span class="dot{" active" if i < n else ""}"></span>' for i in range(5))


def day_block(num, zone, title, drive_km, drive_time, tranq, route_text, teaser, gallery_html,
              activities, schedule, spots_html, gmaps_url, gmaps_stops, map_id):
    embed = gmaps_embed(gmaps_stops)
    t = int(tranq.split("/")[0]) if "/" in str(tranq) else 4
    return f"""
      <article class="day-card" id="dia-{num}">
        <div class="day-header">
          <div>
            <p class="day-num">Día {num} · {zone}</p>
            <h3 class="day-title">{title}</h3>
          </div>
          <div class="day-meta">
            <span>📏 ~{drive_km} km</span>
            <span>🚗 ~{drive_time}</span>
          </div>
        </div>
        <div class="day-body">
          <div class="route-bar">{route_text}</div>
          <div class="day-stats">
            <div class="stat"><span class="stat-value">{drive_km}</span><span class="stat-label">Kilómetros</span></div>
            <div class="stat"><span class="stat-value">{drive_time}</span><span class="stat-label">En coche</span></div>
            <div class="stat"><span class="stat-value tranquility">{tranquility_dots(t)}</span><span class="stat-label">Tranquilidad {tranq}</span></div>
            <div class="stat"><span class="stat-value">9:00</span><span class="stat-label">Mejor hora inicio</span></div>
          </div>
          <p class="day-teaser">{teaser}</p>
          <p class="gallery-hint">Toca cualquier foto para ampliar · Desliza entre imágenes en el zoom</p>
          <div class="day-gallery">{gallery_html}</div>
          <div class="day-details">
            <div class="day-detail"><h4>Qué hacer</h4><ul>{activities}</ul></div>
            <div class="day-detail"><h4>Horario sugerido</h4><ul>{schedule}</ul></div>
            <div class="day-detail day-detail--spots"><h4>Qué encontrarás</h4><ul class="spot-list">{spots_html}</ul></div>
          </div>
          <div class="map-wrap gmap-only">
            <iframe class="gmap-embed" title="Ruta día {num}" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade" src="{embed}"></iframe>
            <p class="map-caption">Ruta interactiva en Google Maps</p>
          </div>
          <a class="btn-map" href="{gmaps_url}" target="_blank" rel="noopener">📍 Abrir ruta en app Google Maps</a>
        </div>
      </article>"""


def build_overview():
    tabs, panels = [], []
    for day in DAYS:
        n = day["num"]
        active = " is-active" if n == 1 else ""
        tabs.append(f'<button type="button" class="route-day-tab{active}" data-day="{n}" role="tab">{DAY_TAB_LABELS[n]}</button>')
        embed = gmaps_embed(day["gmaps"])
        panels.append(
            f'<div class="route-day-panel{active}" data-day="{n}" role="tabpanel">'
            f'<iframe class="gmap-embed" title="Ruta día {n}" loading="lazy" allowfullscreen '
            f'referrerpolicy="no-referrer-when-downgrade" src="{embed}"></iframe></div>'
        )
    return f'<div class="full-routes-overview"><div class="route-day-tabs" role="tablist">{"".join(tabs)}</div>{"".join(panels)}</div>'


def main():
    from itinerary import build_days
    days_html = build_days(day_block, gallery, spot)
    overview = build_overview()
    region_map = gmaps_embed(["Palma de Mallorca, Spain", "Cap de Formentor, Mallorca", "Es Trenc, Mallorca"])

    card_keys = ["palma", "valldemossa", "pollenca", "alcudia", "santanyi", "es_trenc"]
    card_data = [
        ("Palma · D1", "Can Cera Boutique Hotel", "Hotel con encanto · Casco antiguo", "En el centro histórico, a pasos de La Seu. Ideal para madrugar y coger el tren a Sóller sin aparcar.", "Can Cera Boutique Hotel Palma"),
        ("Valldemossa · D2", "Hotel Valldemossa", "Hotel · Tramuntana", "Base en el valle para Deià y Banyalbufar. Silencio de montaña y olor a naranja por la mañana.", "Hotel Valldemossa Mallorca"),
        ("Pollença · D3", "Hotel Juma", "Hotel · Plaza mayor", "Frente a la plaza de Pollença. Perfecto para subir a Formentor al amanecer.", "Hotel Juma Pollença"),
        ("Alcúdia · D4", "Can Tem", "Agroturismo · Noreste", "Finca restaurada cerca de Alcúdia. Tranquilo tras un día de playa en Muro y calas del noreste.", "Can Tem Alcudia Mallorca"),
        ("Santanyí · D5", "Hotel Cala Sant Vicenç", "Hotel · Cala boutique", "Base sureste para Mondragó, Santanyí y Cala d'Or. Ambiente más íntimo que los resorts.", "Hotel Cala Sant Vicenç Mallorca"),
        ("Campos · D6", "Fontsanta Hotel", "Spa · Sur de la isla", "Cerca de Es Trenc y Ses Salines. Cierra el viaje con un baño al amanecer en la playa virgen.", "Fontsanta Hotel Mallorca"),
    ]
    cards = ""
    for key, (zone, name, style, desc, search) in zip(card_keys, card_data):
        url = MAINS[key]["url"]
        cards += f"""<article class="card">
          <div class="card-img" style="background-image:url('{url}')"></div>
          <div class="card-body">
            <p class="card-zone">{zone}</p>
            <h3>{name}</h3>
            <span class="card-style">{style}</span>
            <p>{desc}</p>
            <p><a href="https://www.google.com/maps/search/{urllib.parse.quote_plus(search)}" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
          </div>
        </article>"""

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <meta name="theme-color" content="#1a6b8a">
  <title>Mallorca · Guía 6 Días · Playas & pueblos</title>
  <style>
    :root {{
      --sea: #1a6b8a; --sea-light: #2d8aad; --sea-pale: #e8f2f6;
      --green: #3d5a45; --green-light: #5a7a62; --green-pale: #e8f0ea;
      --coral: #d4845a; --sand: #f5f0e8; --sand-dark: #ddd4c8;
      --text: #2c3338; --text-muted: #6b7280; --white: #fff;
      --shadow: 0 4px 24px rgba(26,107,138,.1); --radius: 16px; --radius-sm: 10px; --header-h: 3.25rem;
    }}
    *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
    html{{scroll-behavior:smooth;-webkit-text-size-adjust:100%}}
    body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:var(--sand);color:var(--text);line-height:1.65;overflow-x:hidden}}
    section{{scroll-margin-top:calc(var(--header-h)+.5rem);padding:5rem 0}}
    section:nth-child(even){{background:var(--white)}}
    .container{{max-width:1100px;margin:0 auto;padding:0 1.5rem}}
    .site-header{{position:fixed;top:0;left:0;right:0;z-index:200;height:var(--header-h);display:flex;align-items:center;justify-content:space-between;padding:0 1.25rem;background:rgba(255,255,255,.92);backdrop-filter:blur(14px);border-bottom:1px solid var(--sand-dark)}}
    .site-logo{{font-family:Georgia,serif;font-size:1.05rem;font-weight:600;color:var(--sea);text-decoration:none}}
    .nav-toggle{{display:none;width:2.5rem;height:2.5rem;border:1px solid var(--sand-dark);border-radius:var(--radius-sm);background:var(--white);color:var(--sea);font-size:1.25rem;cursor:pointer}}
    .site-nav ul{{list-style:none;display:flex;flex-wrap:wrap;gap:.15rem .85rem}}
    .site-nav a{{text-decoration:none;color:var(--text-muted);font-size:.78rem;font-weight:500}}
    .site-nav a:hover{{color:var(--sea)}}
    .hero{{position:relative;min-height:88vh;display:flex;align-items:flex-end;overflow:hidden}}
    .hero-bg{{position:absolute;inset:0;background:url('{HERO}') center/cover no-repeat}}
    .hero-bg::after{{content:'';position:absolute;inset:0;background:linear-gradient(to top,rgba(15,45,58,.88),rgba(26,107,138,.35))}}
    .hero-content{{position:relative;z-index:2;padding:4rem 2rem 5rem;max-width:900px;margin:0 auto;width:100%}}
    .hero-tag{{display:inline-block;font-size:.75rem;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:var(--sand);background:rgba(255,255,255,.15);padding:.45rem 1rem;border-radius:100px;margin-bottom:1.25rem}}
    .hero h1{{font-family:Georgia,serif;font-size:clamp(2.6rem,7vw,4.6rem);color:var(--white);line-height:1.05;margin-bottom:1rem}}
    .hero h1 em{{font-style:italic;font-weight:400;color:var(--coral)}}
    .hero-sub{{font-size:1.12rem;color:rgba(255,255,255,.9);max-width:560px;margin-bottom:1.5rem}}
    .hero-meta{{display:flex;flex-wrap:wrap;gap:1.25rem;color:rgba(255,255,255,.78);font-size:.9rem}}
    .section-label{{font-size:.72rem;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:var(--sea);margin-bottom:.75rem}}
    .section-title{{font-family:Georgia,serif;font-size:clamp(2rem,4vw,2.75rem);margin-bottom:.75rem;line-height:1.15}}
    .section-intro{{color:var(--text-muted);max-width:680px;margin-bottom:2rem;font-size:1.05rem}}
    .intro-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr));gap:1.5rem}}
    .intro-card{{background:var(--white);border-radius:var(--radius-sm);padding:1.75rem;box-shadow:var(--shadow)}}
    .intro-card h3{{font-family:Georgia,serif;margin-bottom:.5rem}}
    .intro-card p,.intro-card ol{{color:var(--text-muted);font-size:.92rem}}
    .intro-card ol{{padding-left:1.25rem;margin-top:.5rem}}
    .day-cards{{display:grid;grid-template-columns:1fr;gap:2rem;width:100%}}
    .day-card{{background:var(--white);border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow);border:1px solid var(--sand-dark)}}
    section#itinerario{{background:var(--sand)}}
    .day-header{{display:flex;flex-wrap:wrap;justify-content:space-between;gap:1rem;padding:1.5rem 1.75rem;background:linear-gradient(135deg,var(--sea),var(--sea-light));color:var(--white)}}
    .day-num{{font-size:.72rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;opacity:.85}}
    .day-title{{font-family:Georgia,serif;font-size:1.45rem;margin-top:.25rem}}
    .day-meta{{display:flex;flex-wrap:wrap;gap:.75rem;font-size:.82rem;opacity:.9}}
    .day-body{{padding:1.75rem}}
    .route-bar{{background:var(--sea-pale);border-radius:var(--radius-sm);padding:.85rem 1rem;font-size:.88rem;margin-bottom:1.25rem;line-height:1.5;color:var(--sea)}}
    .route-bar .arrow{{color:var(--coral);margin:0 .25rem;font-weight:700}}
    .day-stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,120px),1fr));gap:1rem;margin-bottom:1.25rem}}
    .stat{{text-align:center;padding:.85rem;background:var(--sand);border-radius:var(--radius-sm)}}
    .stat-value{{display:block;font-size:1.25rem;font-weight:700;color:var(--sea)}}
    .stat-label{{font-size:.72rem;color:var(--text-muted);text-transform:uppercase;letter-spacing:.06em}}
    .tranquility{{display:flex;align-items:center;justify-content:center;gap:.2rem}}
    .tranquility .dot{{width:10px;height:10px;border-radius:50%;background:var(--sand-dark)}}
    .tranquility .dot.active{{background:var(--green-light)}}
    .day-teaser{{font-family:Georgia,serif;font-style:italic;color:var(--green);margin-bottom:.75rem;font-size:1.02rem;line-height:1.6}}
    .gallery-hint{{font-size:.78rem;color:var(--text-muted);margin-bottom:.65rem}}
    .day-gallery{{display:flex;gap:.65rem;overflow-x:auto;padding-bottom:.35rem;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;margin-bottom:1.25rem}}
    .gallery-item{{border:none;padding:0;background:none;cursor:zoom-in;flex-shrink:0;scroll-snap-align:start;border-radius:var(--radius-sm);overflow:hidden;box-shadow:var(--shadow);position:relative}}
    .gallery-item::after{{content:'🔍';position:absolute;right:.35rem;bottom:.3rem;font-size:.7rem;background:rgba(0,0,0,.45);color:#fff;padding:.12rem .3rem;border-radius:5px}}
    .gallery-item img{{height:130px;width:auto;min-width:200px;max-width:280px;object-fit:cover;display:block}}
    .day-details{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:1.25rem;margin-bottom:1.25rem;width:100%}}
    .day-detail h4{{font-size:.78rem;text-transform:uppercase;letter-spacing:.1em;color:var(--text-muted);margin-bottom:.5rem}}
    .day-detail ul{{list-style:none;font-size:.9rem;color:var(--text)}}
    .day-detail li{{padding:.25rem 0;padding-left:1rem;position:relative}}
    .day-detail li::before{{content:'·';position:absolute;left:0;color:var(--coral);font-weight:700}}
    .day-detail--spots{{grid-column:1/-1}}
    .spot-list{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,280px),1fr));gap:1.25rem;width:100%}}
    .spot-item{{display:flex;flex-direction:column;border-radius:var(--radius-sm);overflow:hidden;background:var(--white);border:1px solid var(--sand-dark);box-shadow:var(--shadow)}}
    .spot-img{{width:100%;height:148px;border:none;cursor:zoom-in;padding:0;overflow:hidden;background-size:cover;background-position:center}}
    .spot-img img{{width:100%;height:100%;object-fit:cover;display:block}}
    .spot-body{{padding:1rem 1.15rem 1.15rem}}
    .spot-body strong{{display:block;font-family:Georgia,serif;margin-bottom:.35rem}}
    .spot-desc{{font-size:.88rem;color:var(--text-muted);line-height:1.55}}
    .map-wrap{{border-radius:var(--radius-sm);overflow:hidden;box-shadow:var(--shadow);border:1px solid var(--sand-dark);margin-top:1rem}}
    .gmap-embed{{width:100%;height:380px;border:0;display:block}}
    .map-caption{{font-size:.78rem;color:var(--text-muted);padding:.65rem 1rem;background:var(--white);border-top:1px solid var(--sand-dark);margin:0}}
    .full-routes-overview{{border-radius:var(--radius-sm);overflow:hidden;border:1px solid var(--sand-dark);box-shadow:var(--shadow)}}
    .route-day-tabs{{display:flex;flex-wrap:wrap;background:var(--white);border-bottom:1px solid var(--sand-dark)}}
    .route-day-tab{{flex:1;min-width:4.5rem;padding:.6rem .35rem;border:none;background:transparent;font-size:.72rem;font-weight:600;color:var(--text-muted);cursor:pointer}}
    .route-day-tab.is-active{{color:var(--sea);box-shadow:inset 0 -2px 0 var(--sea);background:var(--sea-pale)}}
    .route-day-panel{{display:none}}.route-day-panel.is-active{{display:block}}
    .route-day-panel .gmap-embed{{height:420px}}
    .btn-map{{display:inline-flex;align-items:center;gap:.4rem;margin-top:1rem;padding:.65rem 1.15rem;background:var(--sea);color:var(--white);text-decoration:none;border-radius:100px;font-size:.85rem;font-weight:600}}
    .card-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:1.5rem}}
    .card{{background:var(--white);border-radius:var(--radius-sm);overflow:hidden;box-shadow:var(--shadow);border:1px solid var(--sand-dark)}}
    .card-img{{height:180px;background-size:cover;background-position:center}}
    .card-body{{padding:1.5rem}}
    .card-zone{{font-size:.72rem;text-transform:uppercase;letter-spacing:.1em;color:var(--green-light);margin-bottom:.35rem}}
    .card-body h3{{font-family:Georgia,serif;margin-bottom:.35rem}}
    .card-style{{display:inline-block;font-size:.75rem;background:var(--sea-pale);color:var(--sea);padding:.2rem .6rem;border-radius:100px;margin-bottom:.65rem}}
    .card-body p{{font-size:.9rem;color:var(--text-muted);margin-bottom:.5rem}}
    .card-body a{{color:var(--sea);font-size:.85rem;font-weight:600}}
    .gastro-block{{margin-top:2rem;background:var(--white);border-radius:var(--radius);padding:2rem;box-shadow:var(--shadow);border-top:4px solid var(--coral)}}
    .gastro-block h3{{font-family:Georgia,serif;margin-bottom:.75rem}}
    .gastro-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr));gap:1.5rem;margin-top:1rem}}
    .gastro-col h4{{font-size:.72rem;text-transform:uppercase;letter-spacing:.12em;color:var(--coral);margin-bottom:.5rem}}
    .gastro-col li{{padding:.35rem 0;border-bottom:1px solid var(--sand);font-size:.88rem;color:var(--text-muted);list-style:none}}
    .route-legend{{display:flex;flex-wrap:wrap;gap:.65rem 1.25rem;font-size:.82rem;color:var(--text-muted);margin-top:1rem}}
    .legend-dot{{width:12px;height:12px;border-radius:50%;display:inline-block;margin-right:.35rem}}
    .optimized{{background:linear-gradient(135deg,var(--green),var(--sea));color:var(--white);border-radius:var(--radius);padding:3rem 2.5rem;text-align:center;margin-top:2rem}}
    .optimized .section-title{{color:var(--white)}}
    .optimized-flow{{display:flex;flex-wrap:wrap;justify-content:center;gap:.5rem 1rem;margin:1.5rem 0;font-size:.95rem}}
    .optimized-flow .step{{background:rgba(255,255,255,.15);padding:.5rem 1rem;border-radius:100px}}
    .optimized-flow .arrow{{color:var(--coral);font-weight:700}}
    footer{{text-align:center;padding:3rem 1.5rem;background:var(--sea);color:rgba(255,255,255,.85)}}
    footer em{{display:block;font-family:Georgia,serif;font-size:1.2rem;margin-bottom:.5rem;color:var(--white)}}
    .lightbox{{position:fixed;inset:0;z-index:9999;background:rgba(0,0,0,.92);display:none;align-items:center;justify-content:center;padding:1rem}}
    .lightbox.is-open{{display:flex}}
    .lightbox-inner{{max-width:min(96vw,1200px);display:flex;flex-direction:column;align-items:center;position:relative}}
    .lightbox-img{{max-width:100%;max-height:78vh;object-fit:contain;border-radius:8px;touch-action:pinch-zoom}}
    .lightbox-cap{{color:#fff;margin-top:.75rem;font-size:.9rem;text-align:center;max-width:640px}}
    .lightbox-close{{position:absolute;top:-2.5rem;right:0;width:2.5rem;height:2.5rem;border:none;border-radius:50%;background:rgba(255,255,255,.15);color:#fff;font-size:1.4rem;cursor:pointer}}
    @media(max-width:640px){{
      .container{{max-width:100%;padding-left:max(.65rem,env(safe-area-inset-left));padding-right:max(.65rem,env(safe-area-inset-right))}}
      section{{padding:2.75rem 0}}
      .day-header,.day-body{{padding:1.25rem}}
      #itinerario .day-details{{display:flex;flex-direction:column}}
      #itinerario .spot-list{{display:flex;flex-direction:column}}
      .gmap-embed,.route-day-panel .gmap-embed{{height:min(52vw,340px);min-height:260px}}
      .gallery-item img{{height:118px;min-width:42vw;max-width:none;width:42vw}}
      .route-day-tab{{font-size:.68rem;padding:.55rem .2rem;min-width:3.4rem}}
    }}
    @media(max-width:820px){{
      .nav-toggle{{display:flex;align-items:center;justify-content:center}}
      .site-nav{{position:absolute;top:100%;left:0;right:0;background:rgba(255,255,255,.98);border-bottom:1px solid var(--sand-dark);max-height:0;overflow:hidden;opacity:0;transition:max-height .3s,opacity .25s}}
      .site-nav.is-open{{max-height:480px;opacity:1}}
      .site-nav ul{{flex-direction:column;padding:.75rem 1.25rem 1rem}}
      .site-nav a{{display:block;padding:.6rem 0;font-size:.9rem}}
    }}
  </style>
</head>
<body>
  <header class="site-header" id="site-header">
    <a class="site-logo" href="#intro">Mallorca</a>
    <button type="button" class="nav-toggle" id="nav-toggle" aria-label="Menú" aria-expanded="false">☰</button>
    <nav class="site-nav" id="site-nav">
      <ul>
        <li><a href="#intro">Introducción</a></li>
        <li><a href="#ruta-completa">Mapa ruta</a></li>
        <li><a href="#itinerario">Itinerario</a></li>
        <li><a href="#alojamiento">Alojamiento</a></li>
        <li><a href="#gastronomia">Gastronomía</a></li>
        <li><a href="#consejos">Consejos</a></li>
      </ul>
    </nav>
  </header>

  <header class="hero">
    <div class="hero-bg"></div>
    <div class="hero-content">
      <span class="hero-tag">🏝 Guía Premium · Junio 2026</span>
      <h1>Mallorca<br><em>Playas, calas y pueblos</em></h1>
      <p class="hero-sub">Seis días de slow travel por la isla: La Seu al atardecer, la carretera a Formentor, calas turquesas del sureste y Es Trenc al amanecer. Mapas Google, fotos ampliables y rutas pensadas para junio.</p>
      <div class="hero-meta">
        <span>☀️ 26–32 °C en junio</span>
        <span>🚗 ~480 km totales</span>
        <span>🏖 Una isla, mil paisajes</span>
      </div>
    </div>
  </header>

  <section id="intro">
    <div class="container">
      <p class="section-label">Bienvenida</p>
      <h2 class="section-title">Por qué Mallorca en junio</h2>
      <p class="section-intro">Junio es el mes perfecto: mar ya caliente, Tramuntana verde, menos masificación que julio-agosto y luz mediterránea larga hasta las nueve. Esta guía prioriza playas bonitas, paisajes dramáticos y pueblos con alma — sin prisas ni listas interminables.</p>
      <div class="intro-grid">
        <div class="intro-card"><h3>🏖 Playas & calas</h3><p>De Es Trenc virgen a Cala Mondragó protegida. Cada día incluye al menos una cala o playa con honestidad sobre aparcamiento y multitudes.</p></div>
        <div class="intro-card"><h3>🗺️ Google Maps</h3><p>Cada día incluye ruta interactiva con zoom y satélite. Pestañas D1–D6 en el mapa general.</p></div>
        <div class="intro-card"><h3>📸 Fotos reales</h3><p>Imágenes de cada lugar. Toca para ampliar y hacer zoom con los dedos.</p></div>
        <div class="intro-card"><h3>⛰ Serra de Tramuntana</h3><p>Patrimonio UNESCO: pueblos de piedra, bancales al borde del acantilado y carreteras que son parte del espectáculo.</p></div>
      </div>
    </div>
  </section>

  <section id="ruta-completa">
    <div class="container">
      <p class="section-label">Visión global</p>
      <h2 class="section-title">Mapa de la ruta completa</h2>
      <p class="section-intro">Las seis rutas en Google Maps por toda la isla. Elige un día en las pestañas para ver su recorrido interactivo.</p>
      <div class="map-wrap">{overview}<p class="map-caption">Selecciona un día · ~480 km totales · Palma → Es Trenc</p></div>
      <iframe class="gmap-embed" style="margin-top:1.5rem;border-radius:var(--radius-sm);box-shadow:var(--shadow)" title="Región" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade" src="{region_map}"></iframe>
      <div class="route-legend">
        <span><span class="legend-dot" style="background:#1a6b8a"></span>D1 Palma</span>
        <span><span class="legend-dot" style="background:#3d5a45"></span>D2 Tramuntana</span>
        <span><span class="legend-dot" style="background:#5a7a62"></span>D3 Formentor</span>
        <span><span class="legend-dot" style="background:#d4845a"></span>D4 Alcúdia</span>
        <span><span class="legend-dot" style="background:#2d8aad"></span>D5 Calas</span>
        <span><span class="legend-dot" style="background:#8b6914"></span>D6 Es Trenc</span>
      </div>
    </div>
  </section>

  <section id="itinerario">
    <div class="container">
      <p class="section-label">Día a día</p>
      <h2 class="section-title">Itinerario 6 días</h2>
      <p class="section-intro">Palma → Tramuntana → Formentor → Alcúdia → Calas del sureste → Es Trenc. Cada día incluye qué verás, olerás y sentirás — con honestidad sobre aparcamiento, multitudes y mejores horas.</p>
      <div class="day-cards">{days_html}</div>
    </div>
  </section>

  <section id="alojamiento">
    <div class="container">
      <p class="section-label">Dónde dormir</p>
      <h2 class="section-title">Bases sugeridas</h2>
      <p class="section-intro">Hoteles y agroturismos para moverte por la isla sin rehacer maletas cada noche. Reserva con antelación en junio — especialmente Pollença y fin de semana en Palma.</p>
      <div class="card-grid">{cards}</div>
    </div>
  </section>

  <section id="gastronomia">
    <div class="container">
      <p class="section-label">Qué comer</p>
      <h2 class="section-title">Gastronomía mallorquina</h2>
      <div class="gastro-block">
        <h3>Sabores de la isla en seis días</h3>
        <p>Mallorca tiene cocina propia más allá del sol y la playa: sobrasada, ensaimada, tumbet y pescado del día en puertos sin pretensiones.</p>
        <div class="gastro-grid">
          <div class="gastro-col"><h4>🍽 Platos imprescindibles</h4><ul>
            <li><strong>Ensaimada</strong> — dulce espiralado; desayuno en Palma o Sóller</li>
            <li><strong>Sobrasada</strong> — embutido untable con miel en pan moreno</li>
            <li><strong>Tumbet</strong> — verduras gratinadas al estilo mallorquín</li>
            <li><strong>Frit mallorquí</strong> — fritura variada de mar y montaña</li>
          </ul></div>
          <div class="gastro-col"><h4>🐟 Del mar</h4><ul>
            <li><strong>Caldereta de langosta</strong> — Formentor y Colònia de Sant Jordi</li>
            <li><strong>Pescado del día</strong> — Port de Sóller, Port de Pollença, Sant Jordi</li>
            <li><strong>Arroz brut</strong> — caldo espeso con verduras y carne</li>
            <li><strong>Hierbas</strong> — licor de hierbas secas de la isla</li>
          </ul></div>
          <div class="gastro-col"><h4>📍 Dónde probarlo</h4><ul>
            <li><strong>Forn Fondo</strong> — ensaimadas en Palma</li>
            <li><strong>Ca'n Torrat</strong> — Valldemossa (cocina local)</li>
            <li><strong>Restaurante Formentor</strong> — vistas al cabo</li>
            <li><strong>Es Molí d'en Bou</strong> — Sa Coma (alta cocina mallorquina)</li>
          </ul></div>
        </div>
      </div>
    </div>
  </section>

  <section id="consejos">
    <div class="container">
      <p class="section-label">Práctico</p>
      <h2 class="section-title">Consejos esenciales</h2>
      <div class="intro-grid">
        <div class="intro-card"><h3>📱 Usar offline en iOS</h3><ol><li>Abre <strong>520vip.space/MALLORCA</strong> o <strong>520520u.github.io/MALLORCA</strong> en Safari</li><li>Pulsa Compartir → «Añadir a pantalla de inicio»</li><li>Con WiFi la primera vez se cachean textos e imágenes</li></ol></div>
        <div class="intro-card"><h3>🚗 Coche</h3><p>Imprescindible. Recogida en aeropuerto de Palma (PMI). Carreteras en buen estado; la de Formentor es estrecha — madruga o ve entre semana. Es Trenc: aparcamiento limitado, llega antes de las 9:00.</p></div>
        <div class="intro-card"><h3>🏖 Playas</h3><p>Lleva escarpines para calas de piedra (Cala Deià). Toalla, agua y crema — sombra escasa en Es Trenc y Formentor. Respeta zonas protegidas en Mondragó y Ses Salines.</p></div>
        <div class="intro-card"><h3>🌦 Junio</h3><p>Calor real a mediodía (30 °C+). Mejor explorar pueblos por la mañana y playa a partir de las 16:00. Tramuntana puede tener niebla matinal — despeja hacia mediodía.</p></div>
      </div>
      <div class="optimized">
        <p class="section-label" style="color:rgba(255,255,255,.7)">Ruta optimizada</p>
        <h2 class="section-title">Orden ideal · 6 días</h2>
        <div class="optimized-flow">
          <span class="step">D1 Palma</span><span class="arrow">→</span>
          <span class="step">D2 Tramuntana</span><span class="arrow">→</span>
          <span class="step">D3 Formentor</span><span class="arrow">→</span>
          <span class="step">D4 Alcúdia</span><span class="arrow">→</span>
          <span class="step">D5 Calas</span><span class="arrow">→</span>
          <span class="step">D6 Es Trenc</span>
        </div>
        <p style="opacity:.88;max-width:600px;margin:0 auto">Base en Palma (D1), Valldemossa (D2), Pollença (D3), Alcúdia (D4), Santanyí (D5) y sur (D6). Evita domingos en Formentor si puedes — autobuses turísticos abarrotan el mirador.</p>
      </div>
    </div>
  </section>

  <div id="lightbox" class="lightbox" hidden role="dialog" aria-modal="true" aria-label="Imagen ampliada">
    <button type="button" class="lightbox-close" aria-label="Cerrar">×</button>
    <div class="lightbox-inner">
      <img class="lightbox-img" src="" alt="" referrerpolicy="no-referrer">
      <p class="lightbox-cap"></p>
    </div>
  </div>

  <footer>
    <em>Playas, calas y pueblos 🏝🌊</em>
    <p>Guía 6 días · Mallorca · Google Maps</p>
  </footer>

<script>
(function(){{
  var h=document.getElementById('site-header'),t=document.getElementById('nav-toggle'),n=document.getElementById('site-nav');
  if(t&&n){{t.addEventListener('click',function(){{var o=n.classList.toggle('is-open');t.setAttribute('aria-expanded',o?'true':'false');t.textContent=o?'✕':'☰';}});n.querySelectorAll('a').forEach(function(a){{a.addEventListener('click',function(){{n.classList.remove('is-open');t.setAttribute('aria-expanded','false');t.textContent='☰';}});}});}}
  qsa('.full-routes-overview').forEach(function(box){{
    qsa('.route-day-tab',box).forEach(function(tab){{
      tab.addEventListener('click',function(){{
        var d=tab.getAttribute('data-day');
        qsa('.route-day-tab',box).forEach(function(x){{x.classList.toggle('is-active',x===tab);}});
        qsa('.route-day-panel',box).forEach(function(p){{p.classList.toggle('is-active',p.getAttribute('data-day')===d);}});
      }});
    }});
  }});
  function qsa(s,r){{return Array.from((r||document).querySelectorAll(s));}}
  var lb=document.getElementById('lightbox'),lbImg=lb&&lb.querySelector('.lightbox-img'),lbCap=lb&&lb.querySelector('.lightbox-cap'),lbClose=lb&&lb.querySelector('.lightbox-close');
  function openLb(full,cap){{if(!lb)return;lbImg.src=full;lbImg.alt=cap||'';lbCap.textContent=cap||'';lb.hidden=false;lb.classList.add('is-open');document.body.style.overflow='hidden';}}
  function closeLb(){{if(!lb)return;lb.classList.remove('is-open');lb.hidden=true;lbImg.src='';document.body.style.overflow='';}}
  document.addEventListener('click',function(e){{var el=e.target.closest('[data-full]');if(el){{e.preventDefault();openLb(el.getAttribute('data-full'),el.getAttribute('data-cap'));}}}});
  if(lbClose)lbClose.addEventListener('click',closeLb);
  if(lb)lb.addEventListener('click',function(e){{if(e.target===lb)closeLb();}});
  document.addEventListener('keydown',function(e){{if(e.key==='Escape')closeLb();}});
}})();
</script>
</body>
</html>"""

    out = BASE / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"Written {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
