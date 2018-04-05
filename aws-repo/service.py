import os


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
    os.system('fab -f ./fabfile.py all -i ~/id -u cyb.kpattamsetty  --show everything')
    if input("Do you want to try for another client(y for yes)?:")=='y':
        pass
    else:
        print("Other than 'y', Quinting..")
        break