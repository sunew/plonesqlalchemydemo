# run me with mysql --force -u root -p < setup.sql

CREATE DATABASE zitelabtest;

CREATE USER 'zitelab'@'localhost' IDENTIFIED BY 'AwaymWad0';
GRANT SELECT, UPDATE, INSERT, DELETE, EXECUTE, SHOW VIEW, CREATE, ALTER, INDEX, CREATE VIEW, CREATE TEMPORARY TABLES
ON zitelabtest.* TO 'zitelab'@'localhost';

FLUSH PRIVILEGES;
