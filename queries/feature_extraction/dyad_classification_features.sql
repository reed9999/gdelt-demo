-- First attempt to extract interesting features regarding actors and dyads
-- Among other things, this is to prepare for fun classification and clustering
-- demos

USE gdelt;
-- DROP TABLE IF EXISTS dyad_events_by_year;

CREATE TABLE IF NOT EXISTS dyad_events_by_year AS
SELECT year, actor1code, actor2code, eventcode, 
-- I don't see why I can't join on a group field but for for now this throws an error.
-- eventcodes.description,
eventbasecode,  eventrootcode, goldsteinscale, count(*) as count_events
FROM events LEFT JOIN eventcodes
  ON eventcodes.code = events.eventcode
GROUP BY year, actor1code, actor2code, eventcode,
-- these should be 1-to-1 with eventcode. Not sure if they would degrade performance or not.
eventbasecode,  eventrootcode, goldsteinscale
;


-- Now for the second order table, extracting some features that might
-- characterize individual dyads

-- !!!!!!!!!!!!!!!!!!!!!!!!!!!!
-- NOT YET WORKING 
-- counts for USA are nowhere near what they should be (38, 45 respectively)
-- !!!!!!!!!!!!!!!!!!!!!!!!!!!!

-- DROP TABLE IF EXISTS dyad_features;

CREATE TABLE IF NOT EXISTS dyad_features AS
SELECT a.actor1code, a.actor2code, 
	count(*) as count_aoeventcodes, sum(a.count_events) as sum_events
FROM dyad_events_by_year AS a
GROUP BY a.actor1code, actor2code;


DROP TABLE IF EXISTS actor_features;

CREATE TABLE IF NOT EXISTS country_features AS
SELECT c.country, 
	count(df1.actor2code) as actor1_relationships, 
	count(df2.actor1code) AS actor2_relationships
FROM countries c 
LEFT JOIN dyad_features AS df1 ON c.code = df1.actor1code
LEFT JOIN dyad_features as df2 ON c.code = df2.actor2code
GROUP BY country;

select count(*) FROM country_features;
select * FROM country_features;
