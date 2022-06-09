CREATE SCHEMA `WORDS_IN_PAGES_DB` ;

CREATE TABLE `WORDS_IN_PAGES_DB`.`words_in_pages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `word` VARCHAR(45) NOT NULL,
  `page_num` INT NOT NULL,
  `date_created` DATETIME NOT NULL,
  PRIMARY KEY (`id`));


/* stored procedures */
USE `WORDS_IN_PAGES_DB`;
DROP procedure IF EXISTS `add_word`;

DELIMITER $$
USE `WORDS_IN_PAGES_DB`$$
CREATE PROCEDURE `add_word` (IN `word` VARCHAR(50), IN `pageNum` INT)  NO SQL
BEGIN
SET SQL_SAFE_UPDATES=0;
	INSERT  INTO words_in_pages (word, page_num, date_created)
	VALUES (word, pageNum, CURDATE());
    SET SQL_SAFE_UPDATES=1;
END$$

DELIMITER ;


USE `WORDS_IN_PAGES_DB`;
DROP procedure IF EXISTS `get_pages_with_words`;

DELIMITER $$
USE `WORDS_IN_PAGES_DB`$$
CREATE  PROCEDURE `get_pages_with_words` (IN `words` VARCHAR(5000))
BEGIN
SELECT page_num
	FROM words_in_pages
    WHERE FIND_IN_SET(word, words);
END$$

DELIMITER $$
USE `WORDS_IN_PAGES_DB`$$
CREATE  PROCEDURE `get_all_words` (IN `words` VARCHAR(5000))
BEGIN
SELECT *
	FROM words_in_pages
    WHERE FIND_IN_SET(word, words);
END$$



DELIMITER ;

