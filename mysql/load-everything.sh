# Despite the name of this file, there was a lot of manual work in setting
# up MySQL that I haven't retrofitted to automation.
# This is incomplete because of permissions issues preventing me from using
# mysqlimport effectively.
# (But I can use the MySQL Workbench GUI for now.)

### MANUAL: Loaded a subset of data to gdelt.events.
MYSQL_HOSTNAME=gdelt2.cjmls0qwqxeg.us-west-2.rds.amazonaws.com
MYSQL_USER=philip
mysql -h $MYSQL_HOSTNAME -u $MYSQL_USER -p \
  < load-lookup-tables.sql

## Obviously DRY indicates we should loop through this.
## eventcodes already done
CURRENT_TABLE=countries
cp ../juliensimon-aws/athena/gdelt/$CURRENT_TABLE.txt ~/temp/$CURRENT_TABLE.csv
mysqlimport -h $MYSQL_HOSTNAME -u $MYSQL_USER -p ~/temp/$CURRENT_TABLE.csv
#
# and then...
CURRENT_TABLE=groups
# ...
CURRENT_TABLE=types
# ... etc. But looping is better of course.

#However it doesn't matter until I solve this problem, which for now I can
# just leave unsolved:
#mysqlimport -h gdelt2.cjmls0qwqxeg.us-west-2.rds.amazonaws.com -u philip -p gdelt ~/temp/countries.csv --verbose
# 
# Loading data from SERVER file: /home/philip/temp/countries.csv into countries
# mysqlimport: Error: 1045, Access denied for user 'philip'@'%' (using password: YES), when using table: countries
