INSERT OVERWRITE DIRECTORY '${OUTPUT}/count/'
SELECT count(*) FROM gdelt_events;
