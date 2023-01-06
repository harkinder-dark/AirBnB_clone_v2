--Write a script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
    IDENTIFIED BY 'hbnb_test_pwd';
-- permission for hbnb_dev_db
GRANT ALL
    ON `hbnb_test_db`.*
    TO 'hbnb_test'@'localhost';
-- permission for performance schema
GRANT SELECT
    ON `performance_schema`.*
    TO 'hbnb_test'@'localhost';
