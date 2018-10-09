-- Hive equivalent of dyad_classification_features.sql
DROP TABLE IF EXISTS gdelt_event_codes;
CREATE EXTERNAL TABLE gdelt_event_codes (
   `code` STRING, 
   `description` STRING 
) 
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe' 
WITH SERDEPROPERTIES ('serialization.format' = '\t','field.delim' = '\t') 
LOCATION 's3://reed9999/data/gdelt/eventcodes/';


-- So far only verified (on AWS EMR) to here.
--------------------------------------------------------------------------------
-- Extraction #1: 
-- Extract each kind of event for each dyad by year.
-- I stopped this before it could run its course but seems to start up OK on EMR

CREATE TABLE dyad_events_by_year AS
SELECT year, actor1code, actor2code, eventcode, 
eventbasecode,  eventrootcode, goldsteinscale, count(e.year) as count_events
FROM gdelt_events e  LEFT JOIN gdelt_event_codes ec
  ON ec.code = e.eventcode
GROUP BY year, actor1code, actor2code, eventcode,
eventbasecode,  eventrootcode, goldsteinscale;

-- 
-- --------------------------------------------------------------------------------
-- -- Extraction #2: 
-- -- some features that might characterize individual dyads across all of time. 
-- 
-- CREATE EXTERNAL TABLE dyad_features AS
-- SELECT a.actor1code, a.actor2code, 
-- 	count(*) as count_aoeventcodes, sum(a.count_events) as sum_events
-- FROM dyad_events_by_year AS a
-- GROUP BY a.actor1code, actor2code;
