import os
import time
from fabric.colors import green,red,yellow,white,cyan,magenta,blue
while True:
    os.system("clear")
    print(white('''\nAvailable Tasks
    1.Service Status
    2.Service Stop and/or Start
    3.Service Start
    4.Purge Logs
    5.Delete S3 Obejcts
    6.Install Package
    '''))
    task=input("Enter Task number: ")
    if task=='1':
        os.system('fab -f ./fabfile.py set_host service_status  -u cyb.kpattamsetty  --show everything')
        
        #service_status()
    elif task=='2':
        os.system('fab -f ./fabfile.py set_host service_stop  -u cyb.kpattamsetty  --show everything')
        
        #service_stop()
    elif task=='3':
        os.system('fab -f ./fabfile.py set_host service_start  -u cyb.kpattamsetty  --show everything')
        
        #service_start()
    elif task=='6':
        os.system('fab -f ./fabfile.py set_host hostname  -u cyb.kpattamsetty  --show everything')
    else:
        print(red("\nInvalid selection.."))
        

    if input(blue("\nWant to try another service(y for yes)?: "))=='y':
        continue
    else:
        print(magenta("Good Bye..."))
        break



