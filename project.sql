-- MySQL dump 10.13  Distrib 8.0.17, for Linux (x86_64)
--
-- Host: localhost    Database: dbda_aug_2019
-- ------------------------------------------------------
-- Server version	8.0.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `s_name` varchar(20) DEFAULT NULL,
  `nation` varchar(20) DEFAULT NULL,
  `state` varchar(20) DEFAULT NULL,
  `cmmnt` text,
  `emailid` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
INSERT INTO `project` VALUES (1,'rajveer singh','sisodiya','Bharat','Madhya Pradesh','Its the first entry after creating this project with Django framework.','rajveer.rajput18.1996@gmail.con'),(2,'rajveer singh','sisodiya','Bharat','Madhya Pradesh','2nd time checking with Django + Mysql.','usdokomo.10@gmail.com'),(3,'rajveer singh','sisodiya','Bharat','Maharashtra','3rd time checking dB for the pop-up window.','rajveer.rajput18.1996@gmail.con'),(4,'vikas ','thakur','Bharat','mp','4th time checking pop-up window.','usdokomo.10@gmail.com'),(5,'vikas ','thakur','bha','Madhya Pradesh','4th time checking pop-up window.','usdokomo.10@gmail.com'),(6,'rajveer singh','sisodiya','bha','mp','5th time checking of message.','vikasthakur@gmail.com'),(7,'rajveer singh','thakur','India','Madhya Pradesh','final checking of message box.','rajveer.rajput18.1996@gmail.con'),(8,'rajveer singh','thakur','Bharat','Maharashtra','final1 checking of message box.','usdokomo.10@gmail.com'),(9,'rajveer singh','sisodiya','India','Maharashtra','final3 checking of message box.','rajveer.rajput18.1996@gmail.com'),(10,'rajveer singh','sisodiya','Bharat','Madhya Pradesh','Now the testing is working fine.','rajveer.rajput18.1996@gmail.com'),(11,'vikas ','sisodiya','Bharat','Madhya Pradesh','just testing another day.','vikassingh@gmail.com'),(12,'rajveer singh','thakur','Bharat','Madhya Pradesh','again checking.','vikasthakur@gmail.com'),(13,'rajveer singh','thakur','Bharat','Maharashtra','again hcecking1.','rajveer.rajput18.1996@gmail.com'),(14,'vikas ','sisodiya','India','Madhya Pradesh','nothing keeps white.','usdokomo.10@gmail.com'),(15,'rajveer singh','sisodiya','Bharat','Madhya Pradesh','fjdsk','vikassingh@gmail.com'),(16,'rajveer singh','sisodiya','Bharat','Madhya Pradesh','fjdsk','vikassingh@gmail.com'),(17,'rajveer singh','sisodiya','Bharat','Madhya Pradesh','fjdsk','vikassingh@gmail.com'),(18,'rajveer singh','sisodiya','Bharat','Madhya Pradesh','fjdsk','vikassingh@gmail.com'),(19,'vikas ','thakur','Bharat','Madhya Pradesh','dd','rajveer.rajput18.1996@gmail.con'),(20,'rajveer ','sisodiya','Bharat','Maharashtra','check','vikassingh@gmail.com'),(21,'vikas ','thakur','Bharat','mp','showing msg.','usdokomo.10@gmail.com'),(22,'rajveer singh','thakur','Bharat','Maharashtra','again check.','rajveer.rajput18.1996@gmail.con'),(23,'rajveer singh','sisodiya','Bharat','Madhya Pradesh','1513','rajveer.rajput18.1996@gmail.com'),(24,'vikas ','singh','Bharat','Madhya Pradesh','dfkj','vikasthakur@gmail.com');
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-16 21:56:09
