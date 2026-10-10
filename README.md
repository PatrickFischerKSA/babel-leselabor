# BABEL – Das Leselabor

Eine interaktive Lerneinheit zum Wandel der Lesekultur, ausgehend von Jorge Luis Borges’ **Die Bibliothek von Babel** und Bent Freiwalds **Die lesende Gesellschaft, um die wir trauern, hat es nie gegeben** (Krautreporter, 08.10.2026).

Erst erleben, dann am Text prüfen: elf frei zugängliche Räume über Textflut, Aufmerksamkeit, Untergangserzählungen, soziale Zugänge, Delegation, Algorithmen, Bookishness, Medien, Resonanz und die eigene zukünftige Lesekultur. Für die Sekundarstufe II, ab ungefähr 15 Jahren. Vorschlag für zwei Lektionen in der Website unter „Für den Unterricht“.

## Durch die Bibliothek wandeln

Die Startseite ist ein begehbares 3D-Interieur aus elf sechseckigen Galerien, hohen Bücherwänden, Holzstegen und einem zentralen Schacht mit Wendeltreppe. Maus oder Finger ziehen dreht den Blick; am Bildschirmrand dreht er sich mit dem Cursor weiter. Pfeile oder WASD und das Mausrad bewegen die Person. Die Bildschirmtasten funktionieren auch auf Touchgeräten. Durchgänge verbinden die Galerien; die Galerieauswahl erlaubt einen direkten Wechsel.

Beschriftete Bände stehen zwischen den Büchern. Beim Anklicken gleitet ein Band aus dem Regal und öffnet sich als Buch mit Lederdecke, Papierseiten und Buchfalz. Fragen, Versuche und Ressourcen erscheinen auf seinen Seiten. Alle 40 unterschiedlichen Quellen sind erreichbar. Escape oder das Lesezeichen „Buch zurückstellen“ schliesst das Buch und behält geschriebene Reflexionen lokal. Seiten lassen sich blättern oder scrollen. Beim Wechsel zum Logbuch und zurück bleibt der zuletzt besuchte Ort erhalten. Ruhemodus und reduzierte Bewegung unterbinden das automatische Drehen.

Three.js 0.180.0 ist lokal unter `assets/vendor/` gebündelt (MIT-Lizenz liegt bei). Ohne WebGL wird eine bebilderte Bücherwand mit bedienbaren Bänden angezeigt.

## Herr Foliant begleitet die Lesetour

Der schrullige, erfundene Bibliothekar erklärt jeden Raum in drei Schritten: erst einen Versuch machen, dann eine bezeichnete Stelle im Original lesen, schliesslich einen konkreten Gedanken festhalten. Er kann die passenden Bände öffnen und führt durch alle elf Galerien. Freies Wandeln bleibt möglich; seine Figur ist jederzeit ansprechbar und einklappbar.

Die Buchseiten enthalten nummerierte Handlungsanweisungen, einen direkten Weg zum Versuch bzw. Schreibfeld, optionale Sprachausgabe und ein Satzgerüst hinter „Ein Beispiel, bitte“. Beim Logbuchauftrag führen Hilfen zum fehlenden Versuch oder Text zurück. Die Tourposition und der nächste Schritt bleiben lokal gespeichert. Die Beispiele sind keine Musterlösungen. Foliant ist eine gestaltete Figur mit vorab geschriebenen Impulsen, kein KI-Chat.

## Start

Statische Website ohne Build oder Bibliotheksinstallation. Im Projektordner einen lokalen Webserver starten (die 3D-Module benötigen HTTP):

```sh
python3 -m http.server 8769
```

Dann `http://localhost:8769` öffnen. Für GitHub Pages dient das Repository-Wurzelverzeichnis als Website. Die enthaltene Actions-Workflowdatei publiziert bei Push nach `main`.

## Originallektüre und Quellen

[Materialsammlung in Craft](https://planes-sit-wl6.craft.me/Ooin1xv6tuY8AP).

Das Stimmenverzeichnis ordnet alle unterschiedlichen Werke der Sammlung einem Raum zu. Parallelfassungen und Audiofassungen werden gemeinsam eingeordnet. Die Primärtexte sind über die Sammlung zugänglich. Die 25 vom Nutzer bereitgestellten Einzelbeiträge aus „Warum Lesen“ liegen unverändert unter `assets/readings/`, mit individuellen Leseimpulsen und Autorenbänden in den passenden Galerien. Der pauschale Sammelband-Eintrag wurde ersetzt. Bei Borges dienen fünf illustrierte Stationen als Lesetor und geben Aufträge für die Originallektüre. Eigene Ausschnitte lassen sich flüchtig in den Leseraum einfügen.

Wichtig: Der Autor heisst **Bent Freiwald**, nicht Bernt. Das Abruf-/Druckdatum älterer PDFs ist nicht ihr Erscheinungsdatum. Amlingers DOCX enthält Transkriptionsfehler; das Audio ist die bessere Kontrollquelle. Lauer-Interview und Pressman-Darstellung sind redaktionelle Sekundärfassungen. Die Atlantic-Übersetzung ist nicht autorisiert. Aussagen von 2023 über KI sind historisch einzuordnen.

## Didaktische Grenzen

Der Aufmerksamkeitsversuch ist keine Diagnostik und kein wissenschaftlicher Kausalnachweis. Die beiden Texte sind verschieden, die Reihenfolge wird variiert. Lesezeit ist kein Verständniswert. Alle Personen, Kurzfassungen, Budgetmodelle, algorithmischen Titel und literarischen Versuchstexte sind erfunden. Ein Perspektivwechsel beweist keine dauerhafte Empathiewirkung. Die Moralstudie wird als Analogie thematisiert, nicht als empirischer Beweis über Lesekultur.

Beurteilt werden können: nachvollziehbare Beobachtung, präziser Textbezug, faire Gegenposition, konkreter Transfer. Kein Punktesystem bewertet Lesegeschwindigkeit oder Buchbesitz.

## Datenschutz und Zugänglichkeit

Keine Anmeldung, kein Backend, keine Analytics. Logbuch und Fortschritt bleiben in `localStorage` dieses Browsers und können als Text exportiert bzw. gedruckt werden. Die lokale Löschung benötigt zwei Klicks. Eingegebene Originalausschnitte werden nicht gespeichert oder übertragen. Optionale Sprachausgabe verwendet die Browserfunktion; verfügbare Stimmen und deren Verarbeitung hängen vom Browser ab. Google Fonts ist ein externer Abruf; Fallback-Schriften sind vorhanden. Notizen überleben einen Geräte- oder Browserwechsel nur durch Export.

Alle Räume sind ohne Zeitsperre zugänglich. Ruhemodus, freiwillige Unterbrechungen, `prefers-reduced-motion`, Tastaturbedienung, sichtbare Fokusmarkierungen, Formularlabels und responsive Layouts sind vorhanden. Für bestimmte Lernende sind begleitendes Vorlesen oder eine Papierfassung der Originale hilfreich.

## Bilder

`assets/bookwall.jpg`, `assets/babel.jpg` und `assets/borges-folge.jpg`: mit dem integrierten Imagegen-Werkzeug generierte Bibliotheksillustration und fünfteilige Bildfolge. Prompt und Herkunft in [ASSETS.md](ASSETS.md). Linienillustrationen und Buchobjekte: eigene SVG-/CSS-Gestaltungen in `app.js` und `style.css`; keine übernommenen Borges-Illustrationen. Forschungsdateien sind bewusst durch `.gitignore` von der Veröffentlichung ausgeschlossen.

## Noch festzulegen

Konkrete Klasse, verfügbare Lesezeit, Leistungsnachweis und Zugangs-/Nutzungsrechte an den Originalen. Diese Ausgabe setzt freie Exploration und ein persönliches Logbuch voraus.

## Prüfung dieser Version

JavaScript-Syntaxprüfung mit `node --check app.js`. Im Browser wurden alle elf Räume geöffnet und ihre zentralen Interaktionen ausgeführt: Regalsuche, sechs Gerichtsakten, beide Aufmerksamkeitsdurchgänge, vier historische Klagen, Ressourcenverteilung, fehlerhafte Kurzfassung mit Originalprüfung, Empfehlungsregal, Bücherinszenierung, Medienwechsel, Perspektivwechsel und Zeitbudget. Logbuch-Speichern, Fortbestand nach Neuladen und zweistufiges Löschen wurden geprüft. Die mobile Borges-Ansicht zeigte keinen horizontalen Überlauf. Die Stichproben erzeugten keine JavaScript-Fehler im Browserprotokoll. Dies ist keine vollständige Screenreader-Prüfung.

Die Foliant-Erweiterung wurde im Browser durch alle elf Räume mit ihren drei Buchphasen, Original-Links, Beispielhilfe, Rückwegen und Tourabschluss geprüft. Borges-Regalsuche und beide Aufmerksamkeitsdurchgänge funktionieren innerhalb der moderierten Bücher weiter.

Die 3D-Fassung wurde zusätzlich auf sichtbare Bücherwände, Galerieübergänge, das Herausziehen und Öffnen der Bände, Buchseiten und Ressourcen geprüft. Frühere direkte Raumlinks funktionieren weiter. `explorer.js`, Bilder und die lokal gebündelte 3D-Bibliothek werden vom GitHub-Pages-Workflow publiziert.

## Freie Bibliotheksflügel

Projekt Gutenberg: vollständiger Import des öffentlichen A–Z-Titelverzeichnisses vom 10.10.2026, 13.138 unterschiedliche Werklinks. Nur Titel, Autor und Original-Link werden gespeichert. `scripts/update-gutenberg.py` aktualisiert den Bestand. In den 3D-Galerien stehen zusätzliche Originalwerke; die Gutenberg-Regale öffnen den gesamten Bestand als durchsuchbare, blätterbare Bücherwände. Jeder Band öffnet den Originalvolltext, ohne Lernauftrag oder Fortschrittsänderung der Lesetour.

Google Books: durchsuchbarer Flügel mit paginierten Ergebnissen der offiziellen Volumes-API. Volltext, Teilvorschau und bibliografischer Eintrag werden unterschieden. Ein vollständig exportierbarer Google-Gesamtkatalog wird nicht angeboten. Bei API-Limits bleibt die direkte, mit der Anfrage vorbereitete Google-Buchsuche zugänglich. Es werden keine erfundenen Treffer und keine Volltextverfügbarkeit behauptet. Suchanfragen werden bei Nutzung dieses Flügels an Google übertragen.
