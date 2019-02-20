# Despite the name of this file, there was a lot of manual work in setting
# up MySQL that I haven't retrofitted to automation.
# This is incomplete because of permissions issues preventing me from using
# mysqlimport effectively.
# (But I can use the MySQL Workbench GUI for now.)

### Let's organize this a bit. We could prompt for each of these option, use a command-line switch,
# or read them from a file.
LOAD_LOOKUP_TABLES='F'
LOAD_FEATURES_TABLES='T'

if [[ 'T' == $LOAD_LOOKUP_TABLES ]] ; then

    ### MANUAL: Loaded a subset of data to gdelt.events.
    MYSQL_HOSTNAME=gdelt.cjmls0qwqxeg.us-west-2.rds.amazonaws.com
    MYSQL_USER=philip
    mysql -h $MYSQL_HOSTNAME -u $MYSQL_USER -p < load-lookup-tables.sql

    ## eventcodes already done
    array=(countries groups types)
    for CURRENT_TABLE in "${array[@]}"
    do
        
        cp ../juliensimon-aws/athena/gdelt/$CURRENT_TABLE.txt ~/temp/$CURRENT_TABLE.csv
        mysqlimport -h $MYSQL_HOSTNAME -u $MYSQL_USER -p ~/temp/$CURRENT_TABLE.csv

# This won't work until I solve this problem, which for now I can
# just leave unsolved:
#mysqlimport -h gdelt.cjmls0qwqxeg.us-west-2.rds.amazonaws.com -u philip -p gdelt ~/temp/countries.csv --verbose
# 
# Loading data from SERVER file: /home/philip/temp/countries.csv into countries
# mysqlimport: Error: 1045, Access denied for user 'philip'@'%' (using password: YES), when using table: countries
    done
fi;

if [[ 'T' == $LOAD_FEATURES_TABLES ]] ; then
    echo "Loading features tables...."
    mysql -h $MYSQL_HOSTNAME -u $MYSQL_USER -p < load-features-tables.sql
fi;
