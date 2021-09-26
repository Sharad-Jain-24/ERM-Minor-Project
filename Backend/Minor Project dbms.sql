-- Show version of mysql components
SHOW VARIABLES LIKE "%version%";
-- DEVELOPMENT COMPONENTS
-- +--------------------------+-------------------------------+
-- | Variable_name            | Value                         |
-- +--------------------------+-------------------------------+
-- | immediate_server_version | 999999                        |
-- | innodb_version           | 8.0.19                        |
-- | original_server_version  | 999999                        |
-- | protocol_version         | 10                            |
-- | slave_type_conversions   |                               |
-- | tls_version              | TLSv1,TLSv1.1,TLSv1.2,TLSv1.3 |
-- | version                  | 8.0.19                        |
-- | version_comment          | MySQL Community Server - GPL  |
-- | version_compile_machine  | x86_64                        |
-- | version_compile_os       | Win64                         |
-- | version_compile_zlib     | 1.2.11                        |
-- +--------------------------+-------------------------------+

-- PRODUCTION COMPONENTS
-- +-------------------------+---------------------+
-- | Variable_name           | Value               |
-- +-------------------------+---------------------+
-- | innodb_version          | 5.6.48              |
-- | protocol_version        | 10                  |
-- | slave_type_conversions  |                     |
-- | version                 | 5.6.48-log          |
-- | version_comment         | Source distribution |
-- | version_compile_machine | x86_64              |
-- | version_compile_os      | Linux               |
-- +-------------------------+---------------------+

-- Create a database.
CREATE DATABASE minor_DB;

-- Show all databases.
SHOW DATABASES;

-- Use "minor_db" database.
USE minor_DB;

DROP DATABASE minor_DB;

-- Create user table
-- It is used to store user details.
CREATE TABLE `user` (
  `User_id` INT AUTO_INCREMENT NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `Email_id` VARCHAR(45) NOT NULL,
  `Phone` VARCHAR(15) NOT NULL,
  `Password` VARCHAR(100) NOT NULL,
  `Permission` INT NOT NULL,
  PRIMARY KEY (`User_id`),
  UNIQUE INDEX `Email_id_UNIQUE` (`Email_id` ASC),
  UNIQUE INDEX `User_id_UNIQUE` (`User_id` ASC));

-- DROP TABLE user;
-- DROP TABLE registration;
-- DROP TABLE participants;
-- DROP TABLE events;

-- Display list of tables.
SHOW TABLES;

-- Dispaly data of all tables.
SELECT * FROM user;
SELECT * FROM participants;
SELECT * FROM events;
SELECT * FROM registration;

SELECT present FROM registration WHERE p_id = "dummy8-8222222222" AND event_id = "2";

SELECT * FROM participants WHERE p_id = "dummy7-7111111111";

-- Display login credentials of all users.
SELECT email_id, password, permission FROM user;

-- Display details of participants and events they are registered in.
SELECT `participants`.*, GROUP_CONCAT(`events`.name, `registration`.present) as "events"
FROM ((`participants`
INNER JOIN `registration` ON `participants`.p_id = `registration`.p_id)
INNER JOIN `events` ON `events`.event_id = `registration`.event_id)
group by p_id;


-- Create participants table
-- It is used to store participants details.
CREATE TABLE `participants` (
  `p_id` VARCHAR(50) NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `Email_id` VARCHAR(45) NOT NULL,
  `Phone` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE INDEX `phone_UNIQUE` (`phone` ASC),
  UNIQUE INDEX `idparticipants_UNIQUE` (`p_id` ASC));

-- Create events table
-- It is used to store event details.
CREATE TABLE `events` (
  `event_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  `date` DATE NOT NULL,
  `time` TIME NOT NULL,
  PRIMARY KEY (`event_id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC),
  UNIQUE INDEX `event_id_UNIQUE` (`event_id` ASC));

-- Create registration table
-- It is used to store participant ID and event ID for each registration along with entry of participants.
CREATE TABLE `registration` (
  `r_id` INT NOT NULL AUTO_INCREMENT,
  `p_id` VARCHAR(50) NOT NULL,
  `event_id` INT NOT NULL,
  `present` INT NOT NULL,
  PRIMARY KEY (`r_id`),
  UNIQUE INDEX `r_id_UNIQUE` (`r_id` ASC),
  INDEX `p_id_idx` (`p_id` ASC),
  INDEX `event_id_idx` (`event_id` ASC),
  CONSTRAINT `p_id`
    FOREIGN KEY (`p_id`)
    REFERENCES `minor_db`.`participants` (`p_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `event_id`
    FOREIGN KEY (`event_id`)
    REFERENCES `minor_db`.`events` (`event_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
  
