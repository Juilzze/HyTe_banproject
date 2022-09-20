-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.4.24-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for bans_2022
CREATE DATABASE IF NOT EXISTS `bans_2022` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `bans_2022`;

-- Dumping structure for table bans_2022.bans
CREATE TABLE IF NOT EXISTS `bans` (
  `banid` int(11) NOT NULL,
  `username` varchar(30) DEFAULT NULL,
  `reason` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `enddate` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`banid`) USING BTREE,
  KEY `username` (`username`),
  CONSTRAINT `bans_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table bans_2022.bans: ~0 rows (approximately)
DELETE FROM `bans`;
/*!40000 ALTER TABLE `bans` DISABLE KEYS */;
/*!40000 ALTER TABLE `bans` ENABLE KEYS */;

-- Dumping structure for table bans_2022.users
CREATE TABLE IF NOT EXISTS `users` (
  `username` varchar(30) NOT NULL,
  `pass` varchar(30) DEFAULT NULL,
  `admin` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`username`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table bans_2022.users: ~1 rows (approximately)
DELETE FROM `users`;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`username`, `pass`, `admin`) VALUES
	('Juuso', 'moi123', 1);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

-- Dumping structure for table bans_2022.warns
CREATE TABLE IF NOT EXISTS `warns` (
  `warnid` int(11) NOT NULL,
  `username` varchar(30) DEFAULT NULL,
  `reason` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`warnid`) USING BTREE,
  KEY `username` (`username`),
  CONSTRAINT `warns_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table bans_2022.warns: ~0 rows (approximately)
DELETE FROM `warns`;
/*!40000 ALTER TABLE `warns` DISABLE KEYS */;
/*!40000 ALTER TABLE `warns` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
