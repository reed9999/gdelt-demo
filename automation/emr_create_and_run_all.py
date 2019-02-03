##############################################################################
# Start up a small AWS Elastic MapReduce (EMR) custer and load it with some
# predetermined steps.
# Python equivalent to scripts/emr-create-and-run-all.py
# See notes in comment block at the bottom.
###############################################################################

import os
import boto3
APPLICATIONS_SET_CHOSEN = 'spark'

#Following DRY violations- see sync-to-s3
S3_BUCKET = 'philip-hadoop-bucket'
SCRIPTS_DIR = os.path.join('automation', 'scripts')
QUERIES_DIR = os.path.join('queries')


AUTOTERMINATE_OR_NOT = False
DEMO_NUMBER = "003 through 006"
REGION = 'us-west-2'
# REGION = 'ap-south-1'
INSTANCE_TYPE = 'm1.large'

APPLICATIONS_SETS = {
    'hadoop': ['Hadoop', 'Hive', 'Mahout', 'Hue', 'Ganglia',],
    'spark': ['Pig', 'Spark', ]
}

OLD_STEP_1 = {
            'Name': 'Load the gdelt_events table',
            'ActionOnFailure': 'CONTINUE',
            'HadoopJarStep': {
                'Properties': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'Jar': 'command-runner.jar',
                # 'Args': [
                # ]
            }
        }

NEW_STEP_1 = {
            'Name': 'Load the gdelt_events table',
            'ActionOnFailure': 'CONTINUE',
            'HadoopJarStep': {
                'Properties': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'Jar': 'command-runner.jar',
                'Args': [ '--help',
                    'Is there a jar to run PySpark steps?'],
            }
        }

emr_client = boto3.client('emr', region_name=REGION)
# See https://stackoverflow.com/a/27768332/742573
# However it seems at some point they got rid of the boto3.emr module (maybe?) so
# from boto3.emr.instance_group import InstanceGroup
# is no longer the way to do this!

instance_groups = []
instance_groups.append({
    'InstanceCount': 1,
    'InstanceRole': "MASTER",
    'InstanceType': INSTANCE_TYPE,
    'Market': "SPOT",
    'Name': "Master node",
})
instance_groups.append({
    'InstanceCount': 1,
    'InstanceRole': "CORE",
    'InstanceType': INSTANCE_TYPE,
    'Market': "SPOT",
    'Name': "Core node",
})

response = emr_client.run_job_flow(
    Name='boto3 EMR creation test 2',
    # LogUri='string',
    # AdditionalInfo='string',
    # AmiVersion='string',
    ReleaseLabel='emr-4.6.0',
    # Has to be either instance_groups or Instances.
    Instances={
        'InstanceGroups': instance_groups
    },
    #     'MasterInstanceType': INSTANCE_TYPE,
    #     'SlaveInstanceType': INSTANCE_TYPE,
    #     'InstanceCount': 2,
    #     'Ec2KeyName' : 'MainKeyPair',
    # },

    Steps=[
    ],
    BootstrapActions=[],
    # SupportedProducts=[ #incompatible with Applications stating versions
        # I think (cryptic error message)
        # Tez is all that's missing but I don't know if that's a problem.
    #     'tez',
    # ],
    Applications=[
        {'Name': x} for x in APPLICATIONS_SETS[APPLICATIONS_SET_CHOSEN]
    ],
    VisibleToAllUsers=True,
    JobFlowRole='EMR_EC2_DefaultRole',
    ServiceRole='EMR_DefaultRole',
    # ScaleDownBehavior='TERMINATE_AT_INSTANCE_HOUR',

)

if response:
    print("Succeded (probably). Here is response:\n")
    print(response)


##
# Additional notes -- mostly for my own reference
# The doc is quite opaque but creating a cluster is called a "job flow," to my
# understanding.
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html
# https://github.com/aws-samples/aws-python-sample/issues/8
