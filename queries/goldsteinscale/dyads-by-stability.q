-- So can the Goldstein scale help us guess which countries are allies?

SELECT
  actor1geo_countrycode,
  actor2geo_countrycode,
  avg(goldsteinscale) as avg_goldsteinscale,
  count(*)
FROM gdelt.events
GROUP BY
  actor1geo_countrycode,
  actor2geo_countrycode
ORDER BY avg_goldsteinscale DESC, actor1geo_countrycode, actor2geo_countrycode;

-- So what does a really unstable dyad look like?
SELECT
  actor1code, actor1name, actor1ethniccode,
  actor2code, actor2name, actor2ethniccode,
  actor1geo_countrycode, actor1geo_fullname,
  actor2geo_countrycode, actor2geo_fullname,
  actiongeo_countrycode, actiongeo_fullname,
  eventcode, goldsteinscale
FROM gdelt.events
WHERE
  actor1geo_countrycode = "SF" AND
  actor2geo_countrycode = "AO";

-- and what does a really stable dyad look like?
-- precursor to the Israel-Lebanon war, oddly enough, but seems that in Jan 1982
-- there was quite a bit of military deescalation.
SELECT
  actor1code, actor1name, actor1ethniccode,
  actor2code, actor2name, actor2ethniccode,
  actor1geo_countrycode, actor1geo_fullname,
  actor2geo_countrycode, actor2geo_fullname,
  actiongeo_countrycode, actiongeo_fullname,
  eventcode, goldsteinscale
FROM gdelt.events
WHERE
  actor1geo_countrycode = "IS" AND
  actor2geo_countrycode = "LE";
