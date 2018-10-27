-- demo-008.q
-- Extend 008 by introducing sorting by day and isrootevent.

INSERT OVERWRITE DIRECTORY '${OUTPUT}/demo-008/'
SELECT *
FROM gdelt_events
WHERE eventcode LIKE "10%"
AND actor1countrycode IN ("USA", "DEU", "BRA", "ARG")
ORDER BY day, isrootevent;
-- actor2countrycode IN ("USA", "DEU", "BRA", "ARG");
