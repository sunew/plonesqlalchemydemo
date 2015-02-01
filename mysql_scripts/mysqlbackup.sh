#!/bin/sh
prefix=./mysql_backup/plonesqldemo
suffix=$(date +%Y%m%d-%H%M%S)
filename=$prefix.$suffix
echo $filename
mysqldump -uroot -p --single-transaction plonesqldemo > $filename
