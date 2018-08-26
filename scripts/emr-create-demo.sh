#DRY violations
S3_BUCKET=s3://philip-hadoop-bucket
SCRIPTS_DIR=$S3_BUCKET/scripts
QUERIES_DIR=$S3_BUCKET/queries



DEMO_NUMBER="005"
QUERY_TO_EXECUTE=demo-$DEMO_NUMBER.q
REGION=us-west-2
INSTANCE_TYPE=m3.xlarge #m3.large doesn't ever seem to work.

#I would like to add more parametrization here -- see below.
aws emr create-cluster --applications Name=Ganglia Name=Hadoop Name=Hive Name=Hue Name=Mahout Name=Pig Name=Tez --ec2-attributes '{"KeyName":"MainKeyPair","InstanceProfile":"EMR_EC2_DefaultRole","SubnetId":"subnet-4453270f","EmrManagedSlaveSecurityGroup":"sg-00286a3fc3b77d243","EmrManagedMasterSecurityGroup":"sg-03b92a0e407d74bab"}' --service-role EMR_DefaultRole --enable-debugging --release-label emr-5.16.0 --log-uri 's3n://philip-hadoop-bucket/' --steps '[{"Args":["hive-script","--run-hive-script","--args","-f",
"'$QUERIES_DIR'/'$QUERY_TO_EXECUTE'",
"-d","OUTPUT='$S3_BUCKET'/first-demo-query/output/'$DEMO_NUMBER'"],"Type":"CUSTOM_JAR","ActionOnFailure":"CONTINUE","Jar":"command-runner.jar","Properties":"","Name":"Demo '$DEMO_NUMBER' Demands by four selected countries"}
]' --name 'GDELT '$DEMO_NUMBER' demo' \
--instance-groups '[{"InstanceCount":1,"InstanceGroupType":"MASTER","InstanceType":"'$INSTANCE_TYPE'","Name":"Master demo '$DEMO_NUMBER'"},{"InstanceCount":1,"InstanceGroupType":"CORE","InstanceType":"'$INSTANCE_TYPE'","Name":"Core demo '$DEMO_NUMBER'"}]' \
--scale-down-behavior TERMINATE_AT_TASK_COMPLETION --auto-terminate --region $REGION

# INSTANCE_TYPE="m3.large" #m3.large may not be enough anyway
# echo "This doesn't appear to work because everything is so thoroughly escaped:"
# echo "$INSTANCE_TYPE"
# INSTANCE_GROUPS='[{"InstanceCount":1,"InstanceGroupType":"MASTER","InstanceType":"m3.xlarge","Name":"Master Instance Group"},{"InstanceCount":1,"InstanceGroupType":"CORE","InstanceType":"m3.xlarge","Name":"Core Instance Group"}]'


### FIRST FULL SCALE ATTEMPT, NOT WORKING

# $DEMO_NUMBER="003"
# $DEMO_DESCRIPTION="Count by actor country pairs"
# $INSTANCE_TYPE="m3.large" #was m3.xlarge, also second InstanceCount was 2
# $SCRIPT_TO_RUN="s3://philip-hadoop-bucket/first-demo-query/scripts/demo-$DEMO_NUMBER.q"
# # $REGION="us-west-2"
# $REGION="ap-south-1"  #Mumbai--to experiment, if not too expensive.
# aws emr create-cluster --applications Name=Ganglia Name=Hadoop Name=Hive Name=Hue Name=Mahout Name=Pig Name=Tez --ec2-attributes '{"KeyName":"MainKeyPair","InstanceProfile":"EMR_EC2_DefaultRole","SubnetId":"subnet-4453270f","EmrManagedSlaveSecurityGroup":"sg-00286a3fc3b77d243","EmrManagedMasterSecurityGroup":"sg-03b92a0e407d74bab"}' --service-role EMR_DefaultRole --enable-debugging --release-label emr-5.16.0 --log-uri 's3n://philip-hadoop-bucket/' --steps '[
#   {
#     "Args":[
#       "hive-script","--run-hive-script","--args","-f",
#       $SCRIPT_TO_RUN,
#       "-d",
#       "OUTPUT=s3://philip-hadoop-bucket/first-demo-query/output/003"
#     ],
#     "Type":"CUSTOM_JAR","ActionOnFailure":"CONTINUE","Jar":"command-runner.jar","Properties":"","Name":"Demo $DEMO_NUMBER $DEMO_DESCRIPTION"
#     }
# ]' --name 'GDELT Demo $DEMO_NUMBER' --instance-groups '[{"InstanceCount":1,"InstanceGroupType":"MASTER","InstanceType":"$INSTANCE_TYPE","Name":"Master Instance Group"},{
#     "InstanceCount":1,"InstanceGroupType":"CORE","InstanceType":"$INSTANCE_TYPE","Name":"Core Instance Group"}]' --scale-down-behavior TERMINATE_AT_TASK_COMPLETION --region us-west-2
