#!/usr/bin/env python3
"""Genera versión PWA y despliega a mallorca-pwa/."""
import shutil
from pathlib import Path

BASE = Path(__file__).parent.resolve()
ROOT = BASE.parent

PWA_HEAD = """  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="default">
  <meta name="format-detection" content="telephone=no">
  <meta name="theme-color" content="#1a6b8a">
  <meta name="apple-mobile-web-app-title" content="Mallorca">
  <meta name="mobile-web-app-capable" content="yes">
  <link rel="manifest" href="manifest.webmanifest">
  <link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
  <link rel="icon" type="image/png" sizes="192x192" href="icons/icon-192.png">
"""

MANIFEST = """{
  "name": "Mallorca · Guía 6 Días",
  "short_name": "Mallorca",
  "description": "Guía slow travel por Mallorca: playas, paisajes y pueblos con mapas Google Maps e itinerario 6 días.",
  "lang": "es",
  "start_url": "./index.html",
  "scope": "./",
  "display": "standalone",
  "orientation": "portrait-primary",
  "background_color": "#f5f0e8",
  "theme_color": "#1a6b8a",
  "categories": ["travel", "navigation"],
  "icons": [
    { "src": "./icons/icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any" },
    { "src": "./icons/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any" },
    { "src": "./icons/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable" }
  ]
}
"""

SW_JS = """/* Mallorca Guía — Service Worker */
const CACHE = 'mallorca-guia-v1';
const APP_SHELL = [
  './',
  './index.html',
  './manifest.webmanifest',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/apple-touch-icon.png',
  './icons/icon.svg'
];
const IMAGE_HOSTS = ['images.unsplash.com'];

self.addEventListener('install', function (event) {
  event.waitUntil(
    caches.open(CACHE).then(function (cache) {
      return cache.addAll(APP_SHELL);
    }).then(function () { return self.skipWaiting(); })
  );
});

self.addEventListener('activate', function (event) {
  event.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.filter(function (k) { return k !== CACHE; }).map(function (k) {
        return caches.delete(k);
      }));
    }).then(function () { return self.clients.claim(); })
  );
});

self.addEventListener('fetch', function (event) {
  var req = event.request;
  if (req.method !== 'GET') return;
  var url;
  try { url = new URL(req.url); } catch (e) { return; }

  if (url.origin !== self.location.origin && IMAGE_HOSTS.indexOf(url.hostname) === -1) return;

  if (IMAGE_HOSTS.indexOf(url.hostname) !== -1) {
    event.respondWith(
      caches.open(CACHE).then(function (cache) {
        return cache.match(req).then(function (cached) {
          if (cached) return cached;
          return fetch(req).then(function (res) {
            if (res && res.ok) cache.put(req, res.clone());
            return res;
          }).catch(function () { return cached; });
        });
      })
    );
    return;
  }

  if (req.mode === 'navigate') {
    event.respondWith(
      caches.match('./index.html').then(function (cached) {
        var network = fetch(req).then(function (res) {
          if (res && res.ok) {
            var copy = res.clone();
            caches.open(CACHE).then(function (c) { c.put('./index.html', copy); });
          }
          return res;
        });
        return cached || network;
      }).catch(function () { return caches.match('./index.html'); })
    );
    return;
  }

  if (url.origin === self.location.origin) {
    event.respondWith(
      caches.match(req).then(function (cached) {
        return cached || fetch(req).then(function (res) {
          if (res && res.ok) {
            var copy = res.clone();
            caches.open(CACHE).then(function (c) { c.put(req, copy); });
          }
          return res;
        });
      })
    );
  }
});
"""

PWA_CSS = """
    .pwa-install{position:fixed;bottom:1rem;left:1rem;right:1rem;max-width:420px;margin:0 auto;padding:1rem;background:var(--sea);color:#fff;border-radius:14px;box-shadow:0 8px 32px rgba(0,0,0,.2);z-index:9999;font-size:.9rem;display:flex;align-items:center;gap:.75rem}
    .pwa-install[hidden]{display:none!important}
    .pwa-install-text{flex:1;line-height:1.4}
    .pwa-install-btn{padding:.5rem 1rem;background:var(--coral);color:var(--sea);border:none;border-radius:100px;font-weight:600;cursor:pointer;font-size:.85rem}
    .pwa-install-close{width:2rem;height:2rem;border:none;border-radius:50%;background:rgba(255,255,255,.15);color:#fff;font-size:1.25rem;cursor:pointer}
"""

PWA_BANNER = """
  <div id="pwa-install" class="pwa-install" hidden>
    <p class="pwa-install-text">Instala la guía en tu iPhone para acceso rápido y contenido cacheado.</p>
    <div class="pwa-install-actions">
      <button type="button" class="pwa-install-btn" id="pwa-install-btn">Instalar</button>
      <button type="button" class="pwa-install-close" id="pwa-install-close" aria-label="Cerrar">×</button>
    </div>
  </div>
"""

PWA_SCRIPT = """
<script>
(function () {
  'use strict';
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', function () {
      navigator.serviceWorker.register('./sw.js', { scope: './' }).catch(function () {});
    });
  }
  var DISMISS_KEY = 'mallorca-pwa-banner-dismissed';
  var deferredPrompt;
  var banner = document.getElementById('pwa-install');
  var btn = document.getElementById('pwa-install-btn');
  var closeBtn = document.getElementById('pwa-install-close');
  function hideBanner(persist) {
    if (!banner) return;
    banner.hidden = true;
    if (persist !== false) { try { localStorage.setItem(DISMISS_KEY, '1'); } catch (e) {} }
  }
  function showBanner() {
    if (!banner) return;
    try { if (localStorage.getItem(DISMISS_KEY)) return; } catch (e) {}
    banner.hidden = false;
  }
  if (closeBtn) closeBtn.addEventListener('click', function () { hideBanner(true); });
  if (window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone) {
    hideBanner(false);
  } else {
    window.addEventListener('beforeinstallprompt', function (e) {
      e.preventDefault(); deferredPrompt = e; showBanner();
    });
    if (btn) btn.addEventListener('click', function () {
      if (deferredPrompt) {
        deferredPrompt.prompt();
        deferredPrompt.userChoice.finally(function () { deferredPrompt = null; hideBanner(true); });
        return;
      }
      alert('En iPhone/iPad: pulsa Compartir en Safari y elige «Añadir a pantalla de inicio».');
    });
    var isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
    if (isIOS) setTimeout(function () {
      if (!window.matchMedia('(display-mode: standalone)').matches) showBanner();
    }, 2500);
  }
})();
</script>
"""


def patch_html(html: str) -> str:
    if 'manifest.webmanifest' not in html:
        html = html.replace(
            '  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">\n  <meta name="theme-color"',
            '  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">\n' + PWA_HEAD + '  <meta name="theme-color"',
            1,
        )
    if '.pwa-install' not in html:
        html = html.replace('  </style>\n</head>', PWA_CSS + '  </style>\n</head>', 1)
    if 'pwa-install' not in html:
        html = html.replace('<body>', '<body>\n' + PWA_BANNER, 1)
    if 'serviceWorker.register' not in html:
        html = html.replace('</body>', PWA_SCRIPT + '\n</body>', 1)
    return html


def deploy_dir(target: Path):
    target.mkdir(parents=True, exist_ok=True)
    icons = target / "icons"
    icons.mkdir(exist_ok=True)
    html = patch_html((BASE / "index.html").read_text(encoding="utf-8"))
    (target / "index.html").write_text(html, encoding="utf-8")
    (target / "manifest.webmanifest").write_text(MANIFEST.strip() + "\n", encoding="utf-8")
    (target / "sw.js").write_text(SW_JS.strip() + "\n", encoding="utf-8")
    for f in (BASE / "icons").glob("*"):
        shutil.copy2(f, icons / f.name)
    src_images = BASE / "images"
    if src_images.is_dir():
        dst_images = target / "images"
        if dst_images.exists():
            shutil.rmtree(dst_images)
        shutil.copytree(src_images, dst_images)


def main():
    deploy_dir(ROOT / "mallorca-pwa")
    docs = ROOT / "docs-mallorca"
    deploy_dir(docs)
    print("PWA:", ROOT / "mallorca-pwa")
    print("Docs:", docs)


if __name__ == "__main__":
    main()
