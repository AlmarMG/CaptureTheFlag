# GPG Guide

### Inleiding
Dit is een mini documentatie van benodigde commando's/handigheidjes die je kunt gebruiken tijdens dit project.
Als er iets op de terminal (lees: cmd) zal moeten worden uitegevoerd, zal dit worden aangegeven met een $
In het begin staat een stappenplan, om vlug te refereren naar bepaalde stappen. Er wordt er van uit gegaan dat je git al hebt geconfigureerd.


###### Stappenplan
Installeer eerst de windows versie van gpg: [Website](https://gnupg.org/download/index.html)
    Met gpg kunnen we commit's verifiëren. Git registreert jou wel als gebruiker, maar voert nauwlijks verificatie uit. Met behulp van een pgp sleutel kan de identitiet wel worden nagetrokken.

Een gpg sleutel, moet net zoals een ssh sleutel worden gegenereerd. Dit kan eventueel in een texteditor met ingebouwde terminal, maar ook in cmd. 

`gpg --full-gen-key`

Vervolgens worden er een aantal vragen gesteld, je kunt de sleutel zelf aanpassen. De 1e vraag gaat over welke soort encryptie de sleutel wordt versleuteld. Kies hierbij de 1e optie, of klik meteen op enter.

De sleutel kan een bepaalde grootte in bits hebben, hoe groter de sleutel, hoe moeilijker het is om de sleutel te achterhalen. Kies hier bij voorkeur 4096. Je kunt, net zoals een ssh key, er voor keizen om deze sleutel te laten verlopen op een bepaalde datum. De keuze is aan jou. Bevestig nu de keuze met y. 
Nu moeten er gegevens in de sleutel worden gezet die onze identiteit bepalen. Vul je naam en je **hva emailadres** in. Je bent tenslotte ingelogd op gitlab met je hva id. Kies hierna een sterk wachtwoord. Het volgende commando kun je gebruiken om de sleutel die je zojuist hebt gegenereerd, weer te geven.

`gpg --list-secret-keys --keyid-format LONG <hva-email>`

De output zal dan als volgt eruit zien, uiteraard met de gegevens van jouw eigen sleutel, de stappen hierna moeten uiteraard ook met de eigen gegevens worden gedaan:

`sec   rsa4096/30F2B65B9246B6CA 2017-08-18 [SC]`
      `D5E4F29F3275DC0CDA8FFC8730F2B65B9246B6CA`
`uid                   [ultimate] Voorbeeld <hva-email>`
`ssb   rsa4096/B7ABC0813E4028C0 2017-08-18 [E]`

Kopieer nu het id wat begint bij sec, in dit geval **30F2B65B9246B6CA**. Je kunt dit exporteren om je public key te bekijken.

`gpg --armor --export 30F2B65B9246B6CA`

Kopieer de public key, en voeg het toe in [Gitlab](https://gitlab.fdmci.hva.nl/-/profile/gpg_keys). Deze kun je vinden bij Preferences -> GPG Keys.
Nu we de slutel hebben toegevoegd in gitlab, kunnen we hem gebruiken in git. Je gebruikt weer het id.

`git config --global user.signingkey 30F2B65B9246B6CA`

Het kan zijn dat git niet weet waar de sleutel of gpg zelf staat. Dit kan bijvoorbeeld het geval zijn als git en gpg op aparte schijven geïnstalleerd zijn. In cmd kun je bekijken waar gpg geïnstalleerd is. 

`where gpg`

Kopieer het pad en selecteer hem met git.

`git config --global gpg.program <pad_naar_gpg>`

Als het goed is werkt de pgp sleutel nu, en kun je geverifieerd commits maken in je repository. Mocht je een verified commit willen maken, dan voeg je -S toe aan de commit.

`git commit -S -m "een mooi bericht"`

Het ondertekenen kan ook automatisch.

`git config --global commit.gpgsign true`
