#DRY violations
S3_BUCKET=s3://philip-hadoop-bucket
SCRIPTS_DIR=$S3_BUCKET/scripts
QUERIES_DIR=$S3_BUCKET/queries

DEMO_NUMBER="003 through 006"
REGION=us-west-2
INSTANCE_TYPE=m3.xlarge #m3.large doesn't ever seem to work.

aws emr create-cluster --applications Name=Ganglia Name=Hadoop Name=Hive Name=Hue Name=Mahout Name=Pig Name=Tez --ec2-attributes '{"KeyName":"MainKeyPair","InstanceProfile":"EMR_EC2_DefaultRole","SubnetId":"subnet-4453270f","EmrManagedSlaveSecurityGroup":"sg-00286a3fc3b77d243","EmrManagedMasterSecurityGroup":"sg-03b92a0e407d74bab"}' --service-role EMR_DefaultRole --enable-debugging --release-label emr-5.16.0 --log-uri 's3n://philip-hadoop-bucket/' --steps '[{"Args":["hive-script","--run-hive-script","--args","-f","'$QUERIES_DIR'/load-gdelt-events.q","-d","OUTPUT='$S3_BUCKET'/output/all"],"Type":"CUSTOM_JAR","ActionOnFailure":"CONTINUE","Jar":"command-runner.jar","Properties":"=","Name":"Demo all Demands by four selected countries"},{"Args":["hive-script","--run-hive-script","--args","-f","'$QUERIES_DIR'/demo-004.q","-d","OUTPUT='$S3_BUCKET'/output/004"],"Type":"CUSTOM_JAR","ActionOnFailure":"CONTINUE","Jar":"command-runner.jar","Properties":"","Name":"Demo 004"},
{"Args":["hive-script","--run-hive-script","--args","-f","'$QUERIES_DIR'/demo-005.q","-d","OUTPUT='$S3_BUCKET'/output/005"],"Type":"CUSTOM_JAR","ActionOnFailure":"CONTINUE","Jar":"command-runner.jar","Properties":"","Name":"Demo 005"},
{"Args":["hive-script","--run-hive-script","--args","-f","'$QUERIES_DIR'/demo-006.q","-d","OUTPUT='$S3_BUCKET'/output/006"],"Type":"CUSTOM_JAR","ActionOnFailure":"CONTINUE","Jar":"command-runner.jar","Properties":"","Name":"Demo 006"}]' --name 'GDELT all demo' --instance-groups '[{"InstanceCount":1,"InstanceGroupType":"CORE","InstanceType":"m3.xlarge","Name":"Core demo all"},{"InstanceCount":1,"InstanceGroupType":"MASTER","InstanceType":"m3.xlarge","Name":"Master demo all"}]' --scale-down-behavior TERMINATE_AT_TASK_COMPLETION --auto-terminate --region us-west-2
