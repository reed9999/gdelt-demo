-- demo-005.q
-- formerly demo-005-part2.q
-- 004 might have been failing, because for some reason I wanted to tshoot
-- by just matching on a single eventcode. Doing a LIKE or an IN is much more
-- useful but this needs to work too.
-- Perhaps it failed because I used single quotes where it should be double.

-- It still fails but only after trying to do something. See below.

INSERT OVERWRITE DIRECTORY '${OUTPUT}/demo-005/'
SELECT *
FROM gdelt_events
WHERE eventcode = "1011";   --failed with single quotes

--- Basically none of my attempts to do anything more sophisticated are working.
-- WHERE eventcode IN ('10', '101', '102', '1011','1012');
----------
-- AND actor1countrycode IN ("USA", "DEU", "BRA", "ARG") OR
-- actor2countrycode IN ("USA", "DEU", "BRA", "ARG");


--------------------------------------
-- Full error
--
--
-- Logging initialized using configuration in file:/etc/hive/conf.dist/hive-log4j2.properties Async: false
-- Query ID = hadoop_20180827003011_2b0242be-a3e7-402d-874a-620d17b81b6d
-- Total jobs = 1
-- Launching Job 1 out of 1
-- Status: Running (Executing on YARN cluster with App id application_1535329573405_0004)
--
-- Map 1: -/-
-- Map 1: 0/6
-- Map 1: 0/6
-- Map 1: 0(+1)/6
-- Map 1: 0(+2)/6
-- Map 1: 0(+3)/6
-- Map 1: 0(+4)/6
-- Map 1: 0(+5)/6
-- Map 1: 0(+6)/6
-- Map 1: 0(+6)/6
-- Map 1: 0(+6)/6
-- Map 1: 0(+6)/6
-- Map 1: 0(+6)/6
-- Map 1: 1(+5)/6
-- Map 1: 1(+5)/6
-- Map 1: 2(+4)/6
-- Map 1: 3(+3)/6
-- Map 1: 4(+2)/6
-- Map 1: 5(+1)/6
-- Map 1: 6/6
-- Moving data to directory s3://philip-hadoop-bucket/output/005/demo-005
-- OK
-- Time taken: 44.537 seconds
-- NoViableAltException(-1@[])
-- 	at org.apache.hadoop.hive.ql.parse.HiveParser.statement(HiveParser.java:1300)
-- 	at org.apache.hadoop.hive.ql.parse.ParseDriver.parse(ParseDriver.java:208)
-- 	at org.apache.hadoop.hive.ql.parse.ParseUtils.parse(ParseUtils.java:77)
-- 	at org.apache.hadoop.hive.ql.parse.ParseUtils.parse(ParseUtils.java:70)
-- 	at org.apache.hadoop.hive.ql.Driver.compile(Driver.java:468)
-- 	at org.apache.hadoop.hive.ql.Driver.compileInternal(Driver.java:1317)
-- 	at org.apache.hadoop.hive.ql.Driver.runInternal(Driver.java:1457)
-- 	at org.apache.hadoop.hive.ql.Driver.run(Driver.java:1237)
-- 	at org.apache.hadoop.hive.ql.Driver.run(Driver.java:1227)
-- 	at org.apache.hadoop.hive.cli.CliDriver.processLocalCmd(CliDriver.java:233)
-- 	at org.apache.hadoop.hive.cli.CliDriver.processCmd(CliDriver.java:184)
-- 	at org.apache.hadoop.hive.cli.CliDriver.processLine(CliDriver.java:403)
-- 	at org.apache.hadoop.hive.cli.CliDriver.processLine(CliDriver.java:336)
-- 	at org.apache.hadoop.hive.cli.CliDriver.processReader(CliDriver.java:474)
-- 	at org.apache.hadoop.hive.cli.CliDriver.processFile(CliDriver.java:490)
-- 	at org.apache.hadoop.hive.cli.CliDriver.executeDriver(CliDriver.java:793)
-- 	at org.apache.hadoop.hive.cli.CliDriver.run(CliDriver.java:759)
-- 	at org.apache.hadoop.hive.cli.CliDriver.main(CliDriver.java:686)
-- 	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
-- 	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
-- 	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
-- 	at java.lang.reflect.Method.invoke(Method.java:498)
-- 	at org.apache.hadoop.util.RunJar.run(RunJar.java:234)
-- 	at org.apache.hadoop.util.RunJar.main(RunJar.java:148)
-- FAILED: ParseException line 3:0 cannot recognize input near '<EOF>' '<EOF>' '<EOF>'
-- Command exiting with ret '64'
