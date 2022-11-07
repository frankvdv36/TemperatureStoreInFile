# MeetDisplayStoreData + PlotData

MeetDisplayStoreData.py

Meet temperaturen met 3 sensoren DS18B20 en zet data in file op SD. 

Laat live de temperaturen zien in de vorm van wijzers samen met datum en tijd in 'dashboard'.

## Beschrijving
Dit project heeft een toepassing om bij een CV-installatie de relatie na te gaan van de temperatuur HEEN en TERUG in functie van de BUITEN temperatuur. Het verschil van de eerste twee heeft aan hoeveel de temperatuur gezakt is na het doorlopen van de kring en zegt iets over de gevraagde warmte.

## Bronnen
De bronnen worden weer gegeven in het programma 'MeetDisplayStoreData.py' en 'Plotdata.py'

## Hardware
Voor dit project zijn dus 3 sensoren nodig.
- meet temperatuur aan de ketel op de buis HEEN
- meet temperatuur aan de ketel op de buis TERUG
- meet buitentemperatuur

Een module Raspberry Pi 'Zero W2' die werkt op afstand met VNC  

Deze 3 temperaturen worden samen met datum en tijd opgeslagen in een file op de SD-kaart.

Formaat 'Datum, Tijd, DatumTijd epoch, Temperatuur Hoog, Temperatuur Laag, Temperatuur Buiten, Temperatuur H-L (verschil)'

Iedere dag wordt een andere file gestart. De naam van de file is 'datum.txt' voorbeeld 221102.txt 

Met het tweede programma 'PlotData.py' kan alles zichtbaar gemaakt worden in een grafiek met 4 waarden op de Y-as.

## Software
MeetDisplayStoreData.py

Dit programma wordt geschreven in Python3 en bestaat uit drie delen die na elkaar doorlopen worden.
 - Lees de sensoren uit. 3x SD18B20. Rood voor HEEN, blauw voor TERUG en geel voor BUITENtemperatuur.
    Er wordt gebruik gemaakt van ingebouwde 1 wire software in de OS.
    Via internet wordt datum en lokale tijd gevonden als ook de teller die tijd en datum bevat in een getal sinds epoch, 1/1/1970
    Indien er een sensor uit valt wordt dit met 'TRY' 'EXCEPT' onderschept en zijn de temperaturen 3x 0°C  
 - Display gegevens op scherm. Hiervoor wordt Pygame gebruikt zoals in vorige projecten.
    Er worden 4 wijzers afgebeeld. Linksboven Temperatuur HEEN, rechtsboven Temperatuur TERUG, linksonder Temperatuur BUITEN, 
    rechtsonder verschil temperatuur heen-terug. Samen met datum en tijd die in het midden staat wordt dit scherm iedere 15 seconden ge-up-dated.
 - Schrijf gegevens weg op SD-kaart
    Het volgende protcol wordt gebruikt. DATUM, TIJD, EPOCH-tijd, TEMP HEEN(Hoog), TEMP TERUG(Laag), Temp Buiten, Verschil H-L
    Dit wordt weg geschreven in file 'datum.txt'. Dit gebeurt iedere 5 minuten. Iedere dag is er dus een andere file.
    Formaat: Datum: YYMMDD, Tijd: HHMMSS, 1667487590 aantal seconden sedert 1/1/70, 4x Temperaturen: XX,X

PlotData.py

Dit programma maakt gebruik van de data die aangemaakt wordt door het vorige programma. Met 'matplotlib' kan eenvoudig mooie grafieken aangemaakt worden.
Eerste bewerking maakt van iedere lijn in file 'datum.txt' die een 'list' is een 2Darray met 'numpy'
Dan worden de gegevens af gezonderd in een 1Darray met Datum, Tijd, DatumTijd, TempH, TempL, TempB, TempH-L.
De laatste 4 worden gebruikt voor de y-as. De x-as zijn de aantal metingen voor die dag. 24 uur x 12 metingen per uur (288).
Bij het opstarten vraagt het programma de naam van de file die u wilt bekijken. Dit wordt ingegeven 'YYMMDD' zonder '.txt'
Na het plotten stopt het programma. Indien het bestand niet bestaat stop het programma ook met de melding 'opnieuw proberen'.

Praktisch loopt het eerste programma op GEANY, het tweede kan dan lopen op Thonny en zal het eerste programma niet hinderen.




## Eigen scripts en programma's
