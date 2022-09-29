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
  `banid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) DEFAULT NULL,
  `reason` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `enddate` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`banid`) USING BTREE,
  KEY `username` (`username`),
  CONSTRAINT `bans_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table bans_2022.bans: ~4 rows (approximately)
DELETE FROM `bans`;
/*!40000 ALTER TABLE `bans` DISABLE KEYS */;
INSERT INTO `bans` (`banid`, `username`, `reason`, `date`, `enddate`) VALUES
	(1, '123v3v1', 'test', '1/1/2000', '1/2/2000'),
	(2, '123v3v1', 'test', '1/1/2000', '1/2/2000'),
	(3, '123v3v1', 'test', '1/1/2000', '1/2/2000'),
	(4, 'Juuso', 'Testi ban', '2022-09-21', '2022-10-01');
/*!40000 ALTER TABLE `bans` ENABLE KEYS */;

-- Dumping structure for table bans_2022.users
CREATE TABLE IF NOT EXISTS `users` (
  `username` varchar(30) NOT NULL,
  `pass` varchar(30) DEFAULT NULL,
  `admin` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`username`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table bans_2022.users: ~17 rows (approximately)
DELETE FROM `users`;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`username`, `pass`, `admin`) VALUES
	('', '', 0),
	('1', '0', 0),
	('123', '55', 1),
	('1231', '123', 1),
	('12399', '55', 1),
	('123v3v1', '1v233v12', 1),
	('itsesaatana', 'lol', 1),
	('ja22aha22s2', 'ha2a2', 0),
	('ja22aha22s2jaaaaaaaa', 'ha2a2', 0),
	('ja22aha2s2', 'ha2a2', 0),
	('jaaha2s2', 'ha2a2', 0),
	('jaahas', 'haa', 0),
	('jaahas2', 'haa2', 0),
	('Juuso', 'moi123', 1),
	('KaHipu', 'KaHipu', 0),
	('superidol', 'kana', 1),
	('testiii123', '123', 1);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

-- Dumping structure for table bans_2022.warns
CREATE TABLE IF NOT EXISTS `warns` (
  `warnid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) DEFAULT NULL,
  `reason` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`warnid`) USING BTREE,
  KEY `username` (`username`),
  CONSTRAINT `warns_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table bans_2022.warns: ~1 rows (approximately)
DELETE FROM `warns`;
/*!40000 ALTER TABLE `warns` DISABLE KEYS */;
INSERT INTO `warns` (`warnid`, `username`, `reason`, `date`) VALUES
	(1, 'testiii123', 'Testaus', '21/09/2022');
/*!40000 ALTER TABLE `warns` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
