-- Script that create a table where the column id is initialized to 1 per default
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,
    name VARCHAR(256)
);