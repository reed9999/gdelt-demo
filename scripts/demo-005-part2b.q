-- See demo-005.q for the first part.

INSERT OVERWRITE DIRECTORY '${OUTPUT}/demo-005b/'
SELECT *
FROM gdelt_events
WHERE eventcode IN ('10', '101');
--10 means demand
----------
-- WHERE eventcode LIKE '10%';
----------
-- AND actor1countrycode IN ("USA", "DEU", "BRA", "ARG") OR
-- actor2countrycode IN ("USA", "DEU", "BRA", "ARG");
