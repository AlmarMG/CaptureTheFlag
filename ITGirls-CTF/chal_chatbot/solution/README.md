# Chatbot solution
De chatbot challenge is opgedeeld in vier delen.

## Deel 1
Hier moet je een hexadecimale code vinden. Deze code staat in de console overview dit is te openen met de `f12` knop. De code in de console overview is decimaal dit moet dus omgezet worden naar een hexadecimale code. 

De code die ingevoerd moet worden is `0xF56D`.

![](https://cdn.discordapp.com/attachments/755558865302585355/846046108153151508/Scherm1.jpg)

## Deel 2
In deel twee moet er gekeken worden naar een logs pagina hier staan veel directories maar na wat kijken kun je de `/shop/` directory vinden. 

Deze directory moet ingevult worden in het scherm als `/shop` of `/shop/`.

![](https://cdn.discordapp.com/attachments/755558865302585355/846046105275203625/deel_2.jpg)

## Deel 3
Deel drie bestaat uit veel verschillende onderdelen, hieronder wordt kort uitgelegd hoe elk deel behaald kan worden.

1. Als eerste moet je naar de `/gevoelig/lijst/` navigeren hier staan *bijna* alle belangrijke pagina op een rijtje.
2. Open `/shop/` en open de cached versie van de pagina `/shop/cache/` (Deze is te vinden in inspect element). Hier kun je het jaar en de maand van de verval datum van de creditcard vinden, jaar:`2026` en maand:`maart`.

![](https://cdn.discordapp.com/attachments/755558865302585355/846046098987417620/cached.jpg)

3. Open de `/gevoelig/logs/` klik op de refresh knop en decode vervolgens de session cookie. Hierin staat de kaarthouder naam `James C. Town`.

![](https://cdn.discordapp.com/attachments/755558865302585355/846046104767430666/Decode.jpg)

4. Bij de `/secret/` en `/secret/vault/` pagina's kun je zien dat een N mist bij de `/secret/` pagina. Klik op de *n* toets op je toetsenbord nu verschijnt de ccv code `503`. Dit is niet de enige manier je kunt deze ook vinden in de files via inspect element.

![](https://cdn.discordapp.com/attachments/755558865302585355/846046109314580550/secret.jpg)

5. Voor het laatste onderdeel moet je naar de `/unimportant/creditcard/` directory navigeren. Hier moet de foto van de kat worden gedownload. De foto moet geopend worden in een text editor zoals notepad, nu moet er naar beneden gescrolt worden waar het creditcardnummer staat `5956272601707993`.  

![](https://cdn.discordapp.com/attachments/755558865302585355/846046102595829791/Creditkat.jpg)

6. Nu moet alles ingevuld worden in de shop. Als alles goed gaat komt er een betalingscode tevoorschijn: `7654729`. Vul deze code in scherm 3 in om naar scherm 4 te navigeren.

## Deel 4
In deel vier krijg je de flag: `flag(9c58b7cb81515f3)`

![](https://cdn.discordapp.com/attachments/755558865302585355/846046106075791410/Flag.jpg)