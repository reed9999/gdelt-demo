-- Earlier I asked if the Goldstein scale can help us guess which countries are allies.
-- Now lets look at avgtone, the average tone of "all documents" (usually media reports) on
-- a particular event.
-- DRY violations abound because this is me getting to know the data better.

SELECT
  actor1geo_countrycode,
  actor2geo_countrycode,
  avg(avgtone) as avg_avgtone,
  count(*)
FROM gdelt.events
GROUP BY
  actor1geo_countrycode,
  actor2geo_countrycode
ORDER BY avg_avgtone DESC, actor1geo_countrycode, actor2geo_countrycode;


-- So what does a zero dyad look like?
-- (Note: avgtone is supposed to sometimes be negative but my mini dataset has a min of 0)
SELECT
  actor1code, actor1name, actor1ethniccode,
  actor2code, actor2name, actor2ethniccode,
  actor1geo_countrycode, actor1geo_fullname,
  actor2geo_countrycode, actor2geo_fullname,
  actiongeo_countrycode, actiongeo_fullname,
  eventcode, goldsteinscale, avgtone, 
  sourceurl -- to give us an idea of the story, but all NULL.
FROM gdelt.events
WHERE
  actor1geo_countrycode = "UK" AND
  actor2geo_countrycode = "IT";

-- Some things I notice: 
-- (1) Actor "SPAIN", code "ESP", has country code "IT", fullname "Italy". 
--     Unless I'm completely missing the point this suggests dirty data.
-- (2) There's an actor2 with name "ITALIAN", code "ITA". This also suggests dirty data.

-- Sometimes both actors are from the same country. Here average is very low 
-- among different elements of the Laotian govt: 
SELECT
  actor1code, actor1name, actor1ethniccode,
  actor2code, actor2name, actor2ethniccode,
  actor1geo_countrycode, actor1geo_fullname,
  actor2geo_countrycode, actor2geo_fullname,
  actiongeo_countrycode, actiongeo_fullname,
  eventcode, goldsteinscale, avgtone, 
  sourceurl -- to give us an idea of the story, but all NULL.
FROM gdelt.events
WHERE
  actor1geo_countrycode = "LA" AND
  actor2geo_countrycode = "LA";


-- and what does a really positive dyad look like?
-- I have no idea why Guinea-Ukraine would be, but apparently there was
-- one pleasant visit that generated three rows. 
-- (TODO: What does this mean?)
SELECT
  day, monthyear,
  actor1code, actor1name, actor1ethniccode,
  actor2code, actor2name, actor2ethniccode,
  actor1geo_countrycode, actor1geo_fullname,
  actor2geo_countrycode, actor2geo_fullname,
  actiongeo_countrycode, actiongeo_fullname,
  eventcode, co.description,
  goldsteinscale, avgtone, 
  sourceurl
FROM gdelt.events AS ev LEFT JOIN gdelt.eventcodes co 
  ON ev.eventcode = co.code
WHERE
  actor1geo_countrycode = "GV" AND
  actor2geo_countrycode = "UP";


-- TODO Let's create a table of dyads/goldstein by year. 