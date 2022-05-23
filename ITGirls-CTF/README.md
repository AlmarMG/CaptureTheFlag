# ITGirls CTF

## ITGirls
De ITGirls CTF is gemaakt voor het PAD project door team IC104-B3. 

De CTF is gemaakt door: 

|        Naam       | Student nummer |           Email            |
|:-----------------:|:--------------:|:--------------------------:|
| Nordin el Assassi | 500855391      | <nordin.el.assassi@hva.nl> |
| Juriaan de Nijs   | 500843525      | <juriaan.de.nijs@hva.nl>   |
| Almar Gemmel      | 500855343      | <almar.gemmel@hva.nl>      |
| Stijn Luijkx      | 500844738      | <stijn.luijkx@hva.nl>      |
| Danny van't Veer  | 500853775      | <danny.van.t.veer@hva.nl>  |

De namen en emails zijn ook terug te vinden in de CTF zelf.

## Thema
Dit project staat in het teken van ![de OWASP Top 10](https://owasp.org/www-project-top-ten/2017/Top_10).
Wij hebben gekozen voor sensitive data exposure. 

Sensitive Data Exposure is geen directe aanval. De techniek achter deze aanval is om kwetsbaarheden in het systeem te benutten. Vaak is dit gericht op data die niet voor iedereen is bedoeld. Een aanval vindt meestal plaats op de plek waar veel data van links naar rechts wordt verzonden en waar data minder goed tot helemaal niet beveiligd is. Er wordt niet verwacht dat er nog iemand tussen deze overdracht zit. Voorbeelden zijn bij data-overdracht van een HTTP-verbinding of een data-overdracht in clear-tekst. Dit is nog erger, aangezien data in clear-tekst niet ontcijferd is en het hierdoor voor de aanvaller nog makkelijker is om de data te achterhalen. Een voorbeeld van Sensitive Data Exposure kan zijn: De man-in-the-middle-attack. Deze manier van data-onderschepping werkt als volgt: Er is tussen twee pratende mensen een derde persoon gekomen (de aanvaller). Hij onderschept de data die de twee communicerende met elkaar uitwisselen. De twee partijen zullen niet merken dat er data wordt onderschept.  

## Challenges

Challenges in een overzichtelijke tabel. 
Flags voor de challenges staan in de bijbehordende "/solution" files.

|  Challenge  | Sterren | Punten |  Port range |
|:-----------:|:-------:|:------:|:-----------:|
| Vlog        | 1       | 20     | 8000 - 8099 |
| Moeilijk    | 1       | 20     | 8100 - 8199 |
| Wireshark   | 1       | 20     | 8200 - 8299 |
| Encodedchat | 1       | 20     | 8300 - 8399 |
| Cookie      | 2       | 40     | 8400 - 8499 |
| Mail        | 2       | 40     | 8500 - 8599 |
| Socialmedia | 2       | 40     | 8600 - 8699 |
| Chatbot     | 3       | 80     | 8700 - 8799 |


## Local Deployment
Om de CTF te spelen of testen met Docker kun je de volgende stappen volgen. (In windows)

1. Clone de gitlab repository via `git@gitlab.fdmci.hva.nl:nijsjm/pad_ic104b3.git` of download het via `https://gitlab.fdmci.hva.nl/nijsjm/pad_ic104b3/`
2. Als Docker nog niet geinstalleerd is op jou machine, gebruik deze link <https://docs.docker.com/docker-for-windows/install/>
3. Voer de volgende command uit: `docker-compose build && docker-compose up -d site`
4. De CTF is te bereiken via <https://itgirls-ctf.localhost>
5. Voer de volgende command uit om de CTF te stoppen: `docker-compose down`


