import os
import ipaddress


print("1.uname \n2.hostname \n3.Service status")
ip=input("Please enter task number to perform: ")
#host= ipaddress.ip_address('172.31.12.150')

if(ip==1):
    os.system('fab  -f ./fabfile.py uname -i ~/id -u cyb.kpattamsetty --sudo-password $DAP --show everything')
if(ip==2):
    os.system('fab  -f ./fabfile.py hostname -i ~/id -u cyb.kpattamsetty --sudo-password $DAP --show everything')
if(ip==3):
    os.system('fab  -f ./fabfile.py service_status -i ~/id -u cyb.kpattamsetty --sudo-password $DAP --show everything')