# [1*] [20] - [Wireshark]

## Description
### Wat is het doel van deze challenge?
    Het doel van deze challenge is om de data die al voor de gebruiker klaar is gezet, te analyseren en daar de flag uit te halen.

### Hoe zijn de packets tot stand gekomen?
    Om te beginnen moet Scapy geïnstalleerd worden. In scapy kun je precies zetten wat er in je packet moet komen. Je start je Wireshark op en selecteert de interface van de WiFi. Als je packets zijn gemaakt kun je ze verstuden door middel van de command: send(naam van je packet). De packets worden verzonden naar de destination adres die zelf is geschreven in de packetinfo. 

    Vervolgens moet er een pythonbestand gemaakt worden die de packets automatisch verstuurd en dit niet meer handmatig getyped hoeft te worden.

## Deployment
De route staat verder in routes.py en de container in de docker-compose. Verder hoeft er niks extra worden opgestart.