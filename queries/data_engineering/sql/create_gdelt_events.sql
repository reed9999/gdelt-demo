-- DRY: Should keep one copy of the GDELT columns and generate whatever flavor
-- of SQL on the fly.
-- assuming every VARCHAR to be length 256 is really inefficient (and might
-- truncate wrongly on occasion) so it's better to find find a specific VARCHAR
-- schema. Search the Web or use my own intuition if needed. 

-- (Fixes to featureid fields: Temporarily untested!)
DROP TABLE IF EXISTS events;
CREATE TABLE events (
  `globaleventid` INT,
  `day` INT NULL,
  `monthyear` INT NULL,
  `year` INT NULL,
  `fractiondate` FLOAT NULL,
  `actor1code` VARCHAR(256) NULL,
  `actor1name` VARCHAR(256) NULL,
  `actor1countrycode` VARCHAR(256) NULL,
  `actor1knowngroupcode` VARCHAR(256) NULL,
  `actor1ethniccode` VARCHAR(256) NULL,
  `actor1religion1code` VARCHAR(256) NULL,
  `actor1religion2code` VARCHAR(256) NULL,
  `actor1type1code` VARCHAR(256) NULL,
  `actor1type2code` VARCHAR(256) NULL,
  `actor1type3code` VARCHAR(256) NULL,
  `actor2code` VARCHAR(256) NULL,
  `actor2name` VARCHAR(256) NULL,
  `actor2countrycode` VARCHAR(256) NULL,
  `actor2knowngroupcode` VARCHAR(256) NULL,
  `actor2ethniccode` VARCHAR(256) NULL,
  `actor2religion1code` VARCHAR(256) NULL,
  `actor2religion2code` VARCHAR(256) NULL,
  `actor2type1code` VARCHAR(256) NULL,
  `actor2type2code` VARCHAR(256) NULL,
  `actor2type3code` VARCHAR(256) NULL,
  `isrootevent` BOOLEAN NULL,
  `eventcode` VARCHAR(256) NULL,
  `eventbasecode` VARCHAR(256) NULL,
  `eventrootcode` VARCHAR(256) NULL,
  `quadclass` INT NULL,
  `goldsteinscale` FLOAT NULL,
  `nummentions` INT NULL,
  `numsources` INT NULL,
  `numarticles` INT NULL,
  `avgtone` FLOAT NULL,
  `actor1geo_type` VARCHAR(10) NULL,
  `actor1geo_fullname` VARCHAR(256) NULL,
  `actor1geo_countrycode` VARCHAR(256) NULL,
  `actor1geo_adm1code` VARCHAR(256) NULL,
  `actor1geo_lat` FLOAT NULL,
  `actor1geo_long` FLOAT NULL,
  `actor1geo_featureid` VARCHAR(10) NULL,
  `actor2geo_type` VARCHAR(10) NULL,
  `actor2geo_fullname` VARCHAR(256) NULL,
  `actor2geo_countrycode` VARCHAR(256) NULL,
  `actor2geo_adm1code` VARCHAR(256) NULL,
  `actor2geo_lat` FLOAT NULL,
  `actor2geo_long` FLOAT NULL,
  `actor2geo_featureid` VARCHAR(10) NULL,
  `actiongeo_type` VARCHAR(10) NULL,
  `actiongeo_fullname` VARCHAR(256) NULL,
  `actiongeo_countrycode` VARCHAR(256) NULL,
  `actiongeo_adm1code` VARCHAR(256) NULL,
  `actiongeo_lat` FLOAT NULL,
  `actiongeo_long` FLOAT NULL,
  `actiongeo_featureid` VARCHAR(10) NULL,
  `dateadded` INT NULL,
  `sourceurl` VARCHAR(256) DEFAULT '' NULL
);
