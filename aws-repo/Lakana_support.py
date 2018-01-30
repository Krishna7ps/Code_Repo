'''
Points to remember

1. Better practice to store API call output in a variable.
2. Avoid calling API calls in loops. Instead use variables.



'''

# python modules that you should aware of to do basic automations

import requests
import win32com.client
import pywinauto
import pyautogui
import urllib.request  #Equivalent to urllib2 in python3
import logging
import boto3
import subprocess
import json
import random
import os
import sys
import fabric3
import re
import glob
import fnmatch
import selenium


#Setting up assumerole on boto3

sts=boto3.client('sts')
res=sts.assume_role(RoleArn='arn:aws:iam::462397709356:role/lakana-fox-admin',RoleSessionName='testrole')

s3=boto3.client('s3',aws_access_key_id=res['Credentials']['AccessKeyId'],
aws_secret_access_key=res['Credentials']['SecretAccessKey'],
aws_session_token=res['Credentials']['SessionToken'])  


#listing buckets and objects of each bucket

for i in range(len(s3.list_buckets()['Buckets'])):
    buck=s3.list_buckets()['Buckets'][i]['Name']
    pprint.pprint(s3.list_objects(Bucket=buck))
    time.sleep(1000)
    
#Listing each object that CacheControl metadata set

API_list_buckets
count=0
for i in range(len(s3.list_buckets()['Buckets'])):
    buck=API_list_buckets['Buckets'][i]['Name']
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


#listing buckets, objects, Keys 

s3l=boto3.client('s3') #Creating s3 boto3 object
s3_buckets=s3l.list_buckets() #Listing buckets under the account

s3_objects=s3l.list_objects(Bucket='lakana-cloudformation')['Contents']
no_of_objs=len(s3_objects)
for i in range(no_of_objs):
    print(s3_obje_ts[i]['Key']) #Listing object keys under specific bucket

s3_objects=s3l.list_objects(Bucket='lakana-cloudformation')['Contents']
no_of_objs=len(_)
for i in range(no_of_objs):
    if s3_objects[i]['Key'].startswith('platform'):
        print(s3_objects[i]['Key']) #Listing object keys those starts with specific word

'''
Exam
import boto3
s3 = boto3.resource('s3')
s3.meta.client.download_file('mybucket', 'hello.txt', '/tmp/hello.txt')

'''

#Downloading objects from specific s3 bucket with specific word they start with

s3_objects=s3l.list_objects(Bucket='lakana-cloudformation')['Contents']
no_of_objs=len(s3_objects)
for i in range(no_of_objs):
    if s3_objects[i]['Key'].startswith('platform/v37'):
        obj_download=s3_objects[i]['Key']
        s3l.download_file('lakana-cloudformation',obj_download,obj_download.split('/')[-1])