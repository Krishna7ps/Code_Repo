import boto3
#import pprint

ec2=boto3.client('ec2')

sg=ec2.describe_security_groups()

# print("List of security groups:")
for i in range(len(sg['SecurityGroups'])):
    if sg['SecurityGroups'][i]['GroupName'] == 'default':
        print("Default SG can't be deleted")
    else:
        try:
            del_g=ec2.delete_security_group(GroupName=sg['SecurityGroups'][i]['GroupName'])
            if del_g['ResponseMetadata']['HTTPStatusCode']==200:
                print(sg['SecurityGroups'][i]['GroupName'],"is deleted")
        except:
            print("Some error occurred while deleting ",sg['SecurityGroups'][i]['GroupName'])


    