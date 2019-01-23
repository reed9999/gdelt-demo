# gdelt-demo: Notes on datasets

Over time and through lack of planning, I have created various subsets of the version 1 GDELT dataset
both locally and on AWS (both MySQL and flat files in s3). Small and medium subsets are
a good thing (they could be considered dev and test, respectively), but poor coordination and
haphazard proliferation are not good.

## Datasets to keep

1. **FULL: Full GDELT on s3://gdelt-open-data/ -- tab-delimited as \*.csv** -- obviously not mine.
1. **SMALL: Local tab-delimited files** -- too big to put in this repo. Intended to validate analysis code. 
For many dates I used a util script to pull 1/10 of the rows. 
1. **MICRO: Flat files in this git repo** - See `data_related/sample_data`. Anyone cloning 
the repo can get going quickly and get output with this set.

Note: The summary country data under `data_related/features` and `data_related/external` also fit
in this repo but should be part of any dataset. The former resulted from a Hadoop query summarizing
the entire dataset.

## Datasets to harmonize
1. **Mini tab-delimited on my s3** -- useful for validating HiveQL scripts. Should match SMALL.
1. **MySQL on AWS Relational Database service** -- should match SMALL
1. **MySQL on my local server** -- lost in a computer crash. Should be rebuilt to match SMALL.

## Datasets to consider eliminating
1. **Mini version** - I forget what this refers to, maybe something stray on s3. I should 
check out what it is, but my strong prior is that it's no longer adding any value..

## Version 2 (future)
As I get into really understanding the Global Knowledge Graph, I may avail myself of the services
offered in its native habitat on Google BigQuery.
