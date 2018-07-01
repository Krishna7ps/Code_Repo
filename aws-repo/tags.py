import boto3
rds=boto3.client("rds")    
iden=['adk','dev','qa','sandbox','stage','uat']
cli=['cmg','fox','gmg','lakananews','mtss','nxs','sps','tegna']
idents=[]
for i in cli:
    for j in iden:
        idents=idents+[i+'-'+j]

res=rds.list_tags_for_resource(ResourceName="arn:aws:rds:us-east-1:127246258661:db:tegna-sandbox")
for i in range(len(res)):
    print(res[i]['Key']," ---> ",res[i]["Value"])

des=rds.describe_db_instances()
des=rds.describe_db_instances(DBInstanceIdentifier='tegna-sandbox')
des["DBInstances"][0]['DBInstanceArn']
des["DBInstances"][0]['DBInstanceIdentifier']


import boto3                            
    ...: rds=boto3.client("rds")                                          
    ...: des=rds.describe_db_instances()                                
    ...: for i in range(len(des["DBInstances"])):                       
    ...:     if des["DBInstances"][i]["DBInstanceIdentifier"] in idents:                                           
    ...:         print(des["DBInstances"][i]['DBInstanceIdentifier'])
    ...:         arn=des["DBInstances"][i]['DBInstanceArn']       
    ...:         res=rds.list_tags_for_resource(ResourceName=arn) 
    ...:         for j in range(len(res)):                        
    ...:             print(res[j]['Key']," ---> ",res[j]["Value"])

 for i in range(len(des["DBInstances"])):                       
    ...:     if des["DBInstances"][i]["DBInstanceIdentifier"] in idents:    
    ...:         print(des["DBInstances"][i]["DBInstanceIdentifier"],"-"*20)      
    ...:         metadata=des["DBInstances"][i]["DBInstanceIdentifier"].split('-')
    ...:         print(metadata)                           
    ...:         arn=des["DBInstances"][i]['DBInstanceArn']      
    ...:         res=rds.list_tags_for_resource(ResourceName=arn)
    ...:         for j in range(len(res["TagList"])):                                   
    ...:             print(res["TagList"][j]['Key']," ---> ",res["TagList"][j]["Value"])
    ...:         time.sleep(2)



response = client.add_tags_to_resource(ResourceName='string',Tags=[{'Key': 'string','Value': 'string'},])

des=rds.describe_db_instances()
for i in range(len(des["DBInstances"])):
    fy=des["DBInstances"][i]["DBInstanceIdentifier"]
    if fy in idents:
        print("-"*30,fy,"-"*30)
        metadata=fy.split('-')
        arn=des["DBInstances"][i]['DBInstanceArn']
        response = rds.add_tags_to_resource(ResourceName=arn,Tags=[{'Key': 'Name','Value':fy},{'Key': 'client','Value':metadata[0]},{'Key': 'env','Value':metadata[1]}])
        res=rds.list_tags_for_resource(ResourceName=arn)
        for j in range(len(res["TagList"])):
            print("{0:>15}   --->   {1:<15}".format(res["TagList"][j]['Key'],res["TagList"][j]["Value"]))
        time.sleep(2)      

if fy in idents:
    print(fy,"-"*20)
    metadata=fy.split('-')
    print(metadata)
    arn='arn:aws:rds:us-east-1:127246258661:db:cmg-sandbox'
    res=rds.list_tags_for_resource(ResourceName=arn)
    response = rds.add_tags_to_resource(ResourceName=arn,Tags=[{'Key': 'Name','Value':fy}])

[{'Key': 'system_type', 'Value': 'postgres'},
 {'Key': 'lifespan', 'Value': '1time'},
 {'Key': 'client', 'Value': 'sps'},
 {'Key': 'workload-type', 'Value': 'lowerdb'},
 {'Key': 'env', 'Value': 'sandbox'},
 {'Key': 'Name', 'Value': 'sps-sandbox'}]
[{'Key': 'system_type', 'Value': 'postgres'},
 {'Key': 'lifespan', 'Value': '1time'},
 {'Key': 'client', 'Value': 'sps'},
 {'Key': 'workload-type', 'Value': 'lowerdb'},
 {'Key': 'env', 'Value': 'sandbox'},
 {'Key': 'Name', 'Value': 'sps-sandbox'}]
[{'Key': 'system_type', 'Value': 'postgres'},
 {'Key': 'lifespan', 'Value': '1time'},
 {'Key': 'client', 'Value': 'sps'},
 {'Key': 'workload-type', 'Value': 'qa'},
 {'Key': 'env', 'Value': 'qa'},
 {'Key': 'Name', 'Value': 'sps-qa'}]
[{'Key': 'system_type', 'Value': 'postgres'},
 {'Key': 'lifespan', 'Value': '1time'},
 {'Key': 'client', 'Value': 'sps'},
 {'Key': 'workload-type', 'Value': 'lowerdb'},
 {'Key': 'env', 'Value': 'sandbox'},
 {'Key': 'Name', 'Value': 'sps-sandbox'}]
[{'Key': 'system_type', 'Value': 'postgres'},
 {'Key': 'lifespan', 'Value': '1time'},
 {'Key': 'client', 'Value': 'sps'},
 {'Key': 'workload-type', 'Value': 'stage'},
 {'Key': 'env', 'Value': 'stage'},
 {'Key': 'Name', 'Value': 'sps-stage'}]
[{'Key': 'system_type', 'Value': 'postgres'},
 {'Key': 'lifespan', 'Value': '1time'},
 {'Key': 'client', 'Value': 'sps'},
 {'Key': 'workload-type', 'Value': 'lowerdb'},
 {'Key': 'env', 'Value': 'sandbox'},
 {'Key': 'Name', 'Value': 'sps-sandbox'}]
[{'Key': 'system_type', 'Value': 'postgres'},
 {'Key': 'lifespan', 'Value': '1time'},
 {'Key': 'client', 'Value': 'sps'},
 {'Key': 'workload-type', 'Value': 'lowerdb'},
 {'Key': 'env', 'Value': 'sandbox'},
 {'Key': 'Name', 'Value': 'sps-sandbox'}]

 import time
     ...: for i in envr:
     ...:     print('*'*25,i,'*'*25)
     ...:     des=rds.describe_db_instances(DBInstanceIdentifier='sps-'+i)
     ...:     arn=des['DBInstances'][0]['DBInstanceArn']
     ...:     pprint.pprint(rds.list_tags_for_resource(ResourceName=arn)['TagList'][-2:])
     ...:     print()
     ...:     res=rds.add_tags_to_resource(ResourceName=arn,Tags=[{'Key': 'Name','Value':'sps-'+i},{'Key': 'client','Value':'s
     ...: ps'},{'Key': 'env','Value':i}])
     ...:     #print(res)
     ...:     pprint.pprint(rds.list_tags_for_resource(ResourceName=arn)['TagList'])
     ...:     
     ...:     
