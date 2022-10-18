# TemperatureStoreInFile
Meet temperaturen met 3x DS18B20 en store in file op SD. Laat live de temperaturen zien in de vorm van wijzers samen met datum en tijd.

## Beschrijving
Dit project heeft een toepassing om bij een CV installatie de relatie na te gaan hoe de temperatuur HEEN en TERUG in functie van de buiten temperatuur.

## Bronnen

## Hardware
Voor dit project zijn dus 3 sensoren nodig.
- meet temperatuur aan de ketel op de buis HEEN
- meet temperatuur aan de ketel op de buis TERUG
- meet buitentemperatuur

Deze 3 temperaturen worden samen met datum en tijd opgeslagen in een file op de SD-kaart.
De file kan steeds opgeladen worden op een laptop en zichtbaar gemaakt in bijvoorbeeld een Exel-file.
Dit gebeurt afstand

## Software
Dit programma wordt geschreven in Python3
Bestaat uit drie delen die na elkaar doorlopen worden.
 - Lees de sendoren uit. 3x SD18B20. Rood voor HEEN, blauw voor TERUG en geel voor buitentemperatuur.
    Er wordt gebruik gemaakt van ingebouwde 1 wire software in de OS.
    Neem via internet wordt datum en lokale tijd gevonden als ook de teller die tijd en datum bevat in een getal sinds epoch, 1/1/1970
 - Display gegevens op scherm. Hiervoor wordt Pygame gebruikt zoals in vorige projecten.
    Er worden 4 wijzers afgebeeld. Linksboven Temperatuur HEEN, rechtsboven Temperatuur TERUG, linksonder Temperatuur Buiten, rechtsonder verschil temperatuur heen-         terug.   

## Eigen scripts en programma's
