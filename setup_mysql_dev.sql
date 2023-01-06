-- Write a script that prepares a MySQL server for the projec
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
    IDENTIFIED BY 'hbnb_dev_pwd';
-- permission for hbnb_dev_db
GRANT ALL
    ON `hbnb_dev_db`.*
    TO 'hbnb_dev'@'localhost';
-- permission for performance schema
GRANT SELECT
    ON `performance_schema`.*
    TO 'hbnb_dev'@'localhost';
