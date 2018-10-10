## Script to create a cluster that's very much like the one I called 3.1 on 2018-10-09
# As it gets more parametrized my naming convention may change. 

# There is still the unresolved problem that this isn't designating  a key to 
# connect so I can't access SSH

aws emr create-cluster \
--applications Name=Ganglia Name=Hadoop Name=Hive Name=Hue Name=Mahout Name=Pig Name=Tez \
--tags 'WhatsNew=Parameters for smaller DB' 'Hadoop=1' 'CliAutomation=1' \
--ec2-attributes InstanceProfile=EMR_EC2_DefaultRole \
--release-label emr-5.16.0 --log-uri 's3n://philip-hadoop-bucket/__archive/' \
--bootstrap-actions Path="s3://reed9999/automation/scripts/emr-bootstrap.sh" \
--steps '[
  {"Args":["hive-script", "--run-hive-script", "--args", "-f","s3://reed9999/queries/data-engineering/hive/load-mini-gdelt-events.q", "-d","INPUT=s3://reed9999/events/subset/small", "-d","OUTPUT=s3://reed9999/output/step0.0","-hiveconf", "hive.support.sql11.reserved.keywords=false"],"Type":"CUSTOM_JAR","ActionOnFailure":"CONTINUE","Jar":"command-runner.jar","Properties":"","Name":"step 0.0 load small subset of DB"},
  {"Args":["hive-script","--run-hive-script","--args","-f","s3://reed9999/queries/feature_extraction/dyad_classification_features.q","-d","INPUT=s3://reed9999/data/subset/small","-d","OUTPUT=s3://reed9999/output/step0.1","-hiveconf","hive.support.sql11.reserved.keywords=false"],"Type":"CUSTOM_JAR","ActionOnFailure":"CONTINUE","Jar":"command-runner.jar","Properties":"","Name":"step 1.0 last cluster grand finale, failed because of forgotten DROP TABLE"}]' \
--instance-groups '[{"InstanceCount":1,"BidPrice":"OnDemandPrice","InstanceGroupType":"CORE","InstanceType":"m1.large","Name":"Core Instance Group"},
  {"InstanceCount":1,"BidPrice":"OnDemandPrice","InstanceGroupType":"MASTER","InstanceType":"m1.large","Name":"Master Instance Group"}]' \
--ebs-root-volume-size 10 --service-role EMR_DefaultRole \
--enable-debugging --name '3.2 (replica of 3.1) Fixed missing DROP TABLE ' \
--scale-down-behavior TERMINATE_AT_TASK_COMPLETION --region us-west-2
