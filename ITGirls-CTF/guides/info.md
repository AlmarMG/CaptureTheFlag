# Git guide

### Shortcut: pushen naar master branch

In dit vb hebben we 2 branches: master (de branch waarnaar we willen pushen) en testing (waar we nieuwe functies in hebben gemaakt.)
Om te pushen naar bijvoorbeeld de master branch, zorg je dat je eerst alles gecommit en gepushed hebt in testing. 
Switch nu naar master met `git checkout master`
Als dit niet werkt kun je altijd nog `git branch -r` gebruiken. Je ziet dan alle verschillende branches.
Ga nu naar de master branch (meestal origin/master).
In de master branch kun je gemakkelijk mergen met `git merge testing`.

### Inleiding
Dit is een mini documentatie van benodigde commando's/handigheidjes die je kunt gebruiken tijdens dit project.
Als er iets op de terminal (lees: cmd) zal moeten worden uitgevoerd, zal dit worden aangegeven met een $ of `code block`
In het begin staat een stappenplan, om vlug te refereren naar bepaalde stappen.

repo = repository

###### Cheatsheet
1. $ git config --global user.name "John Doe"
2. $ git config --global user.email johndoe@example.com
3.  $ git init
4.  $ ssh-keygen -t ed25519
5.  $ git clone ssh url van repo
6.  $ git commit -m "een mooi bericht"
7.  $ git push
8. $ git pull


### Stappenplan

1.   Installeer eerst git: [Website](https://git-scm.com/downloads) 
    Specificeer dan eerst de gebruiker, zodat git jou kan onderscheiden van andere gebruikers: 

`$ git config --global user.name "John Doe"`
`$ git config --global user.email johndoe@example.com`


Ga naar een folder waar jij de gegevens uit een repository wilt importeren 
    VB: Ik wil een map genaamd 'PAD' met daarin de bestanden die ik importeer uit een repository.
            ~\PAD\
    Om deze map te gebruiken moet je deze eerst initialiseren, je maakt dan een lokale repository aan zodat je daar in kan editen voordat je het pusht naar een externe repository.

`$ git init`


2.   De volgende stap is het verbinden/clonen van de externe repository. Dit kan aan de hand van een wachtwoord, maar er wordt aangeraden om dit via ssh te doen.
    Om een ssh key aan te maken, zullen we een type encryptie moeten kiezen. Om de zoveel tijd zal er een nieuwe en veiligere soort encryptie beschikbaar komen, maar op dit moment is dat ed25519.

`$ ssh-keygen -t ed25519`

Er zal worden gevraagd of je de ssh key wilt opslaan op een spcifieke plek, mocht dit het geval zijn, vul dan hier de bestandslocatie in. klik in andere gevallen op enter.
    Nu kun je een wachtwoord op je ssh-key zetten, dit is niet verplicht, maar wel raadzaam
    Als het goed is, is je ssh key nu aangemaakt, deze kan je vinden in de locatie die je hebt opgegeven --> Enter file in which to save the key (locatie-van-de-sleutel):
    
Het is belangrijk deze sleutel ook te laten herkennen door GitLab (https://gitlab.fdmci.hva.nl/users/sign_in), hiervoor log je in met je hva-id.
    Klik hiera rechtsboven op je avatar, daarna "Preferences".
    In de kolom links zie je [SSH Keys](https://gitlab.fdmci.hva.nl/-/profile/keys), ga naar deze pagina.
    Je kan hier je ssh key de je net hebt gemaakt toevoegen, dit doe je door je publieke sleutel aan GitLab toe te voegen.
    Om je publieke sleutel te achterhalen, ga je naar de locatie van je ssh-key. Daar staan 2 bestanden, 1 zonder extentie en 1 met .pub of Microsoft publisher bestand.
    Het .pub bestand willen we openen met een texteditor (kladblok, sublime, vsc, n++ etc.), de inhoud hiervan zet je in gitlab.
    Je kunt je sleutel een naam geven, voor als je meerdere keys hebt. Je kunt ook een datum geven waarop deze sleutel niet meer werkt.
    klik op add key en je sleutel is aangemaakt, deze kunnen we nu gebruiken om een repository te clonen.
    


3. Ga naar de homepagina van je project, je ziet daar een knop 'Clone' staan. kopieer hiervan het ssh gedeelte. (Wat begint met git@......).

`$ git clone *ssh url van de repo`

Als het goed is, is er een map aangemaakt met de naam van het project op gitlab. Om dingen te wijzige zullen we daarom eerst hiernaartoe moeten gaan

`$ cd *naam-project*`

3.5    Nu kun je bestanden aanmaken en wijzigen. Het kan zijn dat je meerdere braches hebt aangemaakt, deze kun je zien met de volgende commando's:

`$ git branch`
`$ git branch -r`

Je kunt zien in welke branch je nu zit met "git branch", en alle beschikbare branches zie je met "git branch -r" Om te wisselen van branch gebruik je checkout.

`$ git checkout *branch waar je naartoe wilt*`



4.   Om jou wijzigen ook daadwerkelijk beschikbaar te maken voor andere teamleden, zal er eerst een commit moeten worden aangemaakt.
    Met een commit update je bestanden die op de externe repo staan. Er kunnen meerdere commit's tegelijkertijd worden verstuurd/gepushed.
    Als ik bijvoorbeeld aan een deel backend en frontend heb gewerkt, wil ik liever niet dat die in 1 commit staan. Ik kan dan naar de desbetreffennde folder gaan, en handmatig het bestand toevoegen.

`$ git add _pad naar bestand_` <-- Voor individuele bestanden
`$ git add .` <-- Om alles in de huidige folder aan de commit toe te voegen

Je kunt aan de hand van git status bekijken of je bestanden zijn toegevoegd aan je commit.

`$ git status`

Als het goed is zie je groene bestandsnamen, wat inhoud dat deze in de huidige commit staan. Mocht je bestanden uit de commit willen halen, dan kan dit met git reset.

`$ git reset`



5.   Het is nu tijd om de veranderingen daadwerkelijk te committen. Je voegt een bericht toe (-m ""), om te zeggen wat je veranderd hebt. Er kan hier ook een optie worden toegeveogd zodat je commit wordt geverifieerd, maar dat wordt niet besproken in deze documentatie

`$ git commit -m "een mooi bericht"`



6.  Nu onze commit is doorgezet in de lokale repository, willen wij dit delen met andere teamleden. Dit doen we door te pushen.

`$ git push`

7.  Jouw wijzigen zijn nu doorgevoerd, om de wijzigingen van anderen te bekijken moet je pullen uit je repo.

`$ git pull`

Dit is een volledige doorloop van een enkele commit in Git. Stap 1 t/m 3 zijn alleen nodig als setup. 
    Hierna kun je altijd beginnen met pullen, en daarna bij stap 4 verder te gaan
