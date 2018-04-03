s3l=boto3.client('s3') #Creating s3 boto3 object
s3_objects=s3l.list_objects(Bucket='lakana-techops-assets-us-east-1')['Contents']
no_of_objs=len(s3_objects)
for i in range(no_of_objs):
    obj_download=s3_objects[i]['Key']
    s3l.download_file('lakana-techops-assets-us-east-1',obj_download,obj_download)