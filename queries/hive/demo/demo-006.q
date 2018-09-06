-- demo-006.q
-- formerly demo-005-part2b.q
-- 005-part2 (now known as 005) failed with
--    WHERE eventcode = "1011"
-- However the single quotes seemed to work here, which means I need to learn a
-- lot about Hive QL syntax.

INSERT OVERWRITE DIRECTORY '${OUTPUT}/demo-006/'
SELECT *
FROM gdelt_events
WHERE eventcode IN ('10', '101');
---------- previous attempt 
-- AND actor1countrycode IN ("USA", "DEU", "BRA", "ARG") OR
-- actor2countrycode IN ("USA", "DEU", "BRA", "ARG");
