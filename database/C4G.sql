-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema c4g
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema c4g
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `c4g` DEFAULT CHARACTER SET latin1 ;
USE `c4g` ;

-- -----------------------------------------------------
-- Table `c4g`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `c4g`.`customer` (
  `E-mail` VARCHAR(250) NOT NULL,
  `Name` VARCHAR(50) NOT NULL,
  `Adress` VARCHAR(250) NOT NULL,
  PRIMARY KEY (`E-mail`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `c4g`.`role`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `c4g`.`role` (
  `ID` INT(11) NOT NULL,
  `RoleName` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `c4g`.`region`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `c4g`.`region` (
  `ID` INT(11) NOT NULL,
  `RegionName` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `c4g`.`mentor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `c4g`.`mentor` (
  `E-mail` VARCHAR(250) NOT NULL,
  `First name` VARCHAR(45) NOT NULL,
  `Surname` VARCHAR(45) NOT NULL,
  `Role` INT(11) NOT NULL,
  `Region` INT(11) NOT NULL,
  `Hashpass` VARCHAR(250) NOT NULL,
  `Country` VARCHAR(45) NULL DEFAULT NULL,
  `City` VARCHAR(45) NULL DEFAULT NULL,
  `MobileNum` VARCHAR(45) NULL DEFAULT NULL,
  `Age` INT(11) NULL DEFAULT NULL,
  `Sector` VARCHAR(500) NOT NULL,
  PRIMARY KEY (`E-mail`),
  INDEX `isIN2_idx` (`Region` ASC),
  INDEX `is2_idx` (`Role` ASC),
  CONSTRAINT `is2`
    FOREIGN KEY (`Role`)
    REFERENCES `c4g`.`role` (`ID`)
    ON UPDATE CASCADE,
  CONSTRAINT `isIN2`
    FOREIGN KEY (`Region`)
    REFERENCES `c4g`.`region` (`ID`)
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `c4g`.`mentee`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `c4g`.`mentee` (
  `E-mail` VARCHAR(250) NOT NULL,
  `First name` VARCHAR(45) NOT NULL,
  `Surname` VARCHAR(45) NOT NULL,
  `Region` INT(11) NOT NULL,
  `Role` INT(11) NOT NULL,
  `Mentor` VARCHAR(250) NOT NULL,
  `Menteecol` VARCHAR(45) NOT NULL,
  `HashPass` VARCHAR(250) NOT NULL,
  `Sector` VARCHAR(500) NOT NULL,
  PRIMARY KEY (`E-mail`),
  INDEX `isIN1_idx` (`Region` ASC),
  INDEX `is1_idx` (`Role` ASC),
  INDEX `MentoredBy_idx` (`Mentor` ASC),
  CONSTRAINT `MentoredBy`
    FOREIGN KEY (`Mentor`)
    REFERENCES `c4g`.`mentor` (`E-mail`)
    ON UPDATE CASCADE,
  CONSTRAINT `is1`
    FOREIGN KEY (`Role`)
    REFERENCES `c4g`.`role` (`ID`)
    ON UPDATE CASCADE,
  CONSTRAINT `isIN1`
    FOREIGN KEY (`Region`)
    REFERENCES `c4g`.`region` (`ID`)
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `c4g`.`buysfrom`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `c4g`.`buysfrom` (
  `ID` INT(11) NOT NULL,
  `CustomerID` VARCHAR(250) NOT NULL,
  `ManteeID` VARCHAR(250) NOT NULL,
  PRIMARY KEY (`ID`),
  INDEX `ManteeLink_idx` (`ManteeID` ASC),
  INDEX `CustomerLink_idx` (`CustomerID` ASC),
  CONSTRAINT `CustomerLink`
    FOREIGN KEY (`CustomerID`)
    REFERENCES `c4g`.`customer` (`E-mail`)
    ON UPDATE CASCADE,
  CONSTRAINT `ManteeLink`
    FOREIGN KEY (`ManteeID`)
    REFERENCES `c4g`.`mentee` (`E-mail`)
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
