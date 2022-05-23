# Docker Guide

### Inleiding
Dit is een mini documentatie van benodigde commando's/handigheidjes die je kunt gebruiken tijdens dit project.
Als er iets op de terminal (lees: cmd) zal moeten worden uitegevoerd, zal dit worden aangegeven met een $.

##### Docker-compose
Een docker container kan op verschillende manieren worden aangemaakt, via een cli, of een docker-compose file. Docker-compose is een bestand waarin je meerdere containers kan declareren. Een docker container is een aparte instantie, of meestel een enkel besturingssyteem die i een eigen omgeving draait. We maken zeg maar een soort van virtuele machine. In de docker-compose vind je een aantal vaste elementen, die later zullen worden toegelicht. [Wiki](https://docs.docker.com/compose/)

```
version: '3'

services:
    site:
        container_name: main_site
        build: ./site/
        ports: 
            - "80:80" #http
            - "443:443" #https
```

Hierboven staat een docker-compose die je eventueel kan gebruiken voor een kleine site. Allereerst is er _version_, dit is de versie van docker-compose. In totaal bestaan er nu 3 volledige releases, dus 3 is de laatste versie. Elke versie worden er, net zoals met python of andere stukken software, functionaliteiten toegevoegd en verwijderd. Kijk dus allereerst naar de versie die een docker-compose  bestand heeft als je op zoek gaat naar oplosingen.

In een docker-compose kan van alles staan. Om maar een paar functionalitieten te noemen: Containers kunnen automatisch worden aangemaakt, ze kunnen met elkaar worden verbonden via netwerken. Gegevens kunnen op een speciale manier worden opgeslagen met behulp van volumes en mounts.

##### Uitvoeren
In de docker-compose kan je veel details kwijt over de container die je wilt aanmaken. Zo kun je met ports de poorten bepalen aan de host en docker kant. Ook is het mogelijk om gegevens van een database mee te geven. Een database kan al woren aangemaakt aan de hand van het compose bestand. Maar vrijwel de grootste functie is het builden van dockerfiles. Zo komt het automatisch uitvoeren tot zijn recht.

Om een docker-dompose uit te voeren, kan je de volgende commando's gebruiken.

`$ docker-compose up -d` Om de containers en images te starten
`$ docker-compose down` Om de containers te stoppen
Dit project gebruiken wij `docker-compose build && docker-compose up -d site`. Zo kunnen challenges later in aparte challenges worden gestart