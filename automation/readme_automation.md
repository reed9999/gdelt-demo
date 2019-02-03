# `automation` directory
This is the place for scripts (both Python and shell scripts) to do my personal-scale data 
engineering, particularly as needed to run big queries on AWS Elastic Map Reduce.
This root directory contains Python scripts using boto3, and the `scripts` subdirectory contains 
shell scripts (usually predecessors) to do similar things from the AWS CLI.

## How to execute on AWS
It's been over three months and AWS has hidden my audit trail of what I did, so I'm reconstructing
this as I go.

- emr\_create\_and\_run\_all.py: Probably the starting point. I want to reconfigure it to use spot 
pricing. For now just see if it runs.

Example using spot pricing: https://stackoverflow.com/questions/26314316/how-to-launch-and-configure-an-emr-cluster-using-boto


