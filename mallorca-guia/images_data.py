"""Imágenes reales por sitio — Wikimedia Commons, varias fotos por lugar."""

# Principal + extras descargados a ./images/
MAINS = {
    "palma": {"file": "palma_main.jpg", "cap": "Palma — casco histórico y calles del centro"},
    "cathedral": {"file": "cathedral_main.jpg", "cap": "La Seu — catedral de Palma desde el Parc de la Mar"},
    "soller": {"file": "soller_main.jpg", "cap": "Sóller — estación del tren de palma a Sóller"},
    "port_soller": {"file": "port_soller_main.jpg", "cap": "Port de Sóller — bahía y paseo marítimo"},
    "valldemossa": {"file": "valldemossa_main.jpg", "cap": "Valldemossa — pueblo de piedra en la Tramuntana"},
    "deia": {"file": "deia_main.jpg", "cap": "Deià — casas en terrazas sobre el Mediterráneo"},
    "cala_deia": {"file": "cala_deia_main.jpg", "cap": "Cala Deià — cala de piedra y agua turquesa"},
    "banyalbufar": {"file": "banyalbufar_main.jpg", "cap": "Banyalbufar — bancales al borde del acantilado"},
    "pollenca": {"file": "pollenca_main.jpg", "cap": "Pollença — calle Calvari y casco antiguo"},
    "formentor": {"file": "formentor_main.jpg", "cap": "Cap de Formentor — faro y acantilados"},
    "port_pollenca": {"file": "port_pollenca_main.jpg", "cap": "Port de Pollença — bahía y montaña de fondo"},
    "cala_san_vicente": {"file": "cala_san_vicente_main.jpg", "cap": "Cala San Vicenç — cala tranquila del norte"},
    "alcudia": {"file": "alcudia_main.jpg", "cap": "Alcúdia — murallas medievales y calles empedradas"},
    "playa_muro": {"file": "playa_muro_main.jpg", "cap": "Playa de Muro — arena blanca y aguas poco profundas"},
    "arta": {"file": "arta_main.jpg", "cap": "Artà — pueblo con encanto bajo la sierra"},
    "cala_mesquida": {"file": "cala_mesquida_main.jpg", "cap": "Cala Mesquida — playa virgen del noreste"},
    "cala_mondrago": {"file": "cala_mondrago_main.jpg", "cap": "Cala Mondragó — parque natural y calas turquesas"},
    "santanyi": {"file": "santanyi_main.jpg", "cap": "Santanyí — pueblo de piedra dorada"},
    "cala_dor": {"file": "cala_dor_main.jpg", "cap": "Cala d'Or — calas en forma de herradura"},
    "porto_cristo": {"file": "porto_cristo_main.jpg", "cap": "Porto Cristo — puerto pesquero y cuevas del Drach"},
    "es_trenc": {"file": "es_trenc_main.jpg", "cap": "Es Trenc — la playa virgen del sur"},
    "ses_salines": {"file": "ses_salines_main.jpg", "cap": "Ses Salines — dunas y salinas naturales"},
    "sant_jordi": {"file": "sant_jordi_main.jpg", "cap": "Colònia de Sant Jordi — pueblo marinero del sur"},
    "capdepera": {"file": "capdepera_main.jpg", "cap": "Capdepera — castillo medieval con vistas a Menorca"},
}

EXTRAS = {
    "palma": [
        {"file": "palma_e1.jpg", "cap": "Ayuntamiento de Palma — detalle de la fachada (Wikimedia)"},
        {"file": "palma_e2.jpg", "cap": "Palma de Mallorca — calles del centro (Wikimedia)"},
    ],
    "cathedral": [
        {"file": "cathedral_e1.jpg", "cap": "La Seu — portal principal (Wikimedia)"},
        {"file": "cathedral_e2.jpg", "cap": "Catedral de Palma — fachada lateral (Wikimedia)"},
    ],
    "soller": [
        {"file": "soller_e1.jpg", "cap": "Plaza de Sóller — ambiente de pueblo (Wikimedia)"},
        {"file": "soller_e2.jpg", "cap": "Tren de Sóller en la estación (Wikimedia)"},
    ],
    "port_soller": [
        {"file": "port_soller_e1.jpg", "cap": "Port de Sóller — vista desde la plaza (Wikimedia)"},
        {"file": "port_soller_e2.jpg", "cap": "Port de Sóller — bahía y barcos (Wikimedia)"},
    ],
    "valldemossa": [
        {"file": "valldemossa_e1.jpg", "cap": "Real Cartuja de Valldemossa — patio (Wikimedia)"},
        {"file": "valldemossa_e2.jpg", "cap": "Valldemossa — calles del pueblo (Wikimedia)"},
    ],
    "deia": [
        {"file": "deia_e1.jpg", "cap": "Deià — casas sobre el valle (Wikimedia)"},
        {"file": "deia_e2.jpg", "cap": "Deià — pueblo de los artistas (Wikimedia)"},
    ],
    "cala_deia": [
        {"file": "cala_deia_e1.jpg", "cap": "Cala Deià — rocas y agua clara (Wikimedia)"},
        {"file": "cala_deia_e2.jpg", "cap": "Cala Deià — vista desde el sendero (Wikimedia)"},
    ],
    "banyalbufar": [
        {"file": "banyalbufar_e1.jpg", "cap": "Banyalbufar — terrazas de cultivo (Wikimedia)"},
        {"file": "banyalbufar_e2.jpg", "cap": "Banyalbufar — acantilado y mar (Wikimedia)"},
    ],
    "pollenca": [
        {"file": "pollenca_e1.jpg", "cap": "Escalinata del Calvari — Pollença (Wikimedia)"},
        {"file": "pollenca_e2.jpg", "cap": "Pollença — plaza y casco antiguo (Wikimedia)"},
    ],
    "formentor": [
        {"file": "formentor_e1.jpg", "cap": "Far de Formentor (Wikimedia)"},
        {"file": "formentor_e2.jpg", "cap": "Mirador Es Colomer — acantilados (Wikimedia)"},
    ],
    "port_pollenca": [
        {"file": "port_pollenca_e1.jpg", "cap": "Port de Pollença — paseo marítimo (Wikimedia)"},
        {"file": "port_pollenca_e2.jpg", "cap": "Port de Pollença — bahía al atardecer (Wikimedia)"},
    ],
    "cala_san_vicente": [
        {"file": "cala_san_vicente_e1.jpg", "cap": "Cala San Vicenç — playa entre rocas (Wikimedia)"},
        {"file": "cala_san_vicente_e2.jpg", "cap": "Cala Sant Vicenç — aguas tranquilas (Wikimedia)"},
    ],
    "alcudia": [
        {"file": "alcudia_e1.jpg", "cap": "Murallas de Alcúdia (Wikimedia)"},
        {"file": "alcudia_e2.jpg", "cap": "Casco antiguo de Alcúdia (Wikimedia)"},
    ],
    "playa_muro": [
        {"file": "playa_muro_e1.jpg", "cap": "Platja de Muro — arena blanca (Wikimedia)"},
        {"file": "playa_muro_e2.jpg", "cap": "Playa de Muro — bahía de Alcúdia (Wikimedia)"},
    ],
    "arta": [
        {"file": "arta_e1.jpg", "cap": "Sant Salvador — santuario sobre Artà (Wikimedia)"},
        {"file": "arta_e2.jpg", "cap": "Artà — calles del pueblo (Wikimedia)"},
    ],
    "cala_mesquida": [
        {"file": "cala_mesquida_e1.jpg", "cap": "Cala Mesquida — playa e isla rocosa (Wikimedia)"},
        {"file": "cala_mesquida_e2.jpg", "cap": "Cala Mesquida — vista aérea de la cala (Wikimedia)"},
    ],
    "cala_mondrago": [
        {"file": "cala_mondrago_e1.jpg", "cap": "Cala Mondragó — pinos hasta el agua (Wikimedia)"},
        {"file": "cala_mondrago_e2.jpg", "cap": "Parque natural de Mondragó (Wikimedia)"},
    ],
    "santanyi": [
        {"file": "santanyi_e1.jpg", "cap": "Santanyí — plaza mayor (Wikimedia)"},
        {"file": "santanyi_e2.jpg", "cap": "Santanyí — arquitectura de piedra dorada (Wikimedia)"},
    ],
    "cala_dor": [
        {"file": "cala_dor_e1.jpg", "cap": "Cala Ferrera — cala en herradura (Wikimedia)"},
        {"file": "cala_dor_e2.jpg", "cap": "Cala d'Or — aguas turquesas (Wikimedia)"},
    ],
    "porto_cristo": [
        {"file": "porto_cristo_e1.jpg", "cap": "Cuevas del Drach — lago subterráneo (Wikimedia)"},
        {"file": "porto_cristo_e2.jpg", "cap": "Porto Cristo — puerto pesquero (Wikimedia)"},
    ],
    "es_trenc": [
        {"file": "es_trenc_e1.jpg", "cap": "Es Trenc — dunas y arena blanca (Wikimedia)"},
        {"file": "es_trenc_e2.jpg", "cap": "Platja d'Es Trenc — agua transparente (Wikimedia)"},
    ],
    "ses_salines": [
        {"file": "ses_salines_e1.jpg", "cap": "Salinas de Ses Salines (Wikimedia)"},
        {"file": "ses_salines_e2.jpg", "cap": "Parque natural de Ses Salines (Wikimedia)"},
    ],
    "sant_jordi": [
        {"file": "sant_jordi_e1.jpg", "cap": "Colònia de Sant Jordi — puerto (Wikimedia)"},
        {"file": "sant_jordi_e2.jpg", "cap": "Colònia de Sant Jordi — pueblo marinero (Wikimedia)"},
    ],
    "capdepera": [
        {"file": "capdepera_e1.jpg", "cap": "Castell de Capdepera — murallas (Wikimedia)"},
        {"file": "capdepera_e2.jpg", "cap": "Capdepera — vistas desde el castillo (Wikimedia)"},
    ],
}

REMOTE = {
    "palma_main.jpg": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Casa_de_la_Ciutat_de_Palma_de_Mallorca.jpeg",
    "palma_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/a/aa/Detall_del_r%C3%A0fec_decorat_de_la_teulada_de_l%27ajuntament_de_Palma_de_Mallorca.jpeg",
    "palma_e2.jpg": "https://upload.wikimedia.org/wikipedia/commons/9/94/2007-08-15_Spain_Mallorca_Palma_coach.JPG",
    "cathedral_main.jpg": "https://upload.wikimedia.org/wikipedia/commons/5/54/Palma_Cathedral_%28La_Seu%29_and_reflection_at_Parc_de_la_Mar.jpg",
    "cathedral_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/5/59/Palma_Catedral_La_Seu_de_Mallorca_Portal-3964.jpg",
    "cathedral_e2.jpg": "https://upload.wikimedia.org/wikipedia/commons/1/12/Kathedrale_von_Palma_II.jpg",
    "soller_main.jpg": "https://upload.wikimedia.org/wikipedia/commons/2/28/Depot_of_S%C3%B3ller_train_station_05.jpg",
    "soller_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Girl_in_Plaza_-_Soller_-_Mallorca_-_Spain_%2814497674766%29.jpg",
    "soller_e2.jpg": "https://upload.wikimedia.org/wikipedia/commons/b/bf/Depot_of_S%C3%B3ller_train_station_04.jpg",
    "port_soller_main.jpg": "https://upload.wikimedia.org/wikipedia/commons/3/33/View_from_Pla%C3%A7a_de_Santa_Catarina_in_Port_de_S%C3%B3ller_04.jpg",
    "port_soller_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/e/e3/View_from_Pla%C3%A7a_de_Santa_Catarina_in_Port_de_S%C3%B3ller_06.jpg",
    "port_soller_e2.jpg": "https://upload.wikimedia.org/wikipedia/commons/b/b6/View_from_Pla%C3%A7a_de_Santa_Catarina_in_Port_de_S%C3%B3ller_07.jpg",
    "valldemossa_main.jpg": "https://upload.wikimedia.org/wikipedia/commons/7/75/Valldemossa_view.jpg",
    "valldemossa_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/9/95/Valldemossa_Cartoixa_Patio-3875.jpg",
    "valldemossa_e2.jpg": "https://upload.wikimedia.org/wikipedia/commons/8/8c/Valldemossa._Na_Torta.jpg",
    "deia_main.jpg": "https://upload.wikimedia.org/wikipedia/commons/8/87/Dei%C3%A0%2C_2.jpg",
    "deia_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/3/39/Dei%C3%A0%2C_Mallorca_%2813333899675%29.jpg",
    "deia_e2.jpg": "https://upload.wikimedia.org/wikipedia/commons/5/56/Dei%C3%A0%2C_Mallorca_%2813333982693%29.jpg",
    "cala_deia_main.jpg": "https://upload.wikimedia.org/wikipedia/commons/3/37/Cala_de_Deya%2C_Mallorca_%2813333935885%29.jpg",
    "cala_deia_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/5/56/Cala_de_Deya%2C_Mallorca_%2813333941493%29.jpg",
    "cala_deia_e2.jpg": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Cala_de_Deya%2C_Mallorca_%2813334053713%29.jpg",
    "banyalbufar_main.jpg": "https://upload.wikimedia.org/wikipedia/commons/2/28/Banyalbufar%2C_Carrer_Comte_de_Sallent%2C_01.jpg",
    "banyalbufar_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/1/1f/Banyalbufar_terraces_1.JPG",
    "banyalbufar_e2.jpg": "https://upload.wikimedia.org/wikipedia/commons/8/8c/Banyalbufar_009.JPG",
    "pollenca_main.jpg": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Almond_blossom_at_El_Calvari_01.jpg",
    "pollenca_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/7/75/Pollenca%2C_Carrer_de_Metge_Sureda%2C_torre_iglesia.jpg",
    "pollenca_e2.jpg": "https://upload.wikimedia.org/wikipedia/commons/e/ec/In_Pollen%C3%A7a_09.jpg",
    "formentor_main.jpg": "https://upload.wikimedia.org/wikipedia/commons/e/e5/Cap_Formentor_2015_%28Zuschnitt%29.jpg",
    "formentor_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/c/cf/Cap_Formentor_2015.jpg",
    "formentor_e2.jpg": "https://upload.wikimedia.org/wikipedia/commons/c/cf/Cap_Formentor_2015.jpg",
    "port_pollenca_main.jpg": "https://upload.wikimedia.org/wikipedia/commons/2/26/Boquer_Valley_and_Port_de_Pollen%C3%A7a_from_the_air.JPG",
    "port_pollenca_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/e/ee/Majorca_%2C_Pollenca_Harbour_%2C_July_2008_-_panoramio.jpg",
    "port_pollenca_e2.jpg": "https://upload.wikimedia.org/wikipedia/commons/e/ee/Majorca_%2C_Pollenca_Harbour_%2C_July_2008_-_panoramio.jpg",
    "cala_san_vicente_main.jpg": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Cala_de_San_Vicente._Mallorca_%2817828469484%29.jpg",
    "cala_san_vicente_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/5/5a/02017_0126_Cala_Sant_Vicen%C3%A7%2C_Majorca.jpg",
    "cala_san_vicente_e2.jpg": "https://upload.wikimedia.org/wikipedia/commons/b/b0/Cala_de_San_Vicente._Mallorca_%2817830419653%29.jpg",
    "alcudia_main.jpg": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Alcudia_Old_Town_suburbs_-_panoramio.jpg",
    "alcudia_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/a/af/Alcudia_City_Walls_R04.jpg",
    "alcudia_e2.jpg": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Alcudia_muralla_1.jpg",
    "playa_muro_main.jpg": "https://upload.wikimedia.org/wikipedia/commons/3/3e/16-02-22-Playa-de-Muro-Mallorca-RalfR_RR26379.jpg",
    "playa_muro_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/4/47/Luftbild_Es_Com%C3%BA_01.jpg",
    "playa_muro_e2.jpg": "https://upload.wikimedia.org/wikipedia/commons/4/41/Platja_de_Muro_R01.jpg",
    "arta_main.jpg": "https://upload.wikimedia.org/wikipedia/commons/6/65/Ajuntament_d_Art%C3%A0_courtyard.jpg",
    "arta_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/c/ce/Art%C3%A0_%28Sant_Salvador%29_03_ies.jpg",
    "arta_e2.jpg": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Mallorca_Art%C3%A0_church_asv2023-04.jpg",
    "cala_mesquida_main.jpg": "https://upload.wikimedia.org/wikipedia/commons/6/6c/Cala_Mesquida%2C_Art%C3%A0%2C_Mallorca%2C_Espa%C3%B1a.jpg",
    "cala_mesquida_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Aerial_view_of_Cala_Mesquida_beach_and_sand_dunes_in_Mallorca%2C_Spain_%2848001486971%29.jpg",
    "cala_mesquida_e2.jpg": "https://upload.wikimedia.org/wikipedia/commons/6/6c/Cala_Mesquida%2C_Art%C3%A0%2C_Mallorca%2C_Espa%C3%B1a.jpg",
    "cala_mondrago_main.jpg": "https://upload.wikimedia.org/wikipedia/commons/5/55/Cala_Mondrag%C3%B3_05.jpg",
    "cala_mondrago_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/2/21/Cala_Mondrago%2C_near_Porto_Petro%2C_Cala_D%27or%2C_Majorca_%284223115749%29.jpg",
    "cala_mondrago_e2.jpg": "https://upload.wikimedia.org/wikipedia/commons/3/3b/Mondrag%C3%B3_01.jpg",
    "santanyi_main.jpg": "https://upload.wikimedia.org/wikipedia/commons/2/28/001_2014_03_17_11_Kai.jpg",
    "santanyi_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/2/21/Mallorca-Santany%C3%AD_%28city%29-Pla%C3%A7a_Major-market-01.jpg",
    "santanyi_e2.jpg": "https://upload.wikimedia.org/wikipedia/commons/1/10/Mallorca-Santany%C3%AD_%28city%29-Market-04.jpg",
    "cala_dor_main.jpg": "https://upload.wikimedia.org/wikipedia/commons/4/4f/Cala_D%27or%2C_Illes_Balears%2C_Spain_-_panoramio_%2836%29.jpg",
    "cala_dor_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Cala_Ferrera_02.jpg",
    "cala_dor_e2.jpg": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Cala_Esmeralda%2C_en_Cala_d%27Or_%28Santa%C3%B1%C3%AD%2C_Espa%C3%B1a%29.jpg",
    "porto_cristo_main.jpg": "https://upload.wikimedia.org/wikipedia/commons/1/1c/Carrer_d%27en_Bordils_Porto_Cristo_view_towards_harbour.jpg",
    "porto_cristo_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/1/16/Cueva_del_Drach_Mallorca_01.jpg",
    "porto_cristo_e2.jpg": "https://upload.wikimedia.org/wikipedia/commons/4/40/Mallorca_Porto_Cristo_seaport_area_asv2023-04_img1.jpg",
    "es_trenc_main.jpg": "https://upload.wikimedia.org/wikipedia/commons/9/9c/Es_Trenc%2C_Mallorca%2C_the_beach.jpg",
    "es_trenc_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/9/9c/Es_Trenc%2C_Mallorca%2C_the_beach.jpg",
    "es_trenc_e2.jpg": "https://upload.wikimedia.org/wikipedia/commons/9/9c/Es_Trenc%2C_Mallorca%2C_the_beach.jpg",
    "ses_salines_main.jpg": "https://upload.wikimedia.org/wikipedia/commons/c/c0/003_2015_06_06_Schatten.jpg",
    "ses_salines_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/c/c0/003_2015_06_06_Schatten.jpg",
    "ses_salines_e2.jpg": "https://upload.wikimedia.org/wikipedia/commons/c/c0/003_2015_06_06_Schatten.jpg",
    "sant_jordi_main.jpg": "https://upload.wikimedia.org/wikipedia/commons/d/d0/Mallorca-Col%C3%B2nia_de_Sant_Jordi-Cala_Galiota-01E.jpg",
    "sant_jordi_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/c/c4/Mallorca-Colonia_de_Sant_Jordi-Minigolf-03.jpg",
    "sant_jordi_e2.jpg": "https://upload.wikimedia.org/wikipedia/commons/1/12/Colonia_de_Sant_Jordi_-_panoramio.jpg",
    "capdepera_main.jpg": "https://upload.wikimedia.org/wikipedia/commons/3/34/Capdepera%2C_en_Baleares_%28Espa%C3%B1a%29.jpg",
    "capdepera_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/1/1f/Capdepera_-_Castell_de_Capdepera_06_ies.jpg",
    "capdepera_e2.jpg": "https://upload.wikimedia.org/wikipedia/commons/5/56/Castillo_De_Capdepera_%28149971589%29.jpeg",
}

DAYS = [
    {"num": 1, "spots": ["palma", "cathedral", "soller", "port_soller"], "gmaps": ["Palma de Mallorca, Spain", "Palma Cathedral, Mallorca", "Sóller, Mallorca", "Port de Sóller, Mallorca"], "map_id": "map-day1"},
    {"num": 2, "spots": ["valldemossa", "deia", "cala_deia", "banyalbufar"], "gmaps": ["Sóller, Mallorca", "Valldemossa, Mallorca", "Deià, Mallorca", "Banyalbufar, Mallorca"], "map_id": "map-day2"},
    {"num": 3, "spots": ["pollenca", "formentor", "port_pollenca", "cala_san_vicente"], "gmaps": ["Pollença, Mallorca", "Cap de Formentor, Mallorca", "Port de Pollença, Mallorca", "Cala San Vicente, Pollença"], "map_id": "map-day3"},
    {"num": 4, "spots": ["alcudia", "playa_muro", "arta", "cala_mesquida"], "gmaps": ["Alcúdia, Mallorca", "Platja de Muro, Mallorca", "Artà, Mallorca", "Cala Mesquida, Mallorca"], "map_id": "map-day4"},
    {"num": 5, "spots": ["cala_mondrago", "santanyi", "cala_dor", "porto_cristo"], "gmaps": ["Cala Mondragó, Mallorca", "Santanyí, Mallorca", "Cala d'Or, Mallorca", "Porto Cristo, Mallorca"], "map_id": "map-day5"},
    {"num": 6, "spots": ["es_trenc", "ses_salines", "sant_jordi", "capdepera"], "gmaps": ["Es Trenc, Mallorca", "Ses Salines, Mallorca", "Colònia de Sant Jordi, Mallorca", "Capdepera, Mallorca"], "map_id": "map-day6"},
]

DAY_TAB_LABELS = {
    1: "D1 · Palma",
    2: "D2 · Tramuntana",
    3: "D3 · Formentor",
    4: "D4 · Alcúdia",
    5: "D5 · Calas",
    6: "D6 · Es Trenc",
}


def thumb_path(file):
    stem, ext = file.rsplit(".", 1)
    return f"./images/{stem}_thumb.{ext}"


def full_path(file):
    return f"./images/{file}"


def photos_for_key(key):
    """Todas las fotos de un sitio: principal + extras."""
    photos = []
    m = MAINS[key]
    photos.append({"url": thumb_path(m["file"]), "full": full_path(m["file"]), "cap": m["cap"], "key": key})
    for ex in EXTRAS.get(key, []):
        photos.append({"url": thumb_path(ex["file"]), "full": full_path(ex["file"]), "cap": ex["cap"], "key": key})
    return photos
