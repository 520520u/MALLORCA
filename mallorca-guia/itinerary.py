"""Itinerario 6 días — Mallorca: playas, paisajes y pueblos con encanto."""

D1 = ["palma", "cathedral", "soller", "port_soller"]
D2 = ["valldemossa", "deia", "cala_deia", "banyalbufar"]
D3 = ["pollenca", "formentor", "port_pollenca", "cala_san_vicente"]
D4 = ["alcudia", "playa_muro", "arta", "cala_mesquida"]
D5 = ["cala_mondrago", "santanyi", "cala_dor", "porto_cristo"]
D6 = ["es_trenc", "ses_salines", "sant_jordi", "capdepera"]


def build_days(day_block, gallery, spot):
    d = ""
    d += day_block(
        1, "Palma & Sóller", "La capital y el valle de naranjos",
        "75", "1 h 30", "3/5",
        "Palma <span class=\"arrow\">→</span> La Seu <span class=\"arrow\">→</span> Sóller <span class=\"arrow\">→</span> Port de Sóller",
        "El primer día mezcla ciudad y mar: la catedral de Palma al atardecer, el tranvía centenario hasta Sóller y una bahía donde el olor a naranja se mezcla con el salitre. Palma puede abrumar a mediodía — madruga y te regala calles vacías.",
        gallery(1, *D1),
        "<li>Paseo por el casco antiguo de Palma</li><li>Visita La Seu (catedral)</li><li>Tren de Sóller + tranvía al puerto</li><li>Baño en Port de Sóller al atardecer</li>",
        "<li>9:00 Palma — casco antiguo</li><li>11:00 La Seu</li><li>13:00 Tren a Sóller</li><li>16:00 Port de Sóller</li><li>19:00 Cena en el puerto</li>",
        spot(1, D1, "palma", "Palma", "Calles empedradas, patios escondidos y la lonja gótica. Olor a ensaimada recién horneada en cada esquina del centro.") +
        spot(1, D1, "cathedral", "La Seu", "La catedral de Palma flota sobre el mar — Gaudí intervino en su interior. Luz filtrada por rosetones al atardecer.") +
        spot(1, D1, "soller", "Sóller", "Valle fértil de naranjos entre montañas. Plaza con modernismo catalán y ambiente de pueblo de montaña.") +
        spot(1, D1, "port_soller", "Port de Sóller", "Bahía protegida con barcos de pesca y terrazas. El agua aquí es más tranquila que en las calas abiertas."),
        "https://www.google.com/maps/dir/Palma+de+Mallorca,+Spain/Palma+Cathedral,+Mallorca/S%C3%B3ller,+Mallorca/Port+de+S%C3%B3ller,+Mallorca",
        ["Palma de Mallorca, Spain", "Palma Cathedral, Mallorca", "Sóller, Mallorca", "Port de Sóller, Mallorca"],
        "map-day1",
    )
    d += day_block(
        2, "Tramuntana oeste", "Valldemossa, Deià & Banyalbufar",
        "65", "1 h 45", "4/5",
        "Sóller <span class=\"arrow\">→</span> Valldemossa <span class=\"arrow\">→</span> Deià <span class=\"arrow\">→</span> Cala Deià <span class=\"arrow\">→</span> Banyalbufar",
        "El día más bucólico: la cartuja donde Chopin compuso, Deià colgando sobre el Mediterráneo y los bancales de Banyalbufar que caen en cascada hacia el mar. Carreteras sinuosas — conduce despacio y disfruta cada curva.",
        gallery(2, *D2),
        "<li>Real Cartuja de Valldemossa</li><li>Pueblo de Deià — cafés con vistas</li><li>Descenso a Cala Deià (piedra y snorkel)</li><li>Atardecer en Banyalbufar</li>",
        "<li>9:00 Valldemossa</li><li>11:30 Deià</li><li>13:00 Cala Deià</li><li>16:00 Banyalbufar</li><li>18:00 Mirador del acantilado</li>",
        spot(2, D2, "valldemossa", "Valldemossa", "Pueblo de piedra seca en la montaña. La cartuja donde Chopin pasó un invierno — olor a cera y jardines viejos.") +
        spot(2, D2, "deia", "Deià", "El pueblo de los artistas: casas de piedra en terrazas, bougainvilleas y el mar abajo. Robert Graves vivió aquí.") +
        spot(2, D2, "cala_deia", "Cala Deià", "Cala de piedra pequeña y auténtica — no es arena fina, es roca y agua clara. Snorkel excelente.") +
        spot(2, D2, "banyalbufar", "Banyalbufar", "Bancales de cultivo al borde del acantilado. Uno de los paisajes más dramáticos de la Tramuntana."),
        "https://www.google.com/maps/dir/S%C3%B3ller,+Mallorca/Valldemossa,+Mallorca/Dei%C3%A0,+Mallorca/Banyalbufar,+Mallorca",
        ["Sóller, Mallorca", "Valldemossa, Mallorca", "Deià, Mallorca", "Banyalbufar, Mallorca"],
        "map-day2",
    )
    d += day_block(
        3, "Norte", "Pollença & Cap de Formentor",
        "90", "2 h", "3/5",
        "Pollença <span class=\"arrow\">→</span> Port de Pollença <span class=\"arrow\">→</span> Formentor <span class=\"arrow\">→</span> Cala San Vicenç",
        "El día más espectacular en paisaje: la carretera a Formentor es una de las más bonitas del Mediterráneo — curvas sobre acantilados, pinos que se inclinan hacia el mar y miradores que quitan el aliento. Llega temprano a Formentor o compartirás el mirador con autobuses.",
        gallery(3, *D3),
        "<li>Subida de los 365 escalones del Calvari (Pollença)</li><li>Carretera a Cap de Formentor</li><li>Mirador Es Colomer</li><li>Tarde tranquila en Cala San Vicenç</li>",
        "<li>8:30 Pollença — Calvari</li><li>10:00 Port de Pollença</li><li>11:00 Formentor (antes de multitudes)</li><li>15:00 Cala San Vicenç</li>",
        spot(3, D3, "pollenca", "Pollença", "Plaza mayor con olivos centenarios, calle Calvari empinada y ambiente de pueblo real — no solo turístico.") +
        spot(3, D3, "formentor", "Cap de Formentor", "Acantilados de 200 m, faro solitario y agua azul profunda. La carretera es parte del espectáculo.") +
        spot(3, D3, "port_pollenca", "Port de Pollença", "Bahía amplia con paseo marítimo, ideal para desayuno antes de subir a Formentor.") +
        spot(3, D3, "cala_san_vicente", "Cala San Vicenç", "Cala tranquila entre rocas — menos famosa que Formentor pero más íntima. Buen snorkel."),
        "https://www.google.com/maps/dir/Pollen%C3%A7a,+Mallorca/Cap+de+Formentor,+Mallorca/Port+de+Pollen%C3%A7a,+Mallorca",
        ["Pollença, Mallorca", "Cap de Formentor, Mallorca", "Port de Pollença, Mallorca", "Cala San Vicente, Pollença"],
        "map-day3",
    )
    d += day_block(
        4, "Noreste", "Alcúdia, Artà & Cala Mesquida",
        "70", "1 h 30", "4/5",
        "Alcúdia <span class=\"arrow\">→</span> Platja de Muro <span class=\"arrow\">→</span> Artà <span class=\"arrow\">→</span> Cala Mesquida",
        "Contraste entre historia y playa: las murallas romanas de Alcúdia, la arena infinita de Muro y la cala virgen de Mesquida con vistas a una isla rocosa. Artà es el pueblo con más alma del noreste — mercado semanal los martes.",
        gallery(4, *D4),
        "<li>Murallas y casco antiguo de Alcúdia</li><li>Playa de Muro (7 km de arena)</li><li>Artà — iglesia y pueblo</li><li>Cala Mesquida al atardecer</li>",
        "<li>9:00 Alcúdia — murallas</li><li>11:00 Platja de Muro</li><li>14:00 Artà</li><li>17:00 Cala Mesquida</li>",
        spot(4, D4, "alcudia", "Alcúdia", "Murallas medievales intactas, calles empedradas y restos romanos. Mercado dominical por la mañana.") +
        spot(4, D4, "playa_muro", "Playa de Muro", "Siete kilómetros de arena blanca fina y agua poco profunda — ideal para familias y baño largo.") +
        spot(4, D4, "arta", "Artà", "Pueblo de piedra dorada bajo la sierra de Artà. Catedral fortificada y calles sin prisas.") +
        spot(4, D4, "cala_mesquida", "Cala Mesquida", "Playa virgen con isla rocosa en el centro. Menos masificada que las calas del sur en junio."),
        "https://www.google.com/maps/dir/Alc%C3%BAdia,+Mallorca/Platja+de+Muro,+Mallorca/Art%C3%A0,+Mallorca/Cala+Mesquida,+Mallorca",
        ["Alcúdia, Mallorca", "Platja de Muro, Mallorca", "Artà, Mallorca", "Cala Mesquida, Mallorca"],
        "map-day4",
    )
    d += day_block(
        5, "Sureste", "Mondragó, Santanyí & Cala d'Or",
        "85", "1 h 45", "4/5",
        "Palma <span class=\"arrow\">→</span> Cala Mondragó <span class=\"arrow\">→</span> Santanyí <span class=\"arrow\">→</span> Cala d'Or <span class=\"arrow\">→</span> Porto Cristo",
        "El sureste combina naturaleza protegida y calas en herradura: Mondragó es parque natural con dos calas unidas por pinos, Santanyí es pueblo de artistas con piedra dorada, y Cala d'Or tiene aguas turquesas en forma de U.",
        gallery(5, *D5),
        "<li>Parque natural de Mondragó — senderismo y calas</li><li>Mercado de Santanyí (miércoles y sábados)</li><li>Calas de Cala d'Or en kayak o a pie</li><li>Porto Cristo — Cuevas del Drach (opcional)</li>",
        "<li>8:30 Cala Mondragó</li><li>12:00 Santanyí</li><li>15:00 Cala d'Or</li><li>18:00 Porto Cristo</li>",
        spot(5, D5, "cala_mondrago", "Cala Mondragó", "Parque natural con dos calas de arena y pinos hasta el agua. Agua turquesa y senderos sombreados.") +
        spot(5, D5, "santanyi", "Santanyí", "Pueblo de piedra dorada con galerías de arte y plazas con sombra. Olor a pan recién hecho por la mañana.") +
        spot(5, D5, "cala_dor", "Cala d'Or", "Varias calas pequeñas en forma de herradura — Cala Ferrera, Cala Egos. Agua tranquila y fondo arenoso.") +
        spot(5, D5, "porto_cristo", "Porto Cristo", "Puerto pesquero con cuevas del Drach (lago subterráneo). Menos encantador que Santanyí pero interesante."),
        "https://www.google.com/maps/dir/Cala+Mondrag%C3%B3,+Mallorca/Santany%C3%AD,+Mallorca/Cala+d%27Or,+Mallorca/Porto+Cristo,+Mallorca",
        ["Cala Mondragó, Mallorca", "Santanyí, Mallorca", "Cala d'Or, Mallorca", "Porto Cristo, Mallorca"],
        "map-day5",
    )
    d += day_block(
        6, "Sur virgen", "Es Trenc & Ses Salines",
        "95", "1 h 45", "5/5",
        "Campos <span class=\"arrow\">→</span> Es Trenc <span class=\"arrow\">→</span> Ses Salines <span class=\"arrow\">→</span> Colònia de Sant Jordi <span class=\"arrow\">→</span> Capdepera",
        "El gran final playero: Es Trenc es la última playa virgen grande de Mallorca — arena blanca, dunas y agua transparente sin hoteles en la orilla. Ses Salines es parque natural con flamencos en las salinas. Despedida perfecta.",
        gallery(6, *D6),
        "<li>Es Trenc al amanecer (aparcamiento limitado)</li><li>Paseo por las salinas de Ses Salines</li><li>Comida en Colònia de Sant Jordi</li><li>Castillo de Capdepera — vistas a Menorca</li>",
        "<li>7:30 Es Trenc (llegar pronto)</li><li>11:00 Ses Salines</li><li>14:00 Colònia de Sant Jordi</li><li>17:00 Capdepera</li>",
        spot(6, D6, "es_trenc", "Es Trenc", "La playa más salvaje de Mallorca: 3 km de arena fina, dunas y agua caribeña. Sin edificios a la vista — protegida.") +
        spot(6, D6, "ses_salines", "Ses Salines", "Parque natural con salinas rosadas, flamencos en primavera y playas abiertas al viento.") +
        spot(6, D6, "sant_jordi", "Colònia de Sant Jordi", "Pueblo marinero auténtico — no resort. Pescado del día en restaurantes sin pretensiones.") +
        spot(6, D6, "capdepera", "Capdepera", "Castillo medieval con vistas a Menorca en días claros. Pueblo tranquilo para cerrar el viaje."),
        "https://www.google.com/maps/dir/Es+Trenc,+Mallorca/Ses+Salines,+Mallorca/Col%C3%B2nia+de+Sant+Jordi,+Mallorca/Capdepera,+Mallorca",
        ["Es Trenc, Mallorca", "Ses Salines, Mallorca", "Colònia de Sant Jordi, Mallorca", "Capdepera, Mallorca"],
        "map-day6",
    )
    return d
