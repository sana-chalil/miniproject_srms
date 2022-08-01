/*
SQLyog Trial v13.1.8 (64 bit)
MySQL - 5.6.12-log : Database - srms
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`srms` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `srms`;

/*Table structure for table `course` */

DROP TABLE IF EXISTS `course`;

CREATE TABLE `course` (
  `course_id` INT(20) NOT NULL,
  `course_name` VARCHAR(20) DEFAULT NULL,
  `duration` VARCHAR(10) DEFAULT NULL,
  `chapters` INT(10) DEFAULT NULL,
  `description` VARCHAR(100) DEFAULT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=INNODB DEFAULT CHARSET=latin1;

/*Data for the table `course` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` INT(10) NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(15) DEFAULT NULL,
  `password` VARCHAR(30) DEFAULT NULL,
  `type` VARCHAR(10) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=INNODB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

INSERT  INTO `login`(`login_id`,`username`,`password`,`type`) VALUES
(1,'a','a','admin'),
(2,'b','b','student');

/*Table structure for table `result` */

DROP TABLE IF EXISTS `result`;

CREATE TABLE `result` (
  `roll_no` INT(10) NOT NULL,
  `student_name` VARCHAR(20) DEFAULT NULL,
  `course_name` VARCHAR(20) DEFAULT NULL,
  `mark_obtained` INT(10) DEFAULT NULL,
  `total_mark` INT(10) DEFAULT NULL,
  `percentage` VARCHAR(10) DEFAULT NULL,
  PRIMARY KEY (`roll_no`)
) ENGINE=INNODB DEFAULT CHARSET=latin1;

/*Data for the table `result` */

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `roll_no` INT(10) NOT NULL,
  `student_name` VARCHAR(20) DEFAULT NULL,
  `date_of_birth` VARCHAR(10) DEFAULT NULL,
  `contact_no` INT(20) DEFAULT NULL,
  `course_name` VARCHAR(20) DEFAULT NULL,
  PRIMARY KEY (`roll_no`)
) ENGINE=INNODB DEFAULT CHARSET=latin1;

/*Data for the table `student` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
