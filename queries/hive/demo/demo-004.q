-- demo-004.q
-- I continue toward more useful research by replicating the counts in 003, but
-- only for event codes associated with demands.
-- This is a demonstration that LIKE "10%" works.

-- Refactoring: There were two queries here, the first to create the DB and this
-- one to query it. I have offloaded the first to load-gdelt-events.q

INSERT OVERWRITE DIRECTORY '${OUTPUT}/demo-004/'
SELECT actor1countrycode, actor2countrycode, COUNT(*), 'DEMAND'
FROM gdelt_events
--10 means demand
WHERE eventcode LIKE "10%"
GROUP BY actor1countrycode, actor2countrycode;
