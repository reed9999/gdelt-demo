-- demo-003.q
-- I move toward more useful research by counting number of occurrences of each
-- country pair.

-- Refactoring: There were two queries here, the first to create the DB and this
-- one to query it. I have offloaded the first to load-gdelt-events.q

INSERT OVERWRITE DIRECTORY '${OUTPUT}/demo-003/'
SELECT actor1countrycode, actor2countrycode, COUNT(*)
FROM gdelt_events
GROUP BY actor1countrycode, actor2countrycode;
