#  Spritpreiseanalyse


## Einstellungen (config.json)

Die für die Analyse benötigten Daten werden von tankerkoenig.de geladen.
Hierfür benötigen Sie einen API-Key von http://tankerkoenig.de.

Bitte rufen Sie die Hompage von tankerkoening.de auf und registrieren sich, um einen eigenen API-Key zu beantragen. Zur zeit (Stand 01.03.2021) ist der
Key kostenlos erhältlich.

Tragen Sie mit einem Editor (Notepad, Notepad++, nano, edit, usw.) ihren Key in die Datei config.json ein. 

{
"key":"00000000-0000-0000-0000-000000000002",   <- ihren Key eintragen
"rad":12,                                       <- den Suchradius in km eintragen
"lat":52.430002066507384,                       <- Latitude (Breitengrad) ihres Standortes eintragen
"lng":8.608646825325337,                        <- Longitude (Längengrad) ihres Standortes eintragen
"interval": 3600                                <- den Intervall in Sekunden eintragen, sollte nicht unter 3600 Sekunden (= 1 Stunden) sein.
"sorte":"e5"                                    <- die Spritsorte (diesel, e5, e10) eintragen
"verbrauch":7.5                                 <- den Durchschnittsverbrauch pro 100 km in Liter ihres Fahrzeugs eintragen
"fahrzeug":"SEAT Leon ST FR 1.8 TSI"            <- Hersteller und Modellbezeichnung eintragen
"kennzeichen":"XXX-XX 1234"                     <- Kfz-Kennzeichen ihres Fahrzeugs
}

