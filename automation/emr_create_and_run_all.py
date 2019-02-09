##############################################################################
# Start up a small AWS Elastic MapReduce (EMR) custer and load it with some
# predetermined steps.
# Python equivalent to scripts/emr-create-and-run-all.py
# See notes in comment block at the bottom.
###############################################################################

import os
import datetime
import boto3
import botocore.client
DEFAULT_APPLICATIONS_SET = 'hadoop'

#Following DRY violations- see sync-to-s3
S3_BUCKET = 'reed9999'
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

def handy_name():
    now = datetime.datetime.now()
    return 'boto3 EMR creation {}'.format(now.strftime('%a %R'))

# https://stackoverflow.com/questions/32410325/boto3-emr-hive-step
hive_script = 's3://reed9999/queries/feature_extraction/dyad_classification_features.q'
output = 's3://reed9999/output'
hive_args = "hive -v -f {} -hiveconf OUTPUT={}".format(hive_script, output).split()
HIVE_SCRIPT = {
            'Name': 'Load the dyad_classification_features table',
            'ActionOnFailure': 'CONTINUE',
            'HadoopJarStep': {
                'Properties': [
                    {
                        'Key': 'Hive',
                        'Value': 'True'
                    },
                ],
                'Jar': 'command-runner.jar',
                'Args': hive_args,
            }
        }

# Not sure if this inheritance will work properly....
# class EmrClient(botocore.client.BaseClient):
#     def __init__(self):
#         super(EmrClient, self).__init__('emr', )

class EmrClientWrapper():
    def __init__(self, region_name=None):
        region_name = region_name or REGION
        self.client = boto3.client('emr', region_name=region_name)
        self.instance_groups = []

    def append_instance_group(self, ig=None, name='Default name', instance_count=1,
                          instance_type=INSTANCE_TYPE, instance_role='MASTER', market='SPOT',):
        if ig is not None:
            self.instance_groups.append(ig)
        else:
            self.instance_groups.append({
                'InstanceCount': instance_count,
                'InstanceRole': instance_role,
                'InstanceType': instance_type,
                'Market': market,
                'Name': name,
            })

    def applications(self, set_chosen=None):
        set_chosen = set_chosen or DEFAULT_APPLICATIONS_SET
        return [{'Name': x} for x in APPLICATIONS_SETS[set_chosen]]

    def steps(self, steps_set='hive'):
        self.steps = [HIVE_SCRIPT] if steps_set == 'hive' else []
        return self.steps

    def run_job_flow(self): #Synonym to match weird/outdated boto3 terminology.
        self.create_cluster()

    def create_cluster(self):
        self.response = self.client.run_job_flow(
            # Un-hardcode these as I go....
            Name=handy_name(),
            LogUri='s3://{}/logs'.format(S3_BUCKET),
            # AdditionalInfo='string',
            # AmiVersion='string',
            ReleaseLabel='emr-4.6.0',
            Instances={
                'InstanceGroups': self.instance_groups
            },

            Steps=self.steps(),
            BootstrapActions=[],
            # SupportedProducts=[ #incompatible with Applications stating versions
            # ],
            Applications=self.applications(),
            VisibleToAllUsers=True,
            JobFlowRole='EMR_EC2_DefaultRole',
            ServiceRole='EMR_DefaultRole',
        )
        self.test_response()

    def test_response(self):
        if self.response:
            print("Succeded (probably). Here is response:\n")
            print(self.response)
        else:
            raise botocore.client.ClientError


wrapper = EmrClientWrapper(REGION)
wrapper.append_instance_group({
    'InstanceCount': 1,
    'InstanceRole': "MASTER",
    'InstanceType': INSTANCE_TYPE,
    'Market': "SPOT",
    'Name': "Master node",
})
wrapper.append_instance_group({
    'InstanceCount': 1,
    'InstanceRole': "CORE",
    'InstanceType': INSTANCE_TYPE,
    'Market': "SPOT",
    'Name': "Core node",
})
wrapper.create_cluster()





##
# Additional notes -- mostly for my own reference
# The doc is quite opaque but creating a cluster is called a "job flow," to my
# understanding.
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html
# https://github.com/aws-samples/aws-python-sample/issues/8


# Alternative Instances parameter when we don't use InstanceGroups:
#     'MasterInstanceType': INSTANCE_TYPE,
#     'SlaveInstanceType': INSTANCE_TYPE,
#     'InstanceCount': 2,
#     'Ec2KeyName' : 'MainKeyPair',
# },

# OLD_STEP_1 = {
#             'Name': 'Load the gdelt_events table',
#             'ActionOnFailure': 'CONTINUE',
#             'HadoopJarStep': {
#                 'Properties': [
#                     {
#                         'Key': 'string',
#                         'Value': 'string'
#                     },
#                 ],
#                 'Jar': 'command-runner.jar',
#                 # 'Args': [
#                 # ]
#             }
#         }
