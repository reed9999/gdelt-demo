-- So can the Goldstein scale help us guess which countries are allies?
-- What's the best way to write queries for both MySQL (development db) and
-- Hive?
-- A good solution might be to create small auxiliary tables that can be stored by Hive to s3 as needed.

CREATE TABLE IF NOT EXISTS dyads_by_stability_pre1983 AS
SELECT
  actor1geo_countrycode,
  actor2geo_countrycode,
  avg(goldsteinscale) as avg_goldsteinscale,
  count(*)
FROM gdelt.events
WHERE year < 1983
GROUP BY
  actor1geo_countrycode,
  actor2geo_countrycode
ORDER BY avg_goldsteinscale DESC, actor1geo_countrycode, actor2geo_countrycode;

CREATE TABLE IF NOT EXISTS dyads_by_stability_201601 AS
SELECT
  actor1geo_countrycode,
  actor2geo_countrycode,
  avg(goldsteinscale) as avg_goldsteinscale,
  count(*)
FROM gdelt.events
WHERE monthyear=201601
GROUP BY
  actor1geo_countrycode,
  actor2geo_countrycode
ORDER BY avg_goldsteinscale DESC, actor1geo_countrycode, actor2geo_countrycode;
