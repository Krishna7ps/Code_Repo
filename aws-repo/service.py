''' from fabric.api import run, env
from fabric.tasks import execute 
import boto3
'''
import os
import time


'''
print("1.Service Status \n2.Service Stop \n3.Service Start")
ip=input("Please enter task number to perform: ")
#host= ipaddress.ip_address('172.31.12.150')

if(ip==1):
    os.system('fab -f ./fabfile.py all uname -i ~/id -u cyb.kpattamsetty  --show everything')
if(ip==2):
    os.system('fab  -f ./fabfile.py all hostname -i ~/id -u cyb.kpattamsetty  --show everything')
if(ip==3):
    os.system('fab  -f ./fabfile.py all service_status -i ~/id -u cyb.kpattamsetty  --show everything')
    '''
    

    

while True:
    print('''\nAvailable Tasks
    1.Service Status
    2.Service Stop
    3.Service Start
    ''')
    task=input("Enter Task number: ")
    if task=='1':
        os.system('fab -f ./fabfile.py set_host service_status -i ~/id -u cyb.kpattamsetty  --show everything')
        #service_status()
    elif task=='2':
        os.system('fab -f ./fabfile.py service_stop -i ~/id -u cyb.kpattamsetty  --show everything')
        #service_stop()
    elif task=='3':
        os.system('fab -f ./fabfile.py service_start -i ~/id -u cyb.kpattamsetty  --show everything')
        #service_start()
    else:
        print("Choice not available")
    if input("Want to try another service(y for yes)?: ")=='y':
        continue
    else:
        break



'''
while True:
    os.system('fab -f ./fabfile.py all -i ~/id -u cyb.kpattamsetty  --show everything')
    x=input("Do you want to try for another client(1 for yes)?:")
    print(x)
    if x=='1':
        continue
    else:
        print("Other than y, Quinting..")
        break
        '''