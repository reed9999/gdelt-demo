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
  eventcode, goldsteinscale, avgtone
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


-- and what does a really stable dyad look like?
-- precursor to the Israel-Lebanon war, oddly enough, but seems that in Jan 1982
-- there was quite a bit of military deescalation.
SELECT
  actor1code, actor1name, actor1ethniccode,
  actor2code, actor2name, actor2ethniccode,
  actor1geo_countrycode, actor1geo_fullname,
  actor2geo_countrycode, actor2geo_fullname,
  actiongeo_countrycode, actiongeo_fullname,
  eventcode, goldsteinscale, avgtone
FROM gdelt.events
WHERE
  actor1geo_countrycode = "IS" AND
  actor2geo_countrycode = "LE";


-- TODO Let's create a table of dyads/goldstein by year. 