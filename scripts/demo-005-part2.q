-- See demo-005.q for the first part.



  -- This may not work, because I saved off the data as a DynamoDB supposedly.
  -- Therefore I presume the SERDEPROPERTIES change.
  -- For now, to avoid a cryptic error, let's suppress this idea.
  --WITH SERDEPROPERTIES (/'serialization.format' = '	','field.delim' = '	') LOCATION 's3://philip-hadoop-bucket/data/';

INSERT OVERWRITE DIRECTORY '${OUTPUT}/demo-005a/'
SELECT *
FROM gdelt_events
WHERE eventcode = '1011';

--- Basically none of my attempts to do anything more sophisticated are working.
-- WHERE eventcode IN ('10', '101', '102', '1011','1012');
--10 means demand
----------
-- WHERE eventcode LIKE '10%';
----------
-- AND actor1countrycode IN ("USA", "DEU", "BRA", "ARG") OR
-- actor2countrycode IN ("USA", "DEU", "BRA", "ARG");
