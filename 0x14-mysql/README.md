# 0x14. MySQL 

<p align="center">
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/280/KkrkDHT.png"
</p>

## Resource

- [What is a database](https://searchdatamanagement.techtarget.com/definition/database)
- [What is a database primary/replicate cluster](https://www.digitalocean.com/community/tutorials/how-to-choose-a-redundancy-plan-to-ensure-high-availability#sql-replication)
- [MySQL primary/replicate setup](https://www.digitalocean.com/community/tutorials/how-to-set-up-replication-in-mysql)
- [Build a robust database backup strategy](https://www.databasejournal.com/ms-sql/developing-a-sql-server-backup-strategy/)
- [Privileges Provided by MySQL](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_replication-client) (***Replication Client***)
- [Creating User for Replication](https://dev.mysql.com/doc/refman/8.0/en/replication-howto-repuser.html)
- [Setting up replicas](https://dev.mysql.com/doc/refman/5.7/en/replication-setup-replicas.html) (***MySQL 5.7.x***)

## Tasks

<details>
<summary>0. Install MySQL</summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/wMPwtg5K/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary>1. Let us in!</summary><br>

<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/zB1QFncd/image.png' border='0' alt='image'/></a>
```sh
mysql> CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
mysql> GRANT REPLICATION CLIENT ON *.* to 'holberton_user'@'localhost';
mysql> FLUSH PRIVILEGES;
```

</details>

<details>
<summary>2. If only you could see what I've seen with your eyes</summary><br>

<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/sgDm766T/image.png' border='0' alt='image'/></a>
```sh
mysql> CREATE DATABASE tyrell_corp;
mysql> USE tyrell_corp;
mysql> CREATE TABLE nexus6 (id INT, name VARCHAR(256));
mysql> INSERT INTO nexus6 (id, name) VALUES ('1', 'Leon');
mysql> GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
```

</details>

<details>
<summary>3. Quite an experience to live in fear, isn't it?</summary><br>

<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/D0CmW3vT/image.png' border='0' alt='image'/></a>
```sh
msql> CREATE USER 'replica_user'@'%' IDENTIFIED BY 'password';
mysql> GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
mysql> GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
```

</details>

<details>
<summary>4. Setup a Primary-Replica infrastructure using MySQL</summary><br>

<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/MKBBLGVn/09e83e914f0d6865ce320a47f2f14837a5b190b6.gif' border='0' alt='09e83e914f0d6865ce320a47f2f14837a5b190b6'/></a>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/9fkyDg7k/image.png' border='0' alt='image'/></a>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/Jhhb4DpP/image.png' border='0' alt='image'/></a>
<a href='https://postimg.cc/4nLx8dpx' target='_blank'><img src='https://i.postimg.cc/28mLSL6h/image.png' border='0' alt='image'/></a>

+ [MySQL primary configuration](./4-mysql_configuration_primary)
+ [MySQL replica configuration](./4-mysql_configuration_replica)

</details>

<details>
<summary>5. MySQL backup</summary><br>

[![IMAGE ALT TEXT HERE](https://i.postimg.cc/3NtKg0gR/verizon.jpg)](https://www.youtube.com/watch?v=ANU-oSE5_hU)
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/J7YV5LfG/image.png' border='0' alt='image'/></a>

```sh
ubuntu@03-web-01:~$ ls
5-mysql_backup
ubuntu@03-web-01:~$ ./5-mysql_backup mydummypassword
backup.sql
ubuntu@03-web-01:~$ ls
01-03-2017.tar.gz  5-mysql_backup  backup.sql
ubuntu@03-web-01:~$ more backup.sql
-- MySQL dump 10.13  Distrib 5.7.25, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database:
-- ------------------------------------------------------
-- Server version   5.7.25-0ubuntu0.14.04.1

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
-- Current Database: `tyrell_corp`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `tyrell_corp` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `tyrell_corp`;

--
-- Table structure for table `nexus6`
--

DROP TABLE IF EXISTS `nexus6`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nexus6` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `firstname` varchar(30) NOT NULL,
  `lastname` varchar(30) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `reg_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
ubuntu@03-web-01:~$
ubuntu@03-web-01:~$ file 01-03-2017.tar.gz
01-03-2017.tar.gz: gzip compressed data, from Unix, last modified: Wed Mar  1 23:38:09 2017
ubuntu@03-web-01:~$
```

+ [Backup script](./5-mysql_backup)

</details>
