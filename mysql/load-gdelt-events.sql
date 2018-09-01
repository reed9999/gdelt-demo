-- DRY: Should keep one copy of the GDELT columns and generate whatever flavor
-- of SQL on the fly.
-- assuming every VARCHAR to be length 256 is really inefficient (and might
-- truncate wrongly on occasion) so it's better to find find a specific VARCHAR
-- schema. Search the Web or use my own intuition if needed. 
CREATE TABLE IF NOT EXISTS events (
  `globaleventid` INT,`day` INT,`monthyear` INT,`year` INT,`fractiondate` FLOAT,
  `actor1code` VARCHAR(256),`actor1name` VARCHAR(256),`actor1countrycode` VARCHAR(256),`actor1knowngroupcode` VARCHAR(256),
  `actor1ethniccode` VARCHAR(256),`actor1religion1code` VARCHAR(256),`actor1religion2code` VARCHAR(256),
  `actor1type1code` VARCHAR(256),`actor1type2code` VARCHAR(256),`actor1type3code` VARCHAR(256),
  `actor2code` VARCHAR(256),`actor2name` VARCHAR(256),`actor2countrycode` VARCHAR(256),`actor2knowngroupcode` VARCHAR(256),
  `actor2ethniccode` VARCHAR(256),`actor2religion1code` VARCHAR(256),`actor2religion2code` VARCHAR(256),
  `actor2type1code` VARCHAR(256),`actor2type2code` VARCHAR(256),`actor2type3code` VARCHAR(256),
  `isrootevent` BOOLEAN,`eventcode` VARCHAR(256),`eventbasecode` VARCHAR(256),`eventrootcode` VARCHAR(256),
  `quadclass` INT,`goldsteinscale` FLOAT,`nummentions` INT,`numsources` INT,`numarticles` INT,`avgtone` FLOAT,
  `actor1geo_type` INT,`actor1geo_fullname` VARCHAR(256),`actor1geo_countrycode` VARCHAR(256),`actor1geo_adm1code` VARCHAR(256),
  `actor1geo_lat` FLOAT,`actor1geo_long` FLOAT,`actor1geo_featureid` INT,
  `actor2geo_type` INT,`actor2geo_fullname` VARCHAR(256),`actor2geo_countrycode` VARCHAR(256),`actor2geo_adm1code` VARCHAR(256),
  `actor2geo_lat` FLOAT,`actor2geo_long` FLOAT,`actor2geo_featureid` INT,
  `actiongeo_type` INT,`actiongeo_fullname` VARCHAR(256),`actiongeo_countrycode` VARCHAR(256),`actiongeo_adm1code` VARCHAR(256),
  `actiongeo_lat` FLOAT,`actiongeo_long` FLOAT,`actiongeo_featureid` INT,
  `dateadded` INT,`sourceurl` VARCHAR(256));
