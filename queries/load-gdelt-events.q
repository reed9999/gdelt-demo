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

-- Continuing my adaptation of this script:
-- http://blog.julien.org/2017/03/exploring-gdelt-data-set-with-amazon.html

-- By the way comments are at the bottom to help me figure out the error
-- messages' line numbering, which is really unclear.

-- Note also:
-- first-demo-query.q had the query ending:
-- ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
--   WITH SERDEPROPERTIES ('serialization.format' = '	','field.delim' = '	') LOCATION 's3://gdelt-open-data/events/';
-- This works for the ENTIRE GDELT dataset, not for development/testing
