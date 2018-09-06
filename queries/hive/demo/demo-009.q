-- demo-009.q
INSERT OVERWRITE DIRECTORY '${OUTPUT}/demo-009/'
SELECT actor1code, actor2code, actiongeo_fullname, count(*)
FROM gdelt_events
WHERE eventcode LIKE "10%"
GROUP BY actor1code, actor2code, actiongeo_fullname;
