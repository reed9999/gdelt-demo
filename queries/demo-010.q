-- demo-010.q

-- I'm just curious if this one works from DynamoDB

-- CREATE EXTERNAL TABLE IF NOT EXISTS gdelt_events (
--   `globaleventid` INT,`day` INT,`monthyear` INT,`year` INT,`fractiondate` FLOAT,
--   `actor1code` string,`actor1name` string,`actor1countrycode` string,`actor1knowngroupcode` string,
--   `actor1ethniccode` string,`actor1religion1code` string,`actor1religion2code` string,
--   `actor1type1code` string,`actor1type2code` string,`actor1type3code` string,
--   `actor2code` string,`actor2name` string,`actor2countrycode` string,`actor2knowngroupcode` string,
--   `actor2ethniccode` string,`actor2religion1code` string,`actor2religion2code` string,
--   `actor2type1code` string,`actor2type2code` string,`actor2type3code` string,
--   `isrootevent` BOOLEAN,`eventcode` string,`eventbasecode` string,`eventrootcode` string,
--   `quadclass` INT,`goldsteinscale` FLOAT,`nummentions` INT,`numsources` INT,`numarticles` INT,`avgtone` FLOAT,
--   `actor1geo_type` INT,`actor1geo_fullname` string,`actor1geo_countrycode` string,`actor1geo_adm1code` string,
--   `actor1geo_lat` FLOAT,`actor1geo_long` FLOAT,`actor1geo_featureid` INT,
--   `actor2geo_type` INT,`actor2geo_fullname` string,`actor2geo_countrycode` string,`actor2geo_adm1code` string,
--   `actor2geo_lat` FLOAT,`actor2geo_long` FLOAT,`actor2geo_featureid` INT,
--   `actiongeo_type` INT,`actiongeo_fullname` string,`actiongeo_countrycode` string,`actiongeo_adm1code` string,
--   `actiongeo_lat` FLOAT,`actiongeo_long` FLOAT,`actiongeo_featureid` INT,
--   `dateadded` INT,`sourceurl` string)
-- LOCATION 's3://philip-hadoop-bucket/data/';


----

CREATE EXTERNAL TABLE IF NOT EXISTS
demands_by_actor_pair
-- (`actor1code` string,
--   `actor2code` string,
-- `count_demands` int)
AS SELECT actor1code, actor2code, count(*)
FROM gdelt_events
WHERE eventcode LIKE "10%"
GROUP BY actor1code, actor2code;

CREATE EXTERNAL TABLE  IF NOT EXISTS old_new_demands
-- (`actor1code` string,
--   `actor2code` string,
-- `period_1_demands` int,
-- `period_2_demands` int,
-- )
AS SELECT actor1code, actor2code, count(*), NULL
FROM gdelt_events
WHERE eventcode LIKE "10%"
AND year < 1999
GROUP BY actor1code, actor2code;

-- TODO: Then insert into the table the period 2 demands column.

INSERT OVERWRITE DIRECTORY '${OUTPUT}/old_new_demands/'
SELECT * FROM old_new_demands;
