-- Continuing my adaptation of this script:
-- http://blog.julien.org/2017/03/exploring-gdelt-data-set-with-amazon.html

CREATE EXTERNAL TABLE IF NOT EXISTS gdelt_events (
  `globaleventid` INT,`day` INT,`monthyear` INT,`year` INT,`fractiondate` FLOAT,
  `actor1code` string,`actor1name` string,`actor1countrycode` string,`actor1knowngroupcode` string,
  `actor1ethniccode` string,`actor1religion1code` string,`actor1religion2code` string,
  `actor1type1code` string,`actor1type2code` string,`actor1type3code` string,
  `actor2code` string,`actor2name` string,`actor2countrycode` string,`actor2knowngroupcode` string,
  `actor2ethniccode` string,`actor2religion1code` string,`actor2religion2code` string,
  `actor2type1code` string,`actor2type2code` string,`actor2type3code` string,
  `isrootevent` BOOLEAN,`eventcode` string,`eventbasecode` string,`eventrootcode` string,
  `quadclass` INT,`goldsteinscale` FLOAT,`nummentions` INT,`numsources` INT,`numarticles` INT,`avgtone` FLOAT,
  `actor1geo_type` INT,`actor1geo_fullname` string,`actor1geo_countrycode` string,`actor1geo_adm1code` string,
  `actor1geo_lat` FLOAT,`actor1geo_long` FLOAT,`actor1geo_featureid` INT,
  `actor2geo_type` INT,`actor2geo_fullname` string,`actor2geo_countrycode` string,`actor2geo_adm1code` string,
  `actor2geo_lat` FLOAT,`actor2geo_long` FLOAT,`actor2geo_featureid` INT,
  `actiongeo_type` INT,`actiongeo_fullname` string,`actiongeo_countrycode` string,`actiongeo_adm1code` string,
  `actiongeo_lat` FLOAT,`actiongeo_long` FLOAT,`actiongeo_featureid` INT,
  `dateadded` INT,`sourceurl` string)
  ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
  WITH SERDEPROPERTIES ('serialization.format' = '	','field.delim' = '	') LOCATION 's3://philip-hadoop-bucket/first-demo-query/input/';
  -- This may not work, because I saved off the data as a DynamoDB supposedly.
  -- Therefore I presume the SERDEPROPERTIES change.
  -- For now, to avoid a cryptic error, let's suppress this idea.
  --WITH SERDEPROPERTIES (/'serialization.format' = '	','field.delim' = '	') LOCATION 's3://philip-hadoop-bucket/data/';

-- Total requests per operating system for a given time frame
INSERT OVERWRITE DIRECTORY '${OUTPUT}/demo-005/'
SELECT *
FROM gdelt_events
--10 means demand
WHERE eventcode LIKE "10%"
AND actor1countrycode IN ("USA", "DEU", "BRA", "ARG") OR
actor2countrycode IN ("USA", "DEU", "BRA", "ARG");
