#!/bin/bash
# To get this to work, I had to whitelist the relevant directories in AppArmor
# https://stackoverflow.com/questions/2783313/
# But it still fails with: 
# ERROR 1366 (HY000) at line 2: Incorrect integer value: '' for column 
#    'actor1geo_type' at row 1
# Reluctantly I'm going to set aside this attempt at automation for the moment.

MYSQL_SCRIPT="__temp_import.sql"
echo " The script is $MYSQL_SCRIPT"
[ -e $MYSQL_SCRIPT ] && rm $MYSQL_SCRIPT
echo "USE gdelt;" > "$MYSQL_SCRIPT"

#This feels horrible but is needed because the NULLs are in there as ''
#It's also not needed; why did my table creation (with VARCHARs) not stick?
# echo "ALTER TABLE events MODIFY actor1geo_type VARCHAR(10) NULL;" >> "$MYSQL_SCRIPT"
# echo "ALTER TABLE events MODIFY actor2geo_type VARCHAR(10) NULL;" >> "$MYSQL_SCRIPT"
# echo "ALTER TABLE events MODIFY actiongeo_type VARCHAR(10) NULL;" >> "$MYSQL_SCRIPT"
# echo "ALTER TABLE events MODIFY actiongeo_featureid VARCHAR(10) NULL;" >> "$MYSQL_SCRIPT"

for f in `ls /home/philip/Documents/aws-project/gdelt-data/original/events/*.csv`;
do
    #Using mysqlimport is too much of a mess because table names have to be the same.
    echo "LOAD DATA INFILE '$f' INTO TABLE events;" >> $MYSQL_SCRIPT
done;

PROMPT_FOR_PASSWORD="" #or -p
mysql -uroot $PROMPT_FOR_PASSWORD < $MYSQL_SCRIPT
# rm $MYSQL_SCRIPT
