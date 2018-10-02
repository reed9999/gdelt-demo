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

CREATE TABLE IF NOT EXISTS dyad_features AS
SELECT a.actor1code, a.actor2code, 
	count(*) as count_aoeventcodes, sum(a.count_events) as sum_events
FROM dyad_events_by_year AS a
GROUP BY a.actor1code, actor2code;

-- And the third order table, which has a second query.
-- There may well be a more elegant way to do this with a big nested SELECT


DROP TABLE IF EXISTS country_features;

CREATE TABLE IF NOT EXISTS country_features AS
	SELECT c.country, c.code, 
		count(df1.actor2code) as actor1_relationships, 
		99999 as actor2_relationships
	FROM countries c 
	LEFT JOIN dyad_features AS df1 ON c.code = df1.actor1code
	GROUP BY c.country, c.code;

UPDATE country_features
SET actor2_relationships = (
	SELECT count(*) 
    FROM countries c 
	INNER JOIN dyad_features AS df2 ON c.code = df2.actor2code
    WHERE df2.actor2code = country_features.code
)    ;
select * FROM country_features WHERE code = 'USA';
select * FROM country_features WHERE code = 'ESP';
