-- demo-005.q
-- formerly demo-005-part2.q
-- 004 might have been failing, because for some reason I wanted to tshoot
-- by just matching on a single eventcode. Doing a LIKE or an IN is much more
-- useful but this needs to work too.
-- Perhaps it failed because I used single quotes where it should be double.

INSERT OVERWRITE DIRECTORY '${OUTPUT}/demo-005/'
SELECT *
FROM gdelt_events
WHERE eventcode = "1011";   --failed with single quotes

--- Basically none of my attempts to do anything more sophisticated are working.
-- WHERE eventcode IN ('10', '101', '102', '1011','1012');
----------
-- AND actor1countrycode IN ("USA", "DEU", "BRA", "ARG") OR
-- actor2countrycode IN ("USA", "DEU", "BRA", "ARG");
