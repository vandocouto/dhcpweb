-- MySQL dump 10.13  Distrib 5.5.31, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: dhcpweb
-- ------------------------------------------------------
-- Server version	5.5.31-0+wheezy1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admconf`
--

DROP TABLE IF EXISTS `admconf`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admconf` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `c_caminho_conf` int(2) NOT NULL,
  `c_dns_update` varchar(3) NOT NULL,
  `c_gateway` varchar(15) NOT NULL,
  `c_autoritario` varchar(3) NOT NULL,
  `c_offset` varchar(10) NOT NULL,
  `c_bootp` varchar(3) NOT NULL,
  `c_ntp` varchar(30) DEFAULT NULL,
  `c_booting` varchar(3) NOT NULL,
  `c_subnet` varchar(15) NOT NULL,
  `c_subnet_mask` varchar(15) NOT NULL,
  `c_proxy_url` varchar(60) DEFAULT NULL,
  `c_pxe_path` varchar(30) DEFAULT NULL,
  `c_domain_name` varchar(60) DEFAULT NULL,
  `c_pxe_filename` varchar(30) DEFAULT NULL,
  `c_name_servers` varchar(60) DEFAULT NULL,
  `c_pxe_server` varchar(15) DEFAULT NULL,
  `c_netbios_name` varchar(60) DEFAULT NULL,
  `c_deft_lease_time` int(15) NOT NULL,
  `c_max_lease_time` int(15) NOT NULL,
  `c_range_inicio` varchar(15) DEFAULT NULL,
  `c_range_fim` varchar(15) DEFAULT NULL,
  `data` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admconf`
--

LOCK TABLES `admconf` WRITE;
/*!40000 ALTER TABLE `admconf` DISABLE KEYS */;
INSERT INTO `admconf` VALUES (1,6,'','','','','',NULL,'','','',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,NULL,NULL,'2014-01-19 19:18:28'),(2,6,'sim','','','','',NULL,'','','',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,NULL,NULL,'2014-01-19 19:21:17'),(3,6,'sim','192.168.6.1','sim','-18000;','sim','192.168.1.41, 192.168.1.43','sim','192.168.6.0','255.255.254.0','None','None','tgl.com.br tutoriaisgnulinux.com','None','192.168.6.1','None','192.168.1.41, 192.168.1.43',21600,86400,'None','None','2014-01-20 12:49:14');
/*!40000 ALTER TABLE `admconf` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dhcp`
--

DROP TABLE IF EXISTS `dhcp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dhcp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(30) NOT NULL,
  `mac_address` varchar(17) NOT NULL,
  `ip_address` varchar(15) NOT NULL,
  `patrimonio` varchar(30) DEFAULT NULL,
  `grupo_fk` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hostname` (`hostname`),
  UNIQUE KEY `mac_address` (`mac_address`),
  UNIQUE KEY `ip_address` (`ip_address`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dhcp`
--

LOCK TABLES `dhcp` WRITE;
/*!40000 ALTER TABLE `dhcp` DISABLE KEYS */;
/*!40000 ALTER TABLE `dhcp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grupo`
--

DROP TABLE IF EXISTS `grupo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grupo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome_grupo` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nome_grupo` (`nome_grupo`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grupo`
--

LOCK TABLES `grupo` WRITE;
/*!40000 ALTER TABLE `grupo` DISABLE KEYS */;
INSERT INTO `grupo` VALUES (44,'desktop'),(40,'servidores');
/*!40000 ALTER TABLE `grupo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `perfil` int(11) NOT NULL,
  `usuario` varchar(15) NOT NULL,
  `senha` varchar(255) NOT NULL,
  `cookie` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario` (`usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES (1,1,'admin','YWRtaW4=','1-20052484','');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rede`
--

DROP TABLE IF EXISTS `rede`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rede` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip_address` varchar(15) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ip_address` (`ip_address`)
) ENGINE=InnoDB AUTO_INCREMENT=3918664 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rede`
--

LOCK TABLES `rede` WRITE;
/*!40000 ALTER TABLE `rede` DISABLE KEYS */;
INSERT INTO `rede` VALUES (3918155,'192.168.6.1'),(3918173,'192.168.6.10'),(3918353,'192.168.6.100'),(3918355,'192.168.6.101'),(3918357,'192.168.6.102'),(3918359,'192.168.6.103'),(3918361,'192.168.6.104'),(3918363,'192.168.6.105'),(3918365,'192.168.6.106'),(3918367,'192.168.6.107'),(3918369,'192.168.6.108'),(3918371,'192.168.6.109'),(3918175,'192.168.6.11'),(3918373,'192.168.6.110'),(3918375,'192.168.6.111'),(3918377,'192.168.6.112'),(3918379,'192.168.6.113'),(3918381,'192.168.6.114'),(3918383,'192.168.6.115'),(3918385,'192.168.6.116'),(3918387,'192.168.6.117'),(3918389,'192.168.6.118'),(3918391,'192.168.6.119'),(3918177,'192.168.6.12'),(3918393,'192.168.6.120'),(3918395,'192.168.6.121'),(3918397,'192.168.6.122'),(3918399,'192.168.6.123'),(3918401,'192.168.6.124'),(3918403,'192.168.6.125'),(3918405,'192.168.6.126'),(3918407,'192.168.6.127'),(3918409,'192.168.6.128'),(3918411,'192.168.6.129'),(3918179,'192.168.6.13'),(3918413,'192.168.6.130'),(3918415,'192.168.6.131'),(3918417,'192.168.6.132'),(3918419,'192.168.6.133'),(3918421,'192.168.6.134'),(3918423,'192.168.6.135'),(3918425,'192.168.6.136'),(3918427,'192.168.6.137'),(3918429,'192.168.6.138'),(3918431,'192.168.6.139'),(3918181,'192.168.6.14'),(3918433,'192.168.6.140'),(3918435,'192.168.6.141'),(3918437,'192.168.6.142'),(3918439,'192.168.6.143'),(3918441,'192.168.6.144'),(3918443,'192.168.6.145'),(3918445,'192.168.6.146'),(3918447,'192.168.6.147'),(3918449,'192.168.6.148'),(3918451,'192.168.6.149'),(3918183,'192.168.6.15'),(3918453,'192.168.6.150'),(3918455,'192.168.6.151'),(3918457,'192.168.6.152'),(3918459,'192.168.6.153'),(3918461,'192.168.6.154'),(3918463,'192.168.6.155'),(3918465,'192.168.6.156'),(3918467,'192.168.6.157'),(3918469,'192.168.6.158'),(3918471,'192.168.6.159'),(3918185,'192.168.6.16'),(3918473,'192.168.6.160'),(3918475,'192.168.6.161'),(3918477,'192.168.6.162'),(3918479,'192.168.6.163'),(3918481,'192.168.6.164'),(3918483,'192.168.6.165'),(3918485,'192.168.6.166'),(3918487,'192.168.6.167'),(3918489,'192.168.6.168'),(3918491,'192.168.6.169'),(3918187,'192.168.6.17'),(3918493,'192.168.6.170'),(3918495,'192.168.6.171'),(3918497,'192.168.6.172'),(3918499,'192.168.6.173'),(3918501,'192.168.6.174'),(3918503,'192.168.6.175'),(3918505,'192.168.6.176'),(3918507,'192.168.6.177'),(3918509,'192.168.6.178'),(3918511,'192.168.6.179'),(3918189,'192.168.6.18'),(3918513,'192.168.6.180'),(3918515,'192.168.6.181'),(3918517,'192.168.6.182'),(3918519,'192.168.6.183'),(3918521,'192.168.6.184'),(3918523,'192.168.6.185'),(3918525,'192.168.6.186'),(3918527,'192.168.6.187'),(3918529,'192.168.6.188'),(3918531,'192.168.6.189'),(3918191,'192.168.6.19'),(3918533,'192.168.6.190'),(3918535,'192.168.6.191'),(3918537,'192.168.6.192'),(3918539,'192.168.6.193'),(3918541,'192.168.6.194'),(3918543,'192.168.6.195'),(3918545,'192.168.6.196'),(3918547,'192.168.6.197'),(3918549,'192.168.6.198'),(3918551,'192.168.6.199'),(3918157,'192.168.6.2'),(3918193,'192.168.6.20'),(3918553,'192.168.6.200'),(3918555,'192.168.6.201'),(3918557,'192.168.6.202'),(3918559,'192.168.6.203'),(3918561,'192.168.6.204'),(3918563,'192.168.6.205'),(3918565,'192.168.6.206'),(3918567,'192.168.6.207'),(3918569,'192.168.6.208'),(3918571,'192.168.6.209'),(3918195,'192.168.6.21'),(3918573,'192.168.6.210'),(3918575,'192.168.6.211'),(3918577,'192.168.6.212'),(3918579,'192.168.6.213'),(3918581,'192.168.6.214'),(3918583,'192.168.6.215'),(3918585,'192.168.6.216'),(3918587,'192.168.6.217'),(3918589,'192.168.6.218'),(3918591,'192.168.6.219'),(3918197,'192.168.6.22'),(3918593,'192.168.6.220'),(3918595,'192.168.6.221'),(3918597,'192.168.6.222'),(3918599,'192.168.6.223'),(3918601,'192.168.6.224'),(3918603,'192.168.6.225'),(3918605,'192.168.6.226'),(3918607,'192.168.6.227'),(3918609,'192.168.6.228'),(3918611,'192.168.6.229'),(3918199,'192.168.6.23'),(3918613,'192.168.6.230'),(3918615,'192.168.6.231'),(3918617,'192.168.6.232'),(3918619,'192.168.6.233'),(3918621,'192.168.6.234'),(3918623,'192.168.6.235'),(3918625,'192.168.6.236'),(3918627,'192.168.6.237'),(3918629,'192.168.6.238'),(3918631,'192.168.6.239'),(3918201,'192.168.6.24'),(3918633,'192.168.6.240'),(3918635,'192.168.6.241'),(3918637,'192.168.6.242'),(3918639,'192.168.6.243'),(3918641,'192.168.6.244'),(3918643,'192.168.6.245'),(3918645,'192.168.6.246'),(3918647,'192.168.6.247'),(3918649,'192.168.6.248'),(3918651,'192.168.6.249'),(3918203,'192.168.6.25'),(3918653,'192.168.6.250'),(3918655,'192.168.6.251'),(3918657,'192.168.6.252'),(3918659,'192.168.6.253'),(3918661,'192.168.6.254'),(3918663,'192.168.6.255'),(3918205,'192.168.6.26'),(3918207,'192.168.6.27'),(3918209,'192.168.6.28'),(3918211,'192.168.6.29'),(3918159,'192.168.6.3'),(3918213,'192.168.6.30'),(3918215,'192.168.6.31'),(3918217,'192.168.6.32'),(3918219,'192.168.6.33'),(3918221,'192.168.6.34'),(3918223,'192.168.6.35'),(3918225,'192.168.6.36'),(3918227,'192.168.6.37'),(3918229,'192.168.6.38'),(3918231,'192.168.6.39'),(3918161,'192.168.6.4'),(3918233,'192.168.6.40'),(3918235,'192.168.6.41'),(3918237,'192.168.6.42'),(3918239,'192.168.6.43'),(3918241,'192.168.6.44'),(3918243,'192.168.6.45'),(3918245,'192.168.6.46'),(3918247,'192.168.6.47'),(3918249,'192.168.6.48'),(3918251,'192.168.6.49'),(3918163,'192.168.6.5'),(3918253,'192.168.6.50'),(3918255,'192.168.6.51'),(3918257,'192.168.6.52'),(3918259,'192.168.6.53'),(3918261,'192.168.6.54'),(3918263,'192.168.6.55'),(3918265,'192.168.6.56'),(3918267,'192.168.6.57'),(3918269,'192.168.6.58'),(3918271,'192.168.6.59'),(3918165,'192.168.6.6'),(3918273,'192.168.6.60'),(3918275,'192.168.6.61'),(3918277,'192.168.6.62'),(3918279,'192.168.6.63'),(3918281,'192.168.6.64'),(3918283,'192.168.6.65'),(3918285,'192.168.6.66'),(3918287,'192.168.6.67'),(3918289,'192.168.6.68'),(3918291,'192.168.6.69'),(3918167,'192.168.6.7'),(3918293,'192.168.6.70'),(3918295,'192.168.6.71'),(3918297,'192.168.6.72'),(3918299,'192.168.6.73'),(3918301,'192.168.6.74'),(3918303,'192.168.6.75'),(3918305,'192.168.6.76'),(3918307,'192.168.6.77'),(3918309,'192.168.6.78'),(3918311,'192.168.6.79'),(3918169,'192.168.6.8'),(3918313,'192.168.6.80'),(3918315,'192.168.6.81'),(3918317,'192.168.6.82'),(3918319,'192.168.6.83'),(3918321,'192.168.6.84'),(3918323,'192.168.6.85'),(3918325,'192.168.6.86'),(3918327,'192.168.6.87'),(3918329,'192.168.6.88'),(3918331,'192.168.6.89'),(3918171,'192.168.6.9'),(3918333,'192.168.6.90'),(3918335,'192.168.6.91'),(3918337,'192.168.6.92'),(3918339,'192.168.6.93'),(3918341,'192.168.6.94'),(3918343,'192.168.6.95'),(3918345,'192.168.6.96'),(3918347,'192.168.6.97'),(3918349,'192.168.6.98'),(3918351,'192.168.6.99'),(3918154,'192.168.7.0'),(3918156,'192.168.7.1'),(3918174,'192.168.7.10'),(3918354,'192.168.7.100'),(3918356,'192.168.7.101'),(3918358,'192.168.7.102'),(3918360,'192.168.7.103'),(3918362,'192.168.7.104'),(3918364,'192.168.7.105'),(3918366,'192.168.7.106'),(3918368,'192.168.7.107'),(3918370,'192.168.7.108'),(3918372,'192.168.7.109'),(3918176,'192.168.7.11'),(3918374,'192.168.7.110'),(3918376,'192.168.7.111'),(3918378,'192.168.7.112'),(3918380,'192.168.7.113'),(3918382,'192.168.7.114'),(3918384,'192.168.7.115'),(3918386,'192.168.7.116'),(3918388,'192.168.7.117'),(3918390,'192.168.7.118'),(3918392,'192.168.7.119'),(3918178,'192.168.7.12'),(3918394,'192.168.7.120'),(3918396,'192.168.7.121'),(3918398,'192.168.7.122'),(3918400,'192.168.7.123'),(3918402,'192.168.7.124'),(3918404,'192.168.7.125'),(3918406,'192.168.7.126'),(3918408,'192.168.7.127'),(3918410,'192.168.7.128'),(3918412,'192.168.7.129'),(3918180,'192.168.7.13'),(3918414,'192.168.7.130'),(3918416,'192.168.7.131'),(3918418,'192.168.7.132'),(3918420,'192.168.7.133'),(3918422,'192.168.7.134'),(3918424,'192.168.7.135'),(3918426,'192.168.7.136'),(3918428,'192.168.7.137'),(3918430,'192.168.7.138'),(3918432,'192.168.7.139'),(3918182,'192.168.7.14'),(3918434,'192.168.7.140'),(3918436,'192.168.7.141'),(3918438,'192.168.7.142'),(3918440,'192.168.7.143'),(3918442,'192.168.7.144'),(3918444,'192.168.7.145'),(3918446,'192.168.7.146'),(3918448,'192.168.7.147'),(3918450,'192.168.7.148'),(3918452,'192.168.7.149'),(3918184,'192.168.7.15'),(3918454,'192.168.7.150'),(3918456,'192.168.7.151'),(3918458,'192.168.7.152'),(3918460,'192.168.7.153'),(3918462,'192.168.7.154'),(3918464,'192.168.7.155'),(3918466,'192.168.7.156'),(3918468,'192.168.7.157'),(3918470,'192.168.7.158'),(3918472,'192.168.7.159'),(3918186,'192.168.7.16'),(3918474,'192.168.7.160'),(3918476,'192.168.7.161'),(3918478,'192.168.7.162'),(3918480,'192.168.7.163'),(3918482,'192.168.7.164'),(3918484,'192.168.7.165'),(3918486,'192.168.7.166'),(3918488,'192.168.7.167'),(3918490,'192.168.7.168'),(3918492,'192.168.7.169'),(3918188,'192.168.7.17'),(3918494,'192.168.7.170'),(3918496,'192.168.7.171'),(3918498,'192.168.7.172'),(3918500,'192.168.7.173'),(3918502,'192.168.7.174'),(3918504,'192.168.7.175'),(3918506,'192.168.7.176'),(3918508,'192.168.7.177'),(3918510,'192.168.7.178'),(3918512,'192.168.7.179'),(3918190,'192.168.7.18'),(3918514,'192.168.7.180'),(3918516,'192.168.7.181'),(3918518,'192.168.7.182'),(3918520,'192.168.7.183'),(3918522,'192.168.7.184'),(3918524,'192.168.7.185'),(3918526,'192.168.7.186'),(3918528,'192.168.7.187'),(3918530,'192.168.7.188'),(3918532,'192.168.7.189'),(3918192,'192.168.7.19'),(3918534,'192.168.7.190'),(3918536,'192.168.7.191'),(3918538,'192.168.7.192'),(3918540,'192.168.7.193'),(3918542,'192.168.7.194'),(3918544,'192.168.7.195'),(3918546,'192.168.7.196'),(3918548,'192.168.7.197'),(3918550,'192.168.7.198'),(3918552,'192.168.7.199'),(3918158,'192.168.7.2'),(3918194,'192.168.7.20'),(3918554,'192.168.7.200'),(3918556,'192.168.7.201'),(3918558,'192.168.7.202'),(3918560,'192.168.7.203'),(3918562,'192.168.7.204'),(3918564,'192.168.7.205'),(3918566,'192.168.7.206'),(3918568,'192.168.7.207'),(3918570,'192.168.7.208'),(3918572,'192.168.7.209'),(3918196,'192.168.7.21'),(3918574,'192.168.7.210'),(3918576,'192.168.7.211'),(3918578,'192.168.7.212'),(3918580,'192.168.7.213'),(3918582,'192.168.7.214'),(3918584,'192.168.7.215'),(3918586,'192.168.7.216'),(3918588,'192.168.7.217'),(3918590,'192.168.7.218'),(3918592,'192.168.7.219'),(3918198,'192.168.7.22'),(3918594,'192.168.7.220'),(3918596,'192.168.7.221'),(3918598,'192.168.7.222'),(3918600,'192.168.7.223'),(3918602,'192.168.7.224'),(3918604,'192.168.7.225'),(3918606,'192.168.7.226'),(3918608,'192.168.7.227'),(3918610,'192.168.7.228'),(3918612,'192.168.7.229'),(3918200,'192.168.7.23'),(3918614,'192.168.7.230'),(3918616,'192.168.7.231'),(3918618,'192.168.7.232'),(3918620,'192.168.7.233'),(3918622,'192.168.7.234'),(3918624,'192.168.7.235'),(3918626,'192.168.7.236'),(3918628,'192.168.7.237'),(3918630,'192.168.7.238'),(3918632,'192.168.7.239'),(3918202,'192.168.7.24'),(3918634,'192.168.7.240'),(3918636,'192.168.7.241'),(3918638,'192.168.7.242'),(3918640,'192.168.7.243'),(3918642,'192.168.7.244'),(3918644,'192.168.7.245'),(3918646,'192.168.7.246'),(3918648,'192.168.7.247'),(3918650,'192.168.7.248'),(3918652,'192.168.7.249'),(3918204,'192.168.7.25'),(3918654,'192.168.7.250'),(3918656,'192.168.7.251'),(3918658,'192.168.7.252'),(3918660,'192.168.7.253'),(3918662,'192.168.7.254'),(3918206,'192.168.7.26'),(3918208,'192.168.7.27'),(3918210,'192.168.7.28'),(3918212,'192.168.7.29'),(3918160,'192.168.7.3'),(3918214,'192.168.7.30'),(3918216,'192.168.7.31'),(3918218,'192.168.7.32'),(3918220,'192.168.7.33'),(3918222,'192.168.7.34'),(3918224,'192.168.7.35'),(3918226,'192.168.7.36'),(3918228,'192.168.7.37'),(3918230,'192.168.7.38'),(3918232,'192.168.7.39'),(3918162,'192.168.7.4'),(3918234,'192.168.7.40'),(3918236,'192.168.7.41'),(3918238,'192.168.7.42'),(3918240,'192.168.7.43'),(3918242,'192.168.7.44'),(3918244,'192.168.7.45'),(3918246,'192.168.7.46'),(3918248,'192.168.7.47'),(3918250,'192.168.7.48'),(3918252,'192.168.7.49'),(3918164,'192.168.7.5'),(3918254,'192.168.7.50'),(3918256,'192.168.7.51'),(3918258,'192.168.7.52'),(3918260,'192.168.7.53'),(3918262,'192.168.7.54'),(3918264,'192.168.7.55'),(3918266,'192.168.7.56'),(3918268,'192.168.7.57'),(3918270,'192.168.7.58'),(3918272,'192.168.7.59'),(3918166,'192.168.7.6'),(3918274,'192.168.7.60'),(3918276,'192.168.7.61'),(3918278,'192.168.7.62'),(3918280,'192.168.7.63'),(3918282,'192.168.7.64'),(3918284,'192.168.7.65'),(3918286,'192.168.7.66'),(3918288,'192.168.7.67'),(3918290,'192.168.7.68'),(3918292,'192.168.7.69'),(3918168,'192.168.7.7'),(3918294,'192.168.7.70'),(3918296,'192.168.7.71'),(3918298,'192.168.7.72'),(3918300,'192.168.7.73'),(3918302,'192.168.7.74'),(3918304,'192.168.7.75'),(3918306,'192.168.7.76'),(3918308,'192.168.7.77'),(3918310,'192.168.7.78'),(3918312,'192.168.7.79'),(3918170,'192.168.7.8'),(3918314,'192.168.7.80'),(3918316,'192.168.7.81'),(3918318,'192.168.7.82'),(3918320,'192.168.7.83'),(3918322,'192.168.7.84'),(3918324,'192.168.7.85'),(3918326,'192.168.7.86'),(3918328,'192.168.7.87'),(3918330,'192.168.7.88'),(3918332,'192.168.7.89'),(3918172,'192.168.7.9'),(3918334,'192.168.7.90'),(3918336,'192.168.7.91'),(3918338,'192.168.7.92'),(3918340,'192.168.7.93'),(3918342,'192.168.7.94'),(3918344,'192.168.7.95'),(3918346,'192.168.7.96'),(3918348,'192.168.7.97'),(3918350,'192.168.7.98'),(3918352,'192.168.7.99');
/*!40000 ALTER TABLE `rede` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `smtp`
--

DROP TABLE IF EXISTS `smtp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `smtp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `smtpserver` varchar(255) NOT NULL,
  `smtpporta` int(11) NOT NULL,
  `smtplogin` varchar(255) NOT NULL,
  `smtpemail` varchar(255) NOT NULL,
  `smtpsenha` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `smtp`
--

LOCK TABLES `smtp` WRITE;
/*!40000 ALTER TABLE `smtp` DISABLE KEYS */;
INSERT INTO `smtp` VALUES (1,'smtp.googlemail.com',587,'email@gmail.com','email@gmail.com','senha');
/*!40000 ALTER TABLE `smtp` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-01-21 19:16:26