-- first-demo-shorter.q       query number 002
-- The full-dataset one (deleted) would be 001 and this would be 002.

-- Refactoring: There were two queries here, the first to create the DB and this
-- one to query it. I have offloaded the first to load-gdelt-events.q
-- There's no longer much purpose for this query anyway, except tshooting.
INSERT OVERWRITE DIRECTORY '${OUTPUT}/first-demo-query/' SELECT DISTINCT actor1code FROM gdelt_events ;
