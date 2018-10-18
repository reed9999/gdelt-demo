-- Continuing with the idea behind dyad_classification_features.sql, 
-- let's continue extracting some interesting counts and aggregations
-- at the country level.

USE gdelt;

--------------------------------------------------------------------------------
-- Extraction #1: Similar to the relationships in country_features but by year. 

DROP TABLE IF EXISTS country_features_by_year;
CREATE TABLE IF NOT EXISTS country_features_by_year AS
	(SELECT c.country, c.code, 
		count(df1.actor2code)) as actor1_relationships, 
	(SELECT count(*) 
		FROM dyad_events_by_year AS de1 
		WHERE de1.actor2code = c.code) as actor2_relationships
	FROM countries c 
	LEFT JOIN dyad_events_by_year AS de1 ON c.code = de1.actor1code
	GROUP BY c.country, c.code;

-- SELECT year, actor1code, actor2code, eventcode, 
-- -- I don't see why I can't join on a group field but for for now this throws an error.
-- -- eventcodes.description,
-- eventbasecode,  eventrootcode, goldsteinscale, count(*) as count_events
-- FROM events LEFT JOIN eventcodes
--   ON eventcodes.code = events.eventcode
-- GROUP BY year, actor1code, actor2code, eventcode,
-- -- these should be 1-to-1 with eventcode. Not sure if they would degrade performance or not.
-- eventbasecode,  eventrootcode, goldsteinscale
-- ;

-- --------------------------------------------------------------------------------
-- -- Extraction #2: 
-- -- some features that might characterize individual dyads across all of time. 

-- CREATE TABLE IF NOT EXISTS dyad_features AS
-- SELECT a.actor1code, a.actor2code, 
-- 	count(*) as count_aoeventcodes, sum(a.count_events) as sum_events
-- FROM dyad_events_by_year AS a
-- GROUP BY a.actor1code, actor2code;

-- -- And the third order table, which has a second query.
-- -- Earlier I was introducing bugs by doing the three-way join and 

-- CREATE TABLE IF NOT EXISTS country_features AS
-- 	SELECT c.country, c.code, 
-- 		count(df1.actor2code) as actor1_relationships, 
-- 		(SELECT count(*) 
-- 		FROM dyad_features AS df2 
-- 		WHERE df2.actor2code = c.code) as actor2_relationships
-- 	FROM countries c 
-- 	LEFT JOIN dyad_features AS df1 ON c.code = df1.actor1code
-- 	GROUP BY c.country, c.code;

-- -- To write to an arbitrary location, we need to set
-- --     secure_file_priv=""
-- -- e.g. in /etc/mysql/mysql.conf.d/mysqld.cnf on Ubuntu.
-- -- We also need to GRANT the privilege FILE on gdelt, I think.
-- -- Otherwise, set all directories to "/var/lib/mysql-files/"
-- -- which is what it's doing for the moment.

-- -- Alternatively I could also just load MySQL directly into pandas.

-- select * FROM dyad_events_by_year
-- -- 	INTO OUTFILE "/home/philip/aws/demo/data-related/features/dyad_events_by_year.csv"
-- 	INTO OUTFILE "/var/lib/mysql-files/dyad_events_by_year.csv"
-- 	FIELDS TERMINATED BY "\t"
-- 	ENCLOSED BY '"'
-- 	LINES TERMINATED BY "\n";
-- select * FROM dyad_features
-- 	INTO OUTFILE "/var/lib/mysql-files/dyad_features.csv"
-- 	FIELDS TERMINATED BY "\t"
-- 	ENCLOSED BY '"'
-- 	LINES TERMINATED BY "\n";
-- select * FROM country_features 
-- 	INTO OUTFILE "/var/lib/mysql-files/country_features.csv"
-- 	FIELDS TERMINATED BY "\t"
-- 	ENCLOSED BY '"'
-- 	LINES TERMINATED BY "\n";
    
