#!/bin/sh
prefix=./mysql_backup/zitelab
suffix=$(date +%Y%m%d-%H%M%S)
filename=$prefix.$suffix
echo $filename
mysqldump -uroot -p --single-transaction zitelabtest > $filename


