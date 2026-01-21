-- Script that create a table where the column name can't be NULL
CREATE TABLE IF NOT EXISTS `force_name`(
    id INT,
    name VARCHAR(256) NOT NULL
);
