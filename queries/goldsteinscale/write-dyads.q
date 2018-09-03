INSERT OVERWRITE DIRECTORY '${OUTPUT}/dyads-pre1983/'
SELECT * FROM dyads_by_stability_pre1983;
INSERT OVERWRITE DIRECTORY '${OUTPUT}/dyads_by_stability_201601/'
SELECT * FROM dyads_by_stability_201601;
