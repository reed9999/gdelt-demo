-- demo-011.q

UPDATE TABLE ond
SET period_2_demands = count(*)
FROM
  old_new_demands as ond
  LEFT JOIN gdelt_events as ev
    ON ond.actor1code = ev.actor1code
    AND ond.actor2code = ev.actor2code
  WHERE ev.eventcode LIKE "10%"
  AND year >= 1999
  GROUP BY actor1code, actor2code
  ;
-- demo-010.q
--
-- CREATE TABLE IF NOT EXISTS
-- demands_by_actor_pair
-- -- (`actor1code` string,
-- --   `actor2code` string,
-- -- `count_demands` int)
-- AS SELECT actor1code, actor2code, count(*)
-- FROM gdelt_events
-- WHERE eventcode LIKE "10%"
-- GROUP BY actor1code, actor2code;
--
-- CREATE TABLE  IF NOT EXISTS old_new_demands
-- -- (`actor1code` string,
-- --   `actor2code` string,
-- -- `period_1_demands` int,
-- -- `period_2_demands` int,
-- -- )
-- AS SELECT actor1code, actor2code, count(*), NULL
-- FROM gdelt_events
-- WHERE eventcode LIKE "10%"
-- AND year < 1999
-- GROUP BY actor1code, actor2code;
--
-- -- TODO: Then insert into the table the period 2 demands column.
--
-- INSERT OVERWRITE DIRECTORY '${OUTPUT}/old_new_demands/'
-- SELECT * FROM old_new_demands;
