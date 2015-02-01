# run me with mysql --force -u root -p < setup.sql

CREATE DATABASE plonesqldemo;

CREATE USER 'plonesqldemo'@'localhost' IDENTIFIED BY 'AwaymWad0';
GRANT SELECT, UPDATE, INSERT, DELETE, EXECUTE, SHOW VIEW, CREATE, ALTER, INDEX, CREATE VIEW, CREATE TEMPORARY TABLES
ON plonesqldemo.* TO 'plonesqldemo'@'localhost';

FLUSH PRIVILEGES;
