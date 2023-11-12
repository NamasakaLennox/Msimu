-- Prepares the server for the project
-- create database if not exists
CREATE DATABASE IF NOT EXISTS msimu_dev_db;

-- create new user for the project
CREATE USER IF NOT EXISTS 'msimu_dev'@'localhost' IDENTIFIED BY 'msimu_dev_pwd';
GRANT ALL PRIVILEGES ON msimu_dev_db.* TO 'msimu_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'msimu_dev'@'localhost';
