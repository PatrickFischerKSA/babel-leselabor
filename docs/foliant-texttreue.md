# Foliants Textgrundlage

Das Repertoire ist offen. Jede Unterhaltung untersucht einen begrenzten Ausschnitt, nicht das vermeintliche Erinnerungswissen des Modells über einen Titel.

## Was technisch geprüft wird

Die Passage wird in T1, T2 usw. gegliedert. Das Modell liefert ein festes Antwortformat und kann als Beleg nur einen vollständigen vorhandenen Textabschnitt auswählen (JSON-Schema mit konkreten zulässigen Zitaten). Vor der Anzeige prüft der Browser Textkennung und zusammenhängendes wörtliches Zitat (nur Unicode-/Leerraumnormalisierung). Ein fehlender Beleg, falsche Kennung, zusätzliche Antwortfelder, erfundene Ortsangaben oder nicht auffindbare zusätzliche Zitate halten die gesamte Antwort zurück. Die ungeprüfte Ausgabe wird nicht gestreamt oder im Gesprächskontext gespeichert. Auch abgebrochene Teilantworten werden verworfen.

Ein passendes Zitat beweist KEINE richtige Interpretation und nicht einmal die Relevanz des Belegs. Die Oberfläche bezeichnet nur den Wortlaut als gefunden. Jede freie Schlussfolgerung erscheint als inhaltlich nicht automatisch geprüfter Deutungsvorschlag; der Ausschnitt kann die Frage offenlassen. Keine zweite KI-Prüfung und keine Wahrheitsgarantie.

## Hinterlegte Ausgangspunkte

assets/foliant-grounding.json enthält 30 Auswahlpunkte: drei Freiwald-Passagen, eine Borges-Passage, eine eindeutig lesbare Eingangsstelle der fehlerhaften Amlinger-Transkription und 25 Essay-Einträge. 24 Essay-Einträge enthalten einen gelesenen Einstieg mit eng begrenzter Paraphrase. Mahlers Comic enthält bewusst KEINEN aus erfundener Textextraktion gewonnenen Ausgangspunkt: Original öffnen und eine Bildfolge beschreiben. Die Auswahl ist keine Volltextanalyse der Essays.

Die Fundstellen nennen PDF-Seiten, keine ungesicherten Druckseiten. Bei Einstiegen über eine Seitengrenze steht „ab PDF-Seite“. PDF-Ligaturen und Leerraum wurden normalisiert; verbliebene Extraktionsfehler müssen am Original geprüft werden. Bei Amlinger ist der Transkriptionsfehler „lesern“ ausdrücklich erhalten und ausgewiesen; weitergehende Thesen benötigen Audioabgleich. Änderungen am Ausschnitt deaktivieren die hinterlegte Ausgangsaussage.

Neue Ausgangspunkte: Original lesen, möglichst kurzen relevanten Ausschnitt übernehmen, Paraphrase ausschließlich daraus formulieren, Fundstelle und Einschränkungen angeben. Kein Rückschluss vom Einstieg auf das Gesamtwerk. Eigene und fremdsprachige Texte bleiben jederzeit möglich.

## Prüfungen

node tests/foliant-evidence.cjs
node tests/foliant-salon.cjs

tools/foliant-eval/evidence.html ist ein manueller lokaler Modelltest: acht Fälle, Kafka mit einem zusätzlichen Widerspruch; Temperatur 0,1, höchstens 650 Tokens, WebLLM-JSON-Schema. Nur bestandene Antwortformate gelangen in die nächste Runde. Ergebnisse müssen zusätzlich inhaltlich gelesen werden. Tools und Forschung werden nicht auf GitHub Pages ausgeliefert.

## PDF- und Word-Import

Die Sprechstunde liest PDF mit Textschicht sowie .docx lokal in einem kurzlebigen Web Worker aus. PDF.js 6.4.299 und Mammoth 1.13.0 liegen inklusive Lizenzen unter assets/vendor. Es gibt keinen Upload-Endpunkt. Dateiinhalt gelangt weder in eine Suchabfrage noch zu einem KI-Server. Nur der ausdrücklich übernommene Ausschnitt wird zur Gesprächsgrundlage; er unterliegt demselben Belegabgleich wie eingefügter Text.

Grenzen: 25 MB, höchstens 500 PDF-Seiten und eine Million extrahierte Zeichen. Vorschau vor Übernahme; PDF-Seite wählen oder Stelle markieren. Über 4.500 Zeichen wird die Übernahme abgelehnt, niemals still gekürzt. Word erhält keine erfundene Seitenzählung. Bildscans benötigen vorgängige OCR, altes .doc eine Speicherung als .docx. Spalten, Tabellen, Fußnoten und Zeichenerkennung müssen am Original geprüft werden. Abbrechen/Schließen beendet den Parser-Worker. Kein HTML aus dem Word-Dokument wird gerendert (nur extractRawText).

Browserprüfung: zweiseitige PDF ausgelesen, zweite Seite übernommen; DOCX mit zwei Absätzen ausgelesen, gezielt markierten Satz übernommen; Bild-PDF ohne Textschicht zeigt OCR-Hinweis. Tests: node tests/foliant-import.cjs.
