-- -----------------------------------------------------
-- Schema Gegevens
-- -----------------------------------------------------
USE `Gegevens`;

-- -----------------------------------------------------
-- Table `Gegevens`.`Gebruiker`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gegevens`.`Gebruiker` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `gebruikersnaam` VARCHAR(50) NOT NULL,
  `wachtwoord` VARCHAR(64) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Gegevens`.`Challenge`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gegevens`.`Challenge` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `naam` VARCHAR(20) NOT NULL,
  `score` INT NOT NULL,
  `flag` CHAR(21) NOT NULL,
  `moeilijkheidsgraad` INT NOT NULL,
  `flaskNaam` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Gegevens`.`HintPagina`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gegevens`.`HintPagina` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `challengeId` INT NOT NULL,
  `flaskNaam` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_HintPerChallenge_Challenge1_idx` (`challengeId` ASC) VISIBLE,
  CONSTRAINT `fk_HintPerChallenge_Challenge1`
    FOREIGN KEY (`challengeId`)
    REFERENCES `Gegevens`.`Challenge` (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Gegevens`.`Hint`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gegevens`.`Hint` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `titel` VARCHAR(100) NOT NULL,
  `waarde` INT NOT NULL,
  `beschrijving` VARCHAR(255) NOT NULL,
  `hintPaginaId` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Hint_HintPagina1_idx` (`hintPaginaId` ASC) VISIBLE,
  CONSTRAINT `fk_Hint_HintPagina1`
    FOREIGN KEY (`hintPaginaId`)
    REFERENCES `Gegevens`.`HintPagina` (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Gegevens`.`ChallengeStatus`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gegevens`.`ChallengeStatus` (
  `gebruikerId` INT NOT NULL,
  `challengeId` INT NOT NULL,
  `status` TINYINT(1) NOT NULL,
  PRIMARY KEY (`gebruikerId`, `challengeId`),
  INDEX `fk_Gebruiker_has_Challenge_Challenge1_idx` (`challengeId` ASC) VISIBLE,
  INDEX `fk_Gebruiker_has_Challenge_Gebruiker1_idx` (`gebruikerId` ASC) VISIBLE,
  CONSTRAINT `fk_Gebruiker_has_Challenge_Gebruiker1`
    FOREIGN KEY (`gebruikerId`)
    REFERENCES `Gegevens`.`Gebruiker` (`id`),
  CONSTRAINT `fk_Gebruiker_has_Challenge_Challenge1`
    FOREIGN KEY (`challengeId`)
    REFERENCES `Gegevens`.`Challenge` (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Gegevens`.`HintStatus`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gegevens`.`HintStatus` (
  `hintId` INT NOT NULL,
  `gebruikerId` INT NOT NULL,
  `status` TINYINT(1) NOT NULL,
  PRIMARY KEY (`hintId`, `gebruikerId`),
  INDEX `fk_Hint_has_Gebruiker_Gebruiker1_idx` (`gebruikerId` ASC) VISIBLE,
  INDEX `fk_Hint_has_Gebruiker_Hint1_idx` (`hintId` ASC) VISIBLE,
  CONSTRAINT `fk_Hint_has_Gebruiker_Hint1`
    FOREIGN KEY (`hintId`)
    REFERENCES `Gegevens`.`Hint` (`id`),
  CONSTRAINT `fk_Hint_has_Gebruiker_Gebruiker1`
    FOREIGN KEY (`gebruikerId`)
    REFERENCES `Gegevens`.`Gebruiker` (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Gegevens`.`Container`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gegevens`.`Container` (
  `gebruikerId` INT NOT NULL,
  `challengeNaam` VARCHAR(45) NOT NULL,
  `port` INT NOT NULL,
  `status` TINYINT(1) NOT NULL,
  PRIMARY KEY (`gebruikerId`, `challengeNaam`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Data for table `Gegevens`.`Gebruiker`
-- -----------------------------------------------------
START TRANSACTION;
USE `Gegevens`;

INSERT INTO `Gebruiker` (`gebruikersnaam`, `wachtwoord`)
    VALUES ('testnaam', '$2b$12$/KQCNwt0g1abOE/UXLWy7.PVKUaiQ/GvRWqErA1GiONet1Y7S/Hvm');
    -- ww = Testww123

COMMIT;


-- -----------------------------------------------------
-- Data for table `Gegevens`.`Challenge`
-- -----------------------------------------------------
START TRANSACTION;
USE `Gegevens`;

INSERT INTO `Challenge` (`naam`, `score`, `flag`, `moeilijkheidsgraad`, `flaskNaam`)
    VALUES  ('Vlog', '20', 'flag(9Cd77WVKonFlsE2)', '1', 'vlog'),
            ('Moeilijk', '20', 'flag(dH9dhdDjeD984D1)', '1', 'moeilijk'),
            ('Wireshark', '20', 'flag(goegvsnmlzpue28)', '1', 'wireshark'),
            ('Encodedchat', '20', 'flag(f84jgnv83k1la04)', '1', 'encodedchat'),
            ('Cookie', '40', 'flag(ijygiGe7xA3JeHQ)', '2', 'cookie'),
            ('Mail', '40', 'flag(Dtrlaf3G0SPszNh)', '2', 'mail'),
            ('Socialmedia', '40', 'flag(f82d92jfa93jd9a)', '2', 'socialmedia'),
            ('Chatbot', '80', 'flag(9c58b7cb81515f3)', '3', 'chatbot');
            

COMMIT;


-- -----------------------------------------------------
-- Data for table `Gegevens`.`ChallengeStatus`
-- -----------------------------------------------------
START TRANSACTION;
USE `Gegevens`;
INSERT INTO `Gegevens`.`ChallengeStatus` (`gebruikerId`, `challengeId`, `status`) 
-- Values for testuser
    VALUES (1, 1, 0), (1, 2, 0), (1, 3, 0),
            (1, 4, 0), (1, 5, 0),
            (1, 6, 0), (1, 7, 0), (1, 8, 0);

COMMIT;


-- -----------------------------------------------------
-- Data for table `Gegevens`.`HintPagina`
-- -----------------------------------------------------
START TRANSACTION;
USE `Gegevens`;

INSERT INTO `HintPagina` (`challengeId`, `flaskNaam`)
    VALUES  ('1', 'hints_vlog'),
            ('2', 'hints_moeilijk'),
            ('3', 'hints_wireshark'),
            ('4', 'hints_encodedchat'),
            ('5', 'hints_cookie'),
            ('6', 'hints_mail'),
            ('7', 'hints_socialmedia'),
            ('8', 'hints_chatbot');

COMMIT;

-- -----------------------------------------------------
-- Data for table `Gegevens`.`Hint`
-- -----------------------------------------------------
START TRANSACTION;
USE `Gegevens`;
-- Alle hints gekoppeld aan de challenges
INSERT INTO `Hint` (`id`, `titel`, `waarde`, `beschrijving`, `hintPaginaId`)
    VALUES ('1', 'hint 1', '10', 'Kijk wat dieper in de pagina', '1'),
            ('2', 'hint 2', '20', 'Inspecteer op een andere manier, niet met je muis', '1'),
            ('3', 'hint 3', '40', 'Zoek naar comments in de code', '1'),
            ('4', 'hint 1', '10', 'Na het invoeren van een verkeerd wachtwoord word deze handeling opgeslagen in een cookie', '2'),
            ('5', 'hint 2', '20', 'Je kunt de cookie bekijken met de developer tools van je browser', '2'),
            ('6', 'hint 3', '40', 'De cookie is encoded, gelukkig kun je deze decoderen. Er word gebruik gemaakt van dezelfde encoding als bij de encoded chat challenge.', '2'),
            ('7', 'hint 1', '10', 'Denk niet aan encryptie, deze chat maakt gebruik van encoding', '3'),
            ('8', 'hint 2', '20', 'Je hebt tools op internet om deze berichten te decoden', '3'),
            ('9', 'hint 3', '40', 'Er word gebruik gemaakt van base64 encoding', '3'),
            ('10', 'hint 1', '10', 'Op welke manier kan er informatie worden gelekt?', '4'),
            ('11', 'hint 2', '20', 'Verstuur een mail naar jezelf', '4'),
            ('12', 'hint 3', '40', 'Wat is het format van alle oplossingen?', '4'),
            ('13', 'hint 1', '10', 'Lees de tekst op de site goed', '5'),
            ('14', 'hint 2', '20', 'Kijk goed naar de afbeeldingen', '5'),
            ('15', 'hint 3', '40', 'Let op de metadata van de afbeelding', '5'),
            ('16', 'hint 1', '10', 'Kijk eens goed naar de console voor scherm 1', '6'),
            ('17', 'hint 2', '20', 'Een winkel lijkt mij wel een goede plek om creditcard informatie te vinden voor scherm 2. Een tip: maak gebruik van meerdere tabladen!', '6'),
            ('18', 'hint 3', '40', 'Voor scherm 3 is het handig om de "gevoelig/lijst/" te gebruiken want op elke pagina is wel wat informatie te vinden. Kijk ook eens goed naar je cookies!', '6'),
            ('19', 'hint 1', '10', 'Download wireshark om het bestand te kunnen openen', '7'),
            ('20', 'hint 2', '20', 'Analyseer niet te diep in het bestand', '7'),
            ('21', 'hint 3', '40', 'Kijk naar de 3e packet', '7'),
            ('22', 'hint 1', '10', 'Bekijk de video goed', '8'),
            ('23', 'hint 2', '20', 'De flag is in de achtergrond te vinden', '8'),
            ('24', 'hint 3', '40', 'De flag is te zien terwijl de teddybeer word gepakt', '8');

COMMIT;

-- -----------------------------------------------------
-- Data for table `Gegevens`.`HintStatus`
-- -----------------------------------------------------
START TRANSACTION;
USE `Gegevens`;
-- Values for testuser
INSERT INTO `HintStatus` (`hintId`, `gebruikerId`, `status`)
    VALUES ('1', '1', '0'),
            ('2', '1', '0'),
            ('3', '1', '0'),
            ('4', '1', '0'),
            ('5', '1', '0'),
            ('6', '1', '0'),
            ('7', '1', '0'),
            ('8', '1', '0'),
            ('9', '1', '0'),
            ('10', '1', '0'),
            ('11', '1', '0'),
            ('12', '1', '0'),
            ('13', '1', '0'),
            ('14', '1', '0'),
            ('15', '1', '0'),
            ('16', '1', '0'),
            ('17', '1', '0'),
            ('18', '1', '0'),
            ('19', '1', '0'),
            ('20', '1', '0'),
            ('21', '1', '0'),
            ('22', '1', '0'),
            ('23', '1', '0'),
            ('24', '1', '0');

COMMIT;