# gdelt-demo: Some notes about the data

Long story short: I have several different versions of the GDELT data for different purposes. From biggest to smallest: 

1. Full GDELT on s3://gdelt-open-data/ -- tab-delimited as *.csv
1. Mini tab-delimited on my s3, useful for validating HiveQL scripts
1. Local tab-delimited, not in this repo, not-exactly-random selection of files
  - Also mini and micro versions
1. MySQL on AWS Relational Database service
1. MySQL on my local server
1. Micro db as part of this git repo


It would probably make sense to bring these into harmony.
