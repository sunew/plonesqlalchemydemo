#!/bin/sh

# first drop the schema zitelabtest manually.
mysql --force -u root -p < mysql_scripts/setup.sql
