-- create_features_tables.sql
-- DRY VIOLATION
-- This is now the third different place where the schema for these tables lives. The others are:
-- * in the Hive scripts
-- * in the pandas_gdelt_helper.py code itself.
-- One way to remedy this would be a good migrations library, e.g. Django's.
-- Another, less desirable, is to homebrew the generation of all three occurrences from one 
-- canonical source.

-- This directory is called mysql_manually because it's SQL I can manually paste in MySQL workbench
-- or load via stdin on the command prompt.


DROP TABLE IF EXISTS dyad_events_by_year;
CREATE TABLE dyad_events_by_year
    (
    year int,
    actor1code text,
    actor2code text,
    eventcode text,
    eventbasecode text,
    eventrootcode text,
    goldsteinscale float,
    event_count int,
    -- Not sure an id column adds value, but any cost should be negligible.
    -- making it last may help with import: https://stackoverflow.com/questions/2463542
    id int NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (id)	
    );

-- The problem here is that it's a "tab-delimited" CSV file that resulted from my HiveQL, but it's not a 
-- tab character that MySQL recognizes as \t.

-- https://stackoverflow.com/q/6017032
-- LOAD DATA LOCAL INFILE '<whatever>/000000_0.csv'
LOAD DATA LOCAL INFILE '<whatever>/dyad_features_by_year/tiny1.csv'
INTO TABLE dyad_events_by_year
FIELDS TERMINATED BY '^A' 
-- These should be default
ENCLOSED BY '' ESCAPED BY '\\'
LINES TERMINATED BY '\n' STARTING BY ''
(
    year,
    actor1code,
    actor2code,
    eventcode,
    eventbasecode,
    eventrootcode,
    goldsteinscale,
    event_count
    )
SET id = NULL;

SELECT * FROM dyad_events_by_year WHERE actor1code = 'AFR';