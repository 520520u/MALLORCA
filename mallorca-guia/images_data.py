"""Imágenes por sitio: principal Unsplash + extras Wikimedia locales."""

MAINS = {
    "palma": {"url": "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?w=800&q=80", "cap": "Palma — catedral y casco histórico"},
    "cathedral": {"url": "https://images.unsplash.com/photo-1558642452-9d2b7bef6b69?w=800&q=80", "cap": "La Seu — catedral de Palma al atardecer"},
    "soller": {"url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&q=80", "cap": "Sóller — valle de naranjos y montaña"},
    "port_soller": {"url": "https://images.unsplash.com/photo-1505142468610-359e7d316be0?w=800&q=80", "cap": "Port de Sóller — bahía mediterránea"},
    "valldemossa": {"url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800&q=80", "cap": "Valldemossa — pueblo de piedra en la Tramuntana"},
    "deia": {"url": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&q=80", "cap": "Deià — terrazas sobre el mar"},
    "cala_deia": {"url": "https://images.unsplash.com/photo-1473496162514-6ef8162b2b1c?w=800&q=80", "cap": "Cala Deià — cala de piedra y agua turquesa"},
    "banyalbufar": {"url": "https://images.unsplash.com/photo-1439066615861-d1af74d74000?w=800&q=80", "cap": "Banyalbufar — bancales al borde del acantilado"},
    "pollenca": {"url": "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=800&q=80", "cap": "Pollença — plaza mayor y calle Calvari"},
    "formentor": {"url": "https://images.unsplash.com/photo-1500375592092-40eb2168fd21?w=800&q=80", "cap": "Cap de Formentor — acantilados y mirador"},
    "port_pollenca": {"url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&q=80", "cap": "Port de Pollença — paseo marítimo y montaña"},
    "cala_san_vicente": {"url": "https://images.unsplash.com/photo-1473496162514-6ef8162b2b1c?w=800&q=80", "cap": "Cala San Vicenç — cala tranquila del norte"},
    "alcudia": {"url": "https://images.unsplash.com/photo-1523906834658-6e24ef2386f9?w=800&q=80", "cap": "Alcúdia — murallas medievales y calles empedradas"},
    "playa_muro": {"url": "https://images.unsplash.com/photo-1505142468610-359e7d316be0?w=800&q=80", "cap": "Playa de Muro — arena blanca y aguas poco profundas"},
    "arta": {"url": "https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=800&q=80", "cap": "Artà — pueblo con encanto bajo la sierra"},
    "cala_mesquida": {"url": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&q=80", "cap": "Cala Mesquida — playa virgen del noreste"},
    "cala_mondrago": {"url": "https://images.unsplash.com/photo-1592634186523-484938bc3c22?w=800&q=80", "cap": "Cala Mondragó — parque natural y calas turquesas"},
    "santanyi": {"url": "https://images.unsplash.com/photo-1568330265107-7dd078486284?w=800&q=80", "cap": "Santanyí — pueblo de piedra dorada"},
    "cala_dor": {"url": "https://images.unsplash.com/photo-1747752419876-50b8d12d68f2?w=800&q=80", "cap": "Cala d'Or — calas en forma de herradura"},
    "porto_cristo": {"url": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=800&q=80", "cap": "Porto Cristo — puerto pesquero y cuevas"},
    "es_trenc": {"url": "https://images.unsplash.com/photo-1651918858137-d3d484d35854?w=800&q=80", "cap": "Es Trenc — la playa virgen del sur"},
    "ses_salines": {"url": "https://images.unsplash.com/photo-1592634378917-49e37742ee21?w=800&q=80", "cap": "Ses Salines — dunas y salinas naturales"},
    "sant_jordi": {"url": "https://images.unsplash.com/photo-1598345042882-4448d0ed51de?w=800&q=80", "cap": "Colònia de Sant Jordi — pueblo marinero del sur"},
    "capdepera": {"url": "https://images.unsplash.com/photo-1663790161767-cba32a06bbfd?w=800&q=80", "cap": "Capdepera — castillo con vistas a Menorca"},
}

EXTRAS = {
    "cathedral": [{"file": "cathedral_e1.jpg", "cap": "Catedral de Palma — fachada (Wikimedia)"}],
    "formentor": [{"file": "formentor_e1.jpg", "cap": "Far de Formentor (Wikimedia)"}],
    "valldemossa": [{"file": "valldemossa_e1.jpg", "cap": "Real Cartuja de Valldemossa (Wikimedia)"}],
    "es_trenc": [{"file": "es_trenc_e1.jpg", "cap": "Playa de Es Trenc (Wikimedia)"}],
    "soller": [{"file": "soller_e1.jpg", "cap": "Tren de Sóller (Wikimedia)"}],
}

REMOTE = {
    "cathedral_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Palma_de_Mallorca_%28Cathedral%29.jpg",
    "formentor_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/8/8a/Far_de_Formentor%2C_Mallorca.jpg",
    "valldemossa_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Valldemossa_Charterhouse.jpg",
    "es_trenc_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Es_Trenc%2C_Mallorca.jpg",
    "soller_e1.jpg": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Soller_Train%2C_Mallorca.jpg",
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
