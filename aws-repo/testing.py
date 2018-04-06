import boto3

ec2=boto3.client('ec2')

while True:
    servers_list=[]
    client=input("client: ")
    environment=input("environment: ")
    sys_type=input("sys_type: ")
    fulldata=ec2.describe_instances(Filters=[{'Name':'tag:client','Values':[client]},{'Name':'tag:env','Values':[environment]},{'Name':'tag:system_type','Values':[sys_type]}])
    for i in range(len(fulldata['Reservations'])):
        servers_list+=[y["Value"] for y in [x for x in fulldata['Reservations'][i]["Instances"][0]['Tags']] if y["Key"]=="Name"]
    for i in range(len(servers_list)):
        print(servers_list[i])
        
    if input("proceed: ")=='n':
        break
