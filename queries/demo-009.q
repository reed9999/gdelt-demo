-- demo-009.q
-- Incoherent query because SELECT DISTINCT and GROUP BY can't be together.
-- Also I forgot to change the output directory.

INSERT OVERWRITE DIRECTORY '${OUTPUT}/demo-008/'
SELECT DISTINCT actor1code, actor2code, actiongeo_fullname, count(*)
FROM gdelt_events
WHERE eventcode LIKE "10%"
GROUP BY actor1code, actor2code, actiongeo_fullname;
