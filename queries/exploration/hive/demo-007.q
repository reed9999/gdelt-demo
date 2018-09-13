-- demo-007.q
-- Extend 006 by reintroducing the country "IN" list.
-- Try it with and without the event filter just to troubleshoot if anything
-- breaks.

INSERT OVERWRITE DIRECTORY '${OUTPUT}/demo-7a/'
SELECT *
FROM gdelt_events
WHERE actor1countrycode IN ("BRA", "ARG", "AFG", "ESP", "POR", "AUS");

INSERT OVERWRITE DIRECTORY '${OUTPUT}/demo-7b/'
SELECT *
FROM gdelt_events
WHERE eventcode LIKE "10%"
AND actor1countrycode IN ("USA", "DEU", "BRA", "ARG");
-- actor2countrycode IN ("USA", "DEU", "BRA", "ARG");
