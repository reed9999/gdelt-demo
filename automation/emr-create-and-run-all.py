##############################################################################
# NOT YET FUNCTIONAL -- Demo functionality works though, to list cluster names
# Start up a small AWS Elastic MapReduce (EMR) custer and load it with some
# predetermined steps.
# Python equivalent to scripts/emr-create-and-run-all.py
###############################################################################

import os
import boto3
# from pathlib import Path
# import awscli
# from awscli.clidriver import create_clidriver

#Following DRY violations- see sync-to-s3
S3_BUCKET = 'philip-hadoop-bucket'
SCRIPTS_DIR = os.path.join('automation', 'scripts')
QUERIES_DIR = os.path.join('queries')
# BASE_DIR = os.path.join(str(Path.home()), 'aws', 'gdelt-demo')


AUTOTERMINATE_OR_NOT = False
DEMO_NUMBER="003 through 006"
# REGION='us-west-2'
REGION='ap-south-1'
INSTANCE_TYPE='m1.large'

emr_client = boto3.client('emr')

example_clusters = emr_client.list_clusters(ClusterStates=['RUNNING', 'TERMINATED'])['Clusters']
# print([cluster['Name'] for cluster in example_clusters])
print("I have {} cluster[s]".format(len(example_clusters)))
print('**************************************************')
#### END THE DEMO, GET TO THE REAL CREATION


# The doc is quite opaque but a cluster here is called a "job flow," AFAICT
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html
# https://github.com/aws-samples/aws-python-sample/issues/8
# ecs_client = boto3.client('ecs')
# response = ecs_client.create_cluster('experimental')

response = emr_client.run_job_flow(
    Name='boto3 EMR creation test',
    # LogUri='string',
    # AdditionalInfo='string',
    # AmiVersion='string',
    ReleaseLabel='emr-4.6.0',
    Instances={
        'MasterInstanceType': 'm3.xlarge',
        'SlaveInstanceType': 'm1.large',
        'InstanceCount': 2,
        'Ec2KeyName' : 'MainKeyPair',
        # 'InstanceGroups': [
        #     {
        #         'Name': 'Master group (boto3 EMR creation test)',
        #         'Market': 'SPOT',
        #         'InstanceRole': 'MASTER',
        #         # 'BidPrice': 'string',
        #         'InstanceType': 'm3.xlarge',
        #         'InstanceCount': 1,
        #         'Configurations': [
        #             # {
        #             #     'Classification': 'string',
        #             #     'Configurations': {'... recursive ...'},
        #             #     'Properties': {
        #             #         'string': 'string'
        #             #     }
        #             # },
        #         ],
        #         # 'EbsConfiguration': {
        #         #     'EbsBlockDeviceConfigs': [
        #         #         {
        #         #             'VolumeSpecification': {
        #         #                 'VolumeType': 'string',
        #         #                 'Iops': 123,
        #         #                 'SizeInGB': 123
        #         #             },
        #         #             'VolumesPerInstance': 123
        #         #         },
        #         #     ],
        #         #     'EbsOptimized': True|False
        #         # },
        #         #####
        #         # 'AutoScalingPolicy': {
        #         #     'Constraints': {
        #         #         'MinCapacity': 123,
        #         #         'MaxCapacity': 123
        #         #     },
        #         #     'Rules': [
        #         #         {
        #         #             'Name': 'string',
        #         #             'Description': 'string',
        #         #             'Action': {
        #         #                 'Market': 'ON_DEMAND'|'SPOT',
        #         #                 'SimpleScalingPolicyConfiguration': {
        #         #                     'AdjustmentType': 'CHANGE_IN_CAPACITY'|'PERCENT_CHANGE_IN_CAPACITY'|'EXACT_CAPACITY',
        #         #                     'ScalingAdjustment': 123,
        #         #                     'CoolDown': 123
        #         #                 }
        #         #             },
        #         #             'Trigger': {
        #         #                 'CloudWatchAlarmDefinition': {
        #         #                     'ComparisonOperator': 'GREATER_THAN_OR_EQUAL'|'GREATER_THAN'|'LESS_THAN'|'LESS_THAN_OR_EQUAL',
        #         #                     'EvaluationPeriods': 123,
        #         #                     'MetricName': 'string',
        #         #                     'Namespace': 'string',
        #         #                     'Period': 123,
        #         #                     'Statistic': 'SAMPLE_COUNT'|'AVERAGE'|'SUM'|'MINIMUM'|'MAXIMUM',
        #         #                     'Threshold': 123.0,
        #         #                     'Unit': 'NONE'|'SECONDS'|'MICRO_SECONDS'|'MILLI_SECONDS'|'BYTES'|'KILO_BYTES'|'MEGA_BYTES'|'GIGA_BYTES'|'TERA_BYTES'|'BITS'|'KILO_BITS'|'MEGA_BITS'|'GIGA_BITS'|'TERA_BITS'|'PERCENT'|'COUNT'|'BYTES_PER_SECOND'|'KILO_BYTES_PER_SECOND'|'MEGA_BYTES_PER_SECOND'|'GIGA_BYTES_PER_SECOND'|'TERA_BYTES_PER_SECOND'|'BITS_PER_SECOND'|'KILO_BITS_PER_SECOND'|'MEGA_BITS_PER_SECOND'|'GIGA_BITS_PER_SECOND'|'TERA_BITS_PER_SECOND'|'COUNT_PER_SECOND',
        #         #                     'Dimensions': [
        #         #                         {
        #         #                             'Key': 'string',
        #         #                             'Value': 'string'
        #         #                         },
        #         #                     ]
        #         #                 }
        #         #             }
        #         #         },
        #         #     ]
        #         # }
        #         ##### AutoScalingPolicy
        #     },
        # ],
        # 'InstanceFleets': [
        #     {
        #         'Name': 'string',
        #         'InstanceFleetType': 'MASTER'|'CORE'|'TASK',
        #         'TargetOnDemandCapacity': 123,
        #         'TargetSpotCapacity': 123,
        #         'InstanceTypeConfigs': [
        #             {
        #                 'InstanceType': 'string',
        #                 'WeightedCapacity': 123,
        #                 'BidPrice': 'string',
        #                 'BidPriceAsPercentageOfOnDemandPrice': 123.0,
        #                 'EbsConfiguration': {
        #                     'EbsBlockDeviceConfigs': [
        #                         {
        #                             'VolumeSpecification': {
        #                                 'VolumeType': 'string',
        #                                 'Iops': 123,
        #                                 'SizeInGB': 123
        #                             },
        #                             'VolumesPerInstance': 123
        #                         },
        #                     ],
        #                     'EbsOptimized': True|False
        #                 },
        #                 'Configurations': [
        #                     {
        #                         'Classification': 'string',
        #                         'Configurations': {'... recursive ...'},
        #                         'Properties': {
        #                             'string': 'string'
        #                         }
        #                     },
        #                 ]
        #             },
        #         ],
        #         'LaunchSpecifications': {
        #             'SpotSpecification': {
        #                 'TimeoutDurationMinutes': 123,
        #                 'TimeoutAction': 'SWITCH_TO_ON_DEMAND'|'TERMINATE_CLUSTER',
        #                 'BlockDurationMinutes': 123
        #             }
        #         }
        #     },
        # ],
        # 'Ec2KeyName': 'string',
        # 'Placement': {
        #     'AvailabilityZone': 'string',
        #     'AvailabilityZones': [
        #         'string',
        #     ]
        # },
        # 'KeepJobFlowAliveWhenNoSteps': True|False,
        # 'TerminationProtected': True|False,
        # 'HadoopVersion': 'string',
        # 'Ec2SubnetId': 'string',
        # 'Ec2SubnetIds': [
        #     'string',
        # ],
        # 'EmrManagedMasterSecurityGroup': 'string',
        # 'EmrManagedSlaveSecurityGroup': 'string',
        # 'ServiceAccessSecurityGroup': 'string',
        # 'AdditionalMasterSecurityGroups': [
        #     'string',
        # ],
        # 'AdditionalSlaveSecurityGroups': [
        #     'string',
        # ] InstanceGroups
    },
    Steps=[
        {
            'Name': 'Load the gdelt_events table',
            'ActionOnFailure': 'TERMINATE_CLUSTER',
            # or 'TERMINATE_JOB_FLOW'|'CANCEL_AND_WAIT'|'CONTINUE',
            'HadoopJarStep': {
                'Properties': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'Jar': 'command-runner.jar',
                # 'MainClass': 'string',
                'Args': [
                ]
            }
        },
    ],
    BootstrapActions=[
        # {
        #     'Name': 'string',
        #     'ScriptBootstrapAction': {
        #         'Path': 'string',
        #         'Args': [
        #             'string',
        #         ]
        #     }
        # },
    ],
    # SupportedProducts=[
    #     'hue',
    #     'ganglia',
    #     'tez',
    # ],
    # NewSupportedProducts=[
    #     # {
    #     #     'Name': 'string',
    #     #     'Args': [
    #     #         'string',
    #     #     ]
    #     # },
    # ],
    Applications=[
        {
            'Name': 'Hadoop',
            # 'Version': 'string',
            # 'Args': [
            #     'string',
            # ],
            # 'AdditionalInfo': {
            #     'string': 'string'
            # }
        },
        { 'Name': 'Hive',},
        { 'Name': 'Mahout',},
        { 'Name': 'Hue',},
        { 'Name': 'Ganglia',},
        # { 'Name': 'Tez',},
    ],
    # Configurations=[
    #     {
    #         'Classification': 'string',
    #         'Configurations': {'... recursive ...'},
    #         'Properties': {
    #             'string': 'string'
    #         }
    #     },
    # ],
    VisibleToAllUsers=True,
    JobFlowRole='EMR_EC2_DefaultRole',
    ServiceRole='EMR_DefaultRole',
    # Tags=[
    #     {
    #         'Key': 'string',
    #         'Value': 'string'
    #     },
    # ],
    # SecurityConfiguration='string',
    # AutoScalingRole='string',
    # ScaleDownBehavior= ???
        #Not for this release 'TERMINATE_AT_INSTANCE_HOUR',
    # CustomAmiId='string',
    # EbsRootVolumeSize=123,
    # RepoUpgradeOnBoot='SECURITY'|'NONE',
    # KerberosAttributes={
    #     'Realm': 'string',
    #     'KdcAdminPassword': 'string',
    #     'CrossRealmTrustPrincipalPassword': 'string',
    #     'ADDomainJoinUser': 'string',
    #     'ADDomainJoinPassword': 'string'
    # }
)

################################################################################
# aws emr create-cluster --applications Name=Ganglia Name=Hadoop Name=Hive Name=Hue Name=Mahout Name=Pig Name=Tez --ec2-attributes '{"KeyName":"MainKeyPair","InstanceProfile":"EMR_EC2_DefaultRole","SubnetId":"subnet-4453270f","EmrManagedSlaveSecurityGroup":"sg-00286a3fc3b77d243","EmrManagedMasterSecurityGroup":"sg-03b92a0e407d74bab"}' --service-role EMR_DefaultRole --enable-debugging --release-label emr-5.16.0 --log-uri 's3n://philip-hadoop-bucket/' --steps '[{"Args":["hive-script","--run-hive-script","--args","-f","'$QUERIES_DIR'/load-gdelt-events.q","-d","OUTPUT='$S3_BUCKET'/output/all"],"Type":"CUSTOM_JAR","ActionOnFailure":"CONTINUE","Jar":"command-runner.jar","Properties":"=","Name":"Load the gdelt_events table"},
# {"Args":["hive-script","--run-hive-script","--args","-f","'$QUERIES_DIR'/demo-005.q","-d","OUTPUT='$S3_BUCKET'/output/005"],"Type":"CUSTOM_JAR","ActionOnFailure":"CONTINUE","Jar":"command-runner.jar","Properties":"","Name":"Demo 005"},
# {"Args":["hive-script","--run-hive-script","--args","-f","'$QUERIES_DIR'/demo-009.q","-d","OUTPUT='$S3_BUCKET'/output/009"],"Type":"CUSTOM_JAR","ActionOnFailure":"CONTINUE","Jar":"command-runner.jar","Properties":"","Name":"Demo 009"},
# {"Args":["hive-script","--run-hive-script","--args","-f","'$QUERIES_DIR'/demo-010.q","-d","OUTPUT='$S3_BUCKET'/output/010"],"Type":"CUSTOM_JAR","ActionOnFailure":"CONTINUE","Jar":"command-runner.jar","Properties":"","Name":"Demo 010"} ]' --name 'GDELT all demo' --instance-groups '[{"InstanceCount":1,"InstanceGroupType":"CORE","InstanceType":"m3.xlarge","Name":"Core demo all"},{"InstanceCount":1,"InstanceGroupType":"MASTER","InstanceType":"m3.xlarge","Name":"Master demo all"}]' --scale-down-behavior TERMINATE_AT_TASK_COMPLETION $AUTOTERMINATE_OR_NOT --region us-west-2
