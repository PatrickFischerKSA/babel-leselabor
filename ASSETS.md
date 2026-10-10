# Bildnachweise und Generierung

## assets/babel.jpg

Erzeugt am 09.10.2026 mit dem integrierten Imagegen-Werkzeug (kein CLI/API-Fallback). Ausgabe anschliessend als JPEG für die Website verpackt. Kein Originalkunstwerk oder Text von Borges wurde als Bildreferenz verwendet.

Prompt:

> Use case: illustration-story. Asset type: large cinematic background for an interactive German literary learning website. Borges Library of Babel inspired endless hexagonal library, monumental stacked hexagonal galleries, deep central abyss, spiralling stairs, innumerable old books, a tiny solitary reader carrying an amber lantern. Dark ink navy and aged gold palette, atmospheric dust, copperplate engraving crossed with rich painterly architectural concept art, dramatic depth, immersive mysterious literary mood. Landscape composition, no writing no letters no watermark. Save a local image file usable in the project.

## Linienbilder

Die Motive Bibliothek, Satzbruch, Uhr, Tür, Apparat, Netz, Bücher, Welle, Auge und Keim werden als eigene SVG-Grafiken von der Funktion `art()` in `app.js` gezeichnet. Die Raumkarte verwendet diese Motive. Die fünf Borges-Leseaufträge begleitet das separate Bildpanorama. Das Bücherbild im Bookishness-Raum ist eine eigene CSS-Gestaltung mit erfundenen Titeln. Das Hexagon-Logo liegt in `assets/mark.svg`.

## assets/borges-folge.jpg

Ein einziges Panorama mit fünf Szenen, erzeugt mit dem integrierten Imagegen-Werkzeug am 09.10.2026. Die Website zeigt die fünf Bereiche durch CSS-Bildausschnitte.

Prompt:

> Use case: illustration-story. Asset type: a single panoramic five-panel accordion illustration for a Borges Library of Babel literary website. Five equally wide vertical panels, arranged left to right, edge to edge, no gutters or text. Unified richly detailed antique etching and painterly chiaroscuro style in ink navy, muted teal, parchment gold, copper. Panel 1: solitary tiny librarian on a hexagonal gallery over a towering abyss, shelves extending into darkness. Panel 2: extreme close up of a mysterious open old book with tiny indistinct illegible marks, worn paper, lamp illuminating it. Panel 3: labyrinth of cascading catalogue cards and interconnected books, a searching human hand. Panel 4: shadowy robed librarians arguing around stacks of books, one trying to remove books while another protects them, dramatic tension. Panel 5: repeating hexagonal galleries becoming a cosmic spiral constellation, fragile amber light and a single small reader facing infinity. Landscape panoramic format, five panels of equal width. No readable lettering, no labels, no watermark. Original symbolic interpretation, not a reproduction of existing artwork.

## assets/bookwall.jpg

Erzeugt am 10.10.2026 mit dem integrierten Imagegen-Werkzeug, mit dem vom Nutzer angehängten Bücherwandfoto als visueller Referenz. Das Referenzfoto wird nicht im Repository veröffentlicht. Das generierte Bild dient als Material der 3D-Regalwände.

Prompt:

> Create a realistic straight-on architectural texture for a navigable 3D Borges Library of Babel, inspired by the attached reference photo of a densely filled wooden bookcase. This is a texture asset covering an entire monumental library bookcase wall, not an interface. Perfect frontal orthographic view, square composition, full-bleed, 5 vertical wooden bays and 9 horizontal shelves, completely densely filled with hundreds of individually varied antique leather and cloth books, subtle faded spine gold decorations, worn ochre, russet, olive, oxblood, navy and parchment colors. Warm aged walnut joinery and timber cornices, real grain and surface imperfections, dusty patina, faint warm neutral diffuse illumination for texture mapping. No perspective distortion, no doors, no floor, no people, no statues, no readable text, no icons, no labels, no UI. Rich photographic detail, tasteful old residential library feeling from reference enlarged into Borges hexagonal architecture. Entire image consists only of shelves of books and their walnut frame.

Holzboden und beschriftete Buchrücken entstehen als eigene Canvas-Materialien in `explorer.js`. Architektur, Regalbretter, Geländer, Treppen und Buchobjekte sind dort als 3D-Geometrie gebaut. Lederdecke und offene Papierseiten sind eigene CSS-Gestaltungen.

## assets/vendor/

Three.js 0.180.0, lokal gebündelte Module aus dem offiziellen npm-Paket `three`. MIT-Lizenz: `assets/vendor/THREE-LICENSE.txt`.
