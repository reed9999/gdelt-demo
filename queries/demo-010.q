-- demo-010.q

CREATE TABLE IF NOT EXISTS
demands_by_actor_pair
-- (`actor1code` string,
--   `actor2code` string,
-- `count_demands` int)
AS SELECT actor1code, actor2code, count(*)
FROM gdelt_events
WHERE eventcode LIKE "10%"
GROUP BY actor1code, actor2code;

CREATE TABLE  IF NOT EXISTS old_new_demands
-- (`actor1code` string,
--   `actor2code` string,
-- `period_1_demands` int,
-- `period_2_demands` int,
-- )
AS SELECT actor1code, actor2code, count(*), 9999
FROM gdelt_events
WHERE eventcode LIKE "10%"
AND year < 1999
GROUP BY actor1code, actor2code;

-- TODO: Then insert into the table the period 2 demands column.

INSERT OVERWRITE DIRECTORY '${OUTPUT}/old_new_demands/'
SELECT * FROM old_new_demands;
