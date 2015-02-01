#!/bin/sh

# first drop the schema plonesqldemo manually if needed to refresh.
mysql --force -u root -p < mysql_scripts/setup.sql
