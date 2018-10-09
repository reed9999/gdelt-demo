-- Hive equivalent of dyad_classification_features.sql
DROP TABLE IF EXISTS gdelt_event_codes;
CREATE EXTERNAL TABLE gdelt_event_codes (
   `code` STRING, 
   `description` STRING 
) 
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe' 
WITH SERDEPROPERTIES ('serialization.format' = '\t','field.delim' = '\t') 
LOCATION 's3://reed9999/data/gdelt/eventcodes/';


-- So far it only works to here.



-- CREATE EXTERNAL TABLE gdelt_event_codes (
--   `code` STRING, `description` STRING
-- ) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
-- WITH SERDEPROPERTIES ('serialization.format' = '\t','field.delim' = '	') LOCATION 's3://reed9999/gdelt/eventcodes.txt';




-- CREATE EXTERNAL TABLE dyad_events_by_year AS
-- SELECT year, actor1code, actor2code, eventcode, 
-- eventbasecode,  eventrootcode, goldsteinscale, count(events.year) as count_events
-- FROM gdelt_events events LEFT JOIN eventcodes
--   ON eventcodes.code = events.eventcode
-- GROUP BY year, actor1code, actor2code, eventcode,
-- eventbasecode,  eventrootcode, goldsteinscale
-- ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
-- WITH SERDEPROPERTIES ('serialization.format' = '\t','field.delim' = '	') LOCATION 's3://gdelt-open-data/events/';
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
