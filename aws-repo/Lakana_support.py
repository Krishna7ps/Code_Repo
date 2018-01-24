
#listing buckets and objects of each bucket

for i in range(len(s3.list_buckets()['Buckets'])):
    buck=s3.list_buckets()['Buckets'][i]['Name']
    pprint.pprint(s3.list_objects(Bucket=buck))
    time.sleep(1000)
    
#Listing each object that CacheControl metadata set
count=0
for i in range(len(s3.list_buckets()['Buckets'])):
    buck=s3.list_buckets()['Buckets'][i]['Name']
    pprint.pprint('Bucket=',buck)
    print('\n'*3)
    if count==4:
        break
    try:
        for j in range(len(s3.list_objects(Bucket=buck)['Contents'])):
            obj=s3.list_objects(Bucket=buck)['Contents'][j]['Key']
#            pprint.pprint("Object=",obj)
            rep=s3.get_object(Bucket=buck,Key=obj)
            if rep['CacheControl']:
                print(obj,"set CacheControl=",rep['CacheControl'])
                count=count+1
                
    except:
        pass

#Setting up assumerole on boto3

sts=boto3.client('sts')
res=sts.assume_role(RoleArn='arn:aws:iam::462397709356:role/lakana-fox-admin',RoleSessionName='testrole')

s3=boto3.client('s3',aws_access_key_id=res['Credentials']['AccessKeyId'],
aws_secret_access_key=res['Credentials']['SecretAccessKey'],
aws_session_token=res['Credentials']['SessionToken'])

