#!/bin/bash

# I thought: 
# Using mysqlimport is too much of a mess because table names have to be the same.
# but it may be worth trying...

# To get this to work, I had to whitelist the relevant directories in AppArmor
# https://stackoverflow.com/q/2783313/
# It still fails with 
# ERROR 1261 (01000) at line 2: Row 1 doesn't contain data for all columns
# See https://stackoverflow.com/q/42966931/
# None of those solutions works; all that does is to actually add extra tab
# characters. There's probably some reasonable way to do this with sed but 
# let's brainstorm something else.


MYSQL_SCRIPT="__temp_import.sql"
echo " The script is $MYSQL_SCRIPT"
[ -e $MYSQL_SCRIPT ] && rm $MYSQL_SCRIPT
echo "USE gdelt;" > "$MYSQL_SCRIPT"

EVENTS_DIR=/home/philip/Documents/aws-project/gdelt-data/trivial
# EVENTS_DIR=/home/philip/Documents/aws-project/gdelt-data/original/events
for f in `ls $EVENTS_DIR/*.csv`;
do
    echo "LOAD DATA INFILE '$f' INTO TABLE events FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n';" >> $MYSQL_SCRIPT
    # mysqlimport...
done;

PROMPT_FOR_PASSWORD="" #or -p
# mysql -uroot $PROMPT_FOR_PASSWORD < $MYSQL_SCRIPT
# rm $MYSQL_SCRIPT
