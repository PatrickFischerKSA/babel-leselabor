# BABEL – Das Leselabor

Eine interaktive Lerneinheit zum Wandel der Lesekultur, ausgehend von Jorge Luis Borges’ **Die Bibliothek von Babel** und Bent Freiwalds **Die lesende Gesellschaft, um die wir trauern, hat es nie gegeben** (Krautreporter, 08.10.2026).

Erst erleben, dann am Text prüfen: elf frei zugängliche Räume über Textflut, Aufmerksamkeit, Untergangserzählungen, soziale Zugänge, Delegation, Algorithmen, Bookishness, Medien, Resonanz und die eigene zukünftige Lesekultur. Für die Sekundarstufe II, ab ungefähr 15 Jahren. Vorschlag für zwei Lektionen in der Website unter „Für den Unterricht“.

## Start

Statische Website ohne Build oder Bibliotheksinstallation. `index.html` direkt öffnen oder im Projektordner ausführen:

```sh
python3 -m http.server 8769
```

Dann `http://localhost:8769` öffnen. Für GitHub Pages dient das Repository-Wurzelverzeichnis als Website. Die enthaltene Actions-Workflowdatei publiziert bei Push nach `main`.

## Originallektüre und Quellen

[Materialsammlung in Craft](https://planes-sit-wl6.craft.me/Ooin1xv6tuY8AP).

Das Stimmenverzeichnis ordnet alle unterschiedlichen Werke der Sammlung einem Raum zu. Parallelfassungen und Audiofassungen werden gemeinsam eingeordnet. Die Primärtexte sind über die Sammlung zugänglich. Keine vollständigen geschützten Bücher oder Artikel werden in diesem Repository neu veröffentlicht. Bei Borges dienen fünf illustrierte Stationen als Lesetor und geben Aufträge für die Originallektüre. Eigene Ausschnitte lassen sich flüchtig in den Leseraum einfügen.

Wichtig: Der Autor heisst **Bent Freiwald**, nicht Bernt. Das Abruf-/Druckdatum älterer PDFs ist nicht ihr Erscheinungsdatum. Amlingers DOCX enthält Transkriptionsfehler; das Audio ist die bessere Kontrollquelle. Lauer-Interview und Pressman-Darstellung sind redaktionelle Sekundärfassungen. Die Atlantic-Übersetzung ist nicht autorisiert. Aussagen von 2023 über KI sind historisch einzuordnen.

## Didaktische Grenzen

Der Aufmerksamkeitsversuch ist keine Diagnostik und kein wissenschaftlicher Kausalnachweis. Die beiden Texte sind verschieden, die Reihenfolge wird variiert. Lesezeit ist kein Verständniswert. Alle Personen, Kurzfassungen, Budgetmodelle, algorithmischen Titel und literarischen Versuchstexte sind erfunden. Ein Perspektivwechsel beweist keine dauerhafte Empathiewirkung. Die Moralstudie wird als Analogie thematisiert, nicht als empirischer Beweis über Lesekultur.

Beurteilt werden können: nachvollziehbare Beobachtung, präziser Textbezug, faire Gegenposition, konkreter Transfer. Kein Punktesystem bewertet Lesegeschwindigkeit oder Buchbesitz.

## Datenschutz und Zugänglichkeit

Keine Anmeldung, kein Backend, keine Analytics. Logbuch und Fortschritt bleiben in `localStorage` dieses Browsers und können als Text exportiert bzw. gedruckt werden. Die lokale Löschung benötigt zwei Klicks. Eingegebene Originalausschnitte werden nicht gespeichert oder übertragen. Optionale Sprachausgabe verwendet die Browserfunktion; verfügbare Stimmen und deren Verarbeitung hängen vom Browser ab. Google Fonts ist ein externer Abruf; Fallback-Schriften sind vorhanden. Notizen überleben einen Geräte- oder Browserwechsel nur durch Export.

Alle Räume sind ohne Zeitsperre zugänglich. Ruhemodus, freiwillige Unterbrechungen, `prefers-reduced-motion`, Tastaturbedienung, sichtbare Fokusmarkierungen, Formularlabels und responsive Layouts sind vorhanden. Für bestimmte Lernende sind begleitendes Vorlesen oder eine Papierfassung der Originale hilfreich.

## Bilder

`assets/babel.jpg` und `assets/borges-folge.jpg`: mit dem integrierten Imagegen-Werkzeug generierte Bibliotheksillustration und fünfteilige Bildfolge. Prompt und Herkunft in [ASSETS.md](ASSETS.md). Linienillustrationen und Buchobjekte: eigene SVG-/CSS-Gestaltungen in `app.js` und `style.css`; keine übernommenen Borges-Illustrationen. Forschungsdateien sind bewusst durch `.gitignore` von der Veröffentlichung ausgeschlossen.

## Noch festzulegen

Konkrete Klasse, verfügbare Lesezeit, Leistungsnachweis und Zugangs-/Nutzungsrechte an den Originalen. Diese Ausgabe setzt freie Exploration und ein persönliches Logbuch voraus.

## Prüfung dieser Version

JavaScript-Syntaxprüfung mit `node --check app.js`. Im Browser wurden alle elf Räume geöffnet und ihre zentralen Interaktionen ausgeführt: Regalsuche, sechs Gerichtsakten, beide Aufmerksamkeitsdurchgänge, vier historische Klagen, Ressourcenverteilung, fehlerhafte Kurzfassung mit Originalprüfung, Empfehlungsregal, Bücherinszenierung, Medienwechsel, Perspektivwechsel und Zeitbudget. Logbuch-Speichern, Fortbestand nach Neuladen und zweistufiges Löschen wurden geprüft. Die mobile Borges-Ansicht zeigte keinen horizontalen Überlauf. Die Stichproben erzeugten keine JavaScript-Fehler im Browserprotokoll. Dies ist keine vollständige Screenreader-Prüfung.
