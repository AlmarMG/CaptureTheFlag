# Mainsite

## Challenges
Wat is het doel van de challenges pagina?

Het doel van de challenges pagina is dat wij een centrale pagina wilden maken waar je duidelijk kon zien welke challenges er allemaal zijn. Wat je nog meer kan doen op deze pagina is zien hoeveel sterren elke challenge is, deze sterren houden in wat de moeilijkheidsgraad is van een challenge. Wat je ook kan zien is wat de naam van de challenge is, zodat je al een beetje een idee krijgt van wat je moet doen bij de challenge. Wat je ook kan zien is of de challenge voltooid is of niet ten slotte kan je vanaf deze pagina ook zien is de knop naar de verschillende hint pagina’s voor elke challenge.

Hoe is de challenges pagina tot stand gekomen?

Eerst is de front end pagina gemaakt, dit hebben wij zo gemaakt dat er al knoppen zijn die kunnen doorverbinden naar eventuele challenges pagina’s, wij hadden hierover nagedacht en zijn erop uitgekomen dat wij dit het beste konden doen door gebruik te maken van een table waarin dan de informatie wordt gezet. Uiteindelijk hebben wij alle data in de tabel die gehardcode was vervangen door informatie die uit de database wordt opgehaald, dit hebben wij gedaan in combinatie met docker en flask

## Login
Wat is het doel van de login pagina?

Het doel van de login pagina is dat wij niet wilden dat zomaar iedereen op onze ctf terecht kon en dat als wij score en gebruikte hints wilden bijhouden iemand dan ook een account moest hebben om dat te kunnen opslaan. Zo zijn wij tot de conclusie gekomen dat de beste oplossing was om een login pagina te maken. Op deze pagina kan je dus inloggen en er is ook een knop die je doorverbind naar de pagina waar je een account kan maken.

Hoe is de login pagina tot stand gekomen?

Eerst zijn wij begonnen met het maken van de front end pagina, dit hebben wij zo gemaakt dat wij deze konden gebruiken, maar wel verder konden gaan naar latere pagina’s. Dit hebben wij gedaan door de login knop tijdelijk te vervangen voor een knop die direct doorverbind naar de challenges pagina. Uiteindelijk hebben wij deze vervangen voor een knop die controleert of het account die is ingevuld bestaat, dit gaat in combinatie met de database in docker en flask.

## Account aanmaken
Wat is het doel van de account aanmaak pagina?

Het doel van de account aanmaak pagina is om de gebruikers een account aan te laten maken waarmee ze zichzelf kunnen identificeren. Het is hier belangrijk dat gebruikers niet bepaalde speciale tekens kunnen gebruiken of korte wachtwoorden kunnen gebruiken. Want dit is natuurlijk niet goed voor de veiligheid van de site of de gebruiker.

Hoe is de account aanmaak pagina tot stand gekomen?

Eerst zijn we begonnen met het maken van de front-end pagina van de aanmeld pagina, deze deed voorderest nog niet veel. Vervolgens hebben we gezorgd dat je in de invoervelden geen speciale tekens of korte wachtwoorden kan gebruiken. En uiteindelijk is deze pagina volledig verbonden met de database en worden de gemaakte accounts hier nu opgeslagen.


## Hints
Wat is het doel van de hints pagina?

Het doel van de hints pagina is om gebruikers hints te laten kopen ten koste van hun behaalde punten bij de challenges. Het kopen van hints gaat hierdoor ten koste van je positie op de ranglijst waardoor degene die de minste hints nodig heeft dus het hoogst zal eindigen. 

Hoe is de hints pagina tot stand gekomen?

Eerst moest de front-end gemaakt worden voor de hints pagina die de hints laat verschijnen als je op de knop klikte, dit hebben we gedaan met behulp van bootstrap. Vervolgens moesten er verschillende scripts en database tabellen aangemaakt worden. Deze scripts en database tabellen zorgen er samen voor dat bij het kopen van een hint de gebruiker punten verliest en de hint wordt toegevoegd aan het account en de gebruiker deze altijd terug kan zien.

## Flagchecker
Wat is het doel van FlagCheck?
    Het doel van de FlagCheck is zodat de gebruiker kan zien of hij/zij de flag die is gevonden juist is. Als de ingevoerde flag juist is, krijgt de gebruiker er een bepaald aantal punten toegewezen die vervolgens gebruikt kunnen worden om hints te 'kopen' voor wanneer de gebruiker vast zit bij een andere challenge. Als de flag onjuist is ingevoerd, krijgt de gebruiker een melding dat de flag onjuist is. De flag moet dan opnieuw worden gezocht.

Hoe is de FlagChecker tot stand gekomen?
    Het eerste prototype was puur gericht op de flags die in het pythonbestand zijn gezet. Dit was om te kijken hoe de checker zou reageren met een flash message.

    Voor de uiteindelijke FlagCheck is er een verbinding gemaakt met de database. Van te voren is voor elke challenge de benodigde informatie in de database gezet. Vervolgens worden er waardes uit de database gehaald en vergeleken met de flagwaarde die de gebruiker heeft ingevoerd. Wanneer de invoer van de gebruiker gelijk is aan de info die staat in de database, komt er een flashmessage tevoorschijn die verteld dat de flag correct is. Daarnaast wordt er ook verteld hoeveel punten er toegevoegd worden aan de gebruiker zijn/haar score. Deze score wordt ook opgehaald uit de info in de database bij de bijbehorende challenge. Hierna wordt er ook gelijk doorgegeven in de database dat de challenge is voltooid. Nu komt er op de homepage te staan dat de challenge is behaald. Zo weet de gebruiker welke challenge er al voltooid is.

    Wanneer de gebruiker een flag voor de tweede keer invoert, mogelijk om extra punten te bemachtigen, komt er een flashmessage tevoorschijn die verteld dat deze flag al is ingevuld en het niet mogelijk is om extra punten te bemachtigen. Er is namelijk al bij het eerste keer invoeren aangemerkt dat de challenge is voltooid en het dus niet meer mogelijk is om de flag opnieuw in te vullen.


## Ranglijst
Wat is het doel van de ranglijst?

Het doel van de ranglijst is zodat gebruikers kunnen zien hoe goed ze het doen vergeleken met andere gebruikers. Uiteindelijk is de #1 op deze lijst de winnaar van onze CTF.

Hoe is de ranglijst tot stand gekomen?

Eerst moest de front-end tot stand komen met behulp van bootstrap. Vervolgens moesten er scripts geschreven worden die de gebruikersnamen en hun behaalde punten uit de database haalde. Vervolgens moesten deze geordend worden van hoog naar laag.


## Over ons 
Wat is het doel van de over ons pagina?

Het doel van de over ons pagina is zodat mensen die op onze ctf komen kunnen zien door wie deze ctf is gemaakt en wat iedereens rol was. Wij hebben gekeken naar andere websites en hebben gezien dat het gebruikelijk is om een over ons pagina toe te voegen, daarom hebben wij ervoor gekozen om dit ook te doen.

Hoe is de over ons pagina tot stand gekomen?

Eerst zijn wij begonnen met het opzetten van de pagina, dat hebben wij gedaan door met de container-row-col structuur van bootstrap vakjes neer te zetten zodat wij daarin onze gegevens konden zetten, vervolgens hebben wij op de website van bootstrap gekeken naar mooie voorbeelden, daar konden wij goeie classes van gebruiken om het zo mooi mogelijk te maken.

