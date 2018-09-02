#DRY violations
S3_BUCKET=s3://philip-hadoop-bucket
SCRIPTS_DIR=$S3_BUCKET/scripts
QUERIES_DIR=$S3_BUCKET/queries

REGION=us-west-2
INSTANCE_TYPE=m3.micro #m3.large doesn't ever seem to work.
SEQUENCE=3

aws rdb create-db-instance \
--db-instance-identifier <value>
[--allocated-storage <value>]
--db-instance-class <value>
--engine <value>
[--master-username <value>]
[--master-user-password <value>]
[--db-security-groups <value>]
[--vpc-security-group-ids <value>]
[--availability-zone <value>]
[--db-subnet-group-name <value>]
[--preferred-maintenance-window <value>]
[--db-parameter-group-name <value>]
[--backup-retention-period <value>]
[--preferred-backup-window <value>]
[--port <value>]
[--multi-az | --no-multi-az]
[--engine-version <value>]
[--auto-minor-version-upgrade | --no-auto-minor-version-upgrade]
[--license-model <value>]
[--iops <value>]
[--option-group-name <value>]
[--character-set-name <value>]
[--publicly-accessible | --no-publicly-accessible]
[--tags <value>]
[--db-cluster-identifier <value>]
[--storage-type <value>]
[--tde-credential-arn <value>]
[--tde-credential-password <value>]
[--storage-encrypted | --no-storage-encrypted]
[--kms-key-id <value>]
[--domain <value>]
[--copy-tags-to-snapshot | --no-copy-tags-to-snapshot]
[--monitoring-interval <value>]
[--monitoring-role-arn <value>]
[--domain-iam-role-name <value>]
[--promotion-tier <value>]
[--timezone <value>]
[--enable-iam-database-authentication | --no-enable-iam-database-authentication]
[--enable-performance-insights | --no-enable-performance-insights]
[--performance-insights-kms-key-id <value>]
[--performance-insights-retention-period <value>]
[--enable-cloudwatch-logs-exports <value>]
[--processor-features <value>]
[--cli-input-json <value>]
[--generate-cli-skeleton <value>] --applications Name=Ganglia Name=Hadoop Name=Hive Name=Hue Name=Mahout Name=Pig Name=Tez --ec2-attributes '{"KeyName":"MainKeyPair","InstanceProfile":"EMR_EC2_DefaultRole","SubnetId":"subnet-4453270f","EmrManagedSlaveSecurityGroup":"sg-00286a3fc3b77d243","EmrManagedMasterSecurityGroup":"sg-03b92a0e407d74bab"}' --service-role EMR_DefaultRole --enable-debugging --release-label emr-5.16.0 --log-uri 's3n://philip-hadoop-bucket/' --steps '[
{"Args":["hive-script","--run-hive-script","--args","-f",
"'$QUERIES_DIR'/'$QUERY_TO_EXECUTE'",
"-d","OUTPUT='$S3_BUCKET'/first-demo-query/output/'$DEMO_NUMBER'"],"Type":"CUSTOM_JAR","ActionOnFailure":"CONTINUE","Jar":"command-runner.jar","Properties":"","Name":"Demo '$DEMO_NUMBER'"}
]' --name 'GDELT '$DEMO_NUMBER' demo' \
--instance-groups '[{"InstanceCount":1,"InstanceGroupType":"MASTER","InstanceType":"'$INSTANCE_TYPE'","Name":"Master demo '$DEMO_NUMBER'"},{"InstanceCount":1,"InstanceGroupType":"CORE","InstanceType":"'$INSTANCE_TYPE'","Name":"Core demo '$DEMO_NUMBER'"}]' \
--scale-down-behavior TERMINATE_AT_TASK_COMPLETION --auto-terminate --region $REGION

# INSTANCE_TYPE="m3.large" #m3.large may not be enough anyway
# echo "This doesn't appear to work because everything is so thoroughly escaped:"
# echo "$INSTANCE_TYPE"
# INSTANCE_GROUPS='[{"InstanceCount":1,"InstanceGroupType":"MASTER","InstanceType":"m3.xlarge","Name":"Master Instance Group"},{"InstanceCount":1,"InstanceGroupType":"CORE","InstanceType":"m3.xlarge","Name":"Core Instance Group"}]'
