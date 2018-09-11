-- from juliensimon-aws/athena/gdelt/create_tables.txt
-- but adapted to MySQL

CREATE TABLE IF NOT EXISTS gdelt.eventcodes (`code` varchar(4),`description` varchar(100)) ;

CREATE TABLE IF NOT EXISTS gdelt.types (`type` varchar(4),`description` varchar(100));

CREATE TABLE IF NOT EXISTS gdelt.groups (`group` varchar(4),`description` varchar(100));

CREATE TABLE IF NOT EXISTS gdelt.countries (`code` varchar(4),`country` varchar(100));
