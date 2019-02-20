-- Hive equivalent of dyad_classification_features.sql


DROP TABLE IF EXISTS gdelt_event_codes; 
CREATE EXTERNAL TABLE gdelt_event_codes (
   `code` STRING, 
   `description` STRING 
) 
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe' 
WITH SERDEPROPERTIES ('serialization.format' = '\t','field.delim' = '\t') 
LOCATION 's3://reed9999/data/eventcodes/';

-- NOTE: It's only run successfully on AWS EMR up to here (because I forgot 
-- the next DROP TABLE so tried to create a duplicate.)
--------------------------------------------------------------------------------
-- Extraction #1: 
-- Extract each kind of event for each dyad by year.
-- I stopped this before it could run its course but seems to start up OK on EMR
DROP TABLE IF EXISTS dyad_events_by_year; 
CREATE TABLE dyad_events_by_year AS
SELECT year, actor1code, actor2code, eventcode,
eventbasecode,  eventrootcode, goldsteinscale, count(e.year) as count_events
FROM gdelt_events e  LEFT JOIN gdelt_event_codes ec
  ON ec.code = e.eventcode
GROUP BY year, actor1code, actor2code, eventcode,
eventbasecode,  eventrootcode, goldsteinscale;

--------------------------------------------------------------------------------
-- Extraction #2: 
-- some features that might characterize individual dyads across all of time. 

DROP TABLE IF EXISTS dyad_features; 
CREATE TABLE dyad_features AS
SELECT a.actor1code, a.actor2code, 
  count(a.actor1code) as count_eventcodes, sum(a.count_events) as sum_events
FROM dyad_events_by_year AS a
GROUP BY a.actor1code, actor2code;

-- Another lookup table
DROP TABLE IF EXISTS gdelt_countries; 
CREATE EXTERNAL TABLE gdelt_countries (`code` string,`country` string) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe' WITH SERDEPROPERTIES ('serialization.format' = '\t','field.delim' = '\t') LOCATION 's3://reed9999/data/countries/';


DROP TABLE IF EXISTS country_features; 



-- THE SCRIPT ONLY WORKS TO HERE (possibly an old comment?)
-- And the third order table, which has a second query.
-- This explains a bit about Hive subtleties I need to consider:
-- https://stackoverflow.com/q/28405367/
-- FAILED: SemanticException org.apache.hadoop.hive.ql.optimizer.calcite.CalciteSubquerySemanticException: Unsupported SubQuery Expression Invalid subquery. Subquery in SELECT could only be top-level expression
CREATE TABLE country_features AS
SELECT c.country, c.code, 
count(df1.actor2code) as actor1_relationships, 
(SELECT count(*) 
FROM dyad_features AS df2 
WHERE df2.actor2code = c.code) as actor2_relationships
FROM gdelt_countries c 
LEFT JOIN dyad_features AS df1 ON c.code = df1.actor1code
GROUP BY c.country, c.code;

-- TROUBLESHOOTING
CREATE TABLE foo AS (SELECT count(*) FROM dyad_features AS df2 WHERE df2.actor2code = 'USA'); --works
DROP TABLE IF EXISTS foo;
CREATE TABLE foo AS (SELECT count(*) FROM dyad_features AS df2 WHERE df2.actor2code = c.code)
FROM gdelt_countries c LEFT JOIN dyad_features;
; --works


INSERT OVERWRITE DIRECTORY '${hiveconf:OUTPUT}/dyad_events_by_year/'
SELECT * FROM dyad_events_by_year;
INSERT OVERWRITE DIRECTORY '${hiveconf:OUTPUT}/dyad_features/'
SELECT * FROM dyad_features;
-- INSERT OVERWRITE DIRECTORY '${hiveconf:OUTPUT}/country_features/'
-- SELECT * FROM country_features;

