# ObreCarpetaID
- Versió 3 (2023): com a CLI.
- Versió 4 (2026): amb GUI, i opcionalment com a executable a Windows.
Escrit i executat amb Python, per a Windows. Caldrien algunes adaptacions per altres entorns, especialment pel que fa a la lectura i construcció de rutes de fitxer.

_ObreCarpetaID_ és un gadget per obrir carpetes a l'últim nivell d'un arbre de directoris, sense haver de navegar per l'arbre de directoris sinó tan sols introduint el nom de la carpeta.
És útil si els noms de les carpetes de tots els nivells en l'arbre de directoris segueixen un patró sistemàtic que permeti reconstruir la ruta a partir del nom (ID) de la carpeta objectiu.
_ObreCarpetaID_ no fa una cerca de l'ID en l'arbre de directoris, sinó que construeix la seva ruta. Si la ruta sencera no existeix, prova el nivell superior; si aquest no existeix, comprova que la unitat de disc existeixi o sigui accessible. En cada cas, informa l'usuari mitjançant un breu text.

Es tracta d'una utilitat per a una necessitat molt específica, però pot servir per a inspirar solucions a casos anàlegs.

## Cas que inspira i aplica ObreCarpetaID
En el cas implementat a _ObreCarpetaID_ es tracta de carpetes anomenades amb nombres (ID) a partir de 1, i que es van incrementant, arribant al 36220 en el moment de la implementació.
Aquestes carpetes ID estan agrupades en carpetes de nivell superior anomenades "Del x-y", cobrint cadascuna un rang de 100 ID.
"x" és un múltiple de 100, més 1.
"y" és x + 99 (i, per tant, un múltiple de 100).

## Excepcions que el codi ha de contemplar (en el cas descrit)
- La primera carpeta d'agrupament (la que hauria de contenir la ID=1), és "Del 1-2100"(enlloc, com hauríem esperat, de "Del 1-100").
- Manquen els ID entre 9601 i 19000, i no hi ha carpetes d'agrupament per a aquest rang d'ID: l'arbre de directoris salta de "Del 9501-9600" a "De 19001-19100".
- En cada carpeta d'agrupament hi poden mancar molts ID, és a dir que no formen una sèrie contínua ni molt menys.
- En l'arbre de directoris hi poden existir _artefactes_ a causa d'un ús poc curós: carpetes o fitxers que no hi haurien de ser. Seran ignorats pel codi, excepte la possibilitat de fitxers anomenats amb un ID i sense extensió: el codi els detecta i els presenta a l'usuari, tot informant-lo que no es tracta d'una carpeta.

Es facilita (en un .ZIP) un arbre de carpetes per experimentar, que mostreja el cas descrit amb un petit nombre de carpetes. Cal posar el contingut (carpeta global "Candidats") a l'arrel del disc C (si voleu utilitzar una altra unitat o un altre nom per a la carpeta global, tan sols cal adaptar el codi).

Carpetes per experimentar _ObreCarpetaID_ (dins de C:\Candidats):
- carpeta: Del 1-2100
    -- subcarpetes ID: 7, 8, 9, 14, 15, 1978, 2076
- carpeta: Del 2101-2200
    -- subcarpetes ID: 2101, 2131, 2191
- carpeta: Del 2201-2300
    -- subcarpetes ID: 2201, 2274, 2300
- carpeta: Del 20001-20100
    -- subcarpetes ID: 20001, 20085, 20099

Per experimentar les diferents respostes, proveu directament aquests casos d'ID:
- Qualsevol de les carpetes llistades a sobre.
- Valors entre 2301 i 20001, o superior a 20100.
- Valors no existents, dins de les carpetes existents (com ara 1, 2, 2102, 2202 o 20002).

Provar, també:
- Ciclar amb tecla TAB a la interfície.
- Esborrar l'entrada prèvia entre proves, i prémer TAB.
- Validar entrada amb <return> (a) directament al camp d'entrada i (b) activant el botó amb TAB.

# Contacte
Josep Maria Canals Garriga <nalska@mac.com>