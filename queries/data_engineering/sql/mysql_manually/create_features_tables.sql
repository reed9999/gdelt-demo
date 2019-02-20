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


CREATE TABLE dyad_events_by_year
    (year int, 
    actor1code text, 
    actor2code text, 
    eventcode text,
    eventbasecode text,  
    eventrootcode text, 
    goldsteinscale float, 
    event_count int);

