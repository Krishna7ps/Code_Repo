import os
import time
from fabric.colors import green,red,yellow,white,cyan,magenta,blue
while True:
    os.system("clear")
    print(white('''\nAvailable Tasks
    1.Service Status
    2.Service Stop
    3.Service Start
    '''))
    task=input("Enter Task number: ")
    if task=='1':
        os.system('fab -f ./fabfile.py set_host service_status  -u cyb.kpattamsetty  --show everything')
        time.sleep(2)
        #service_status()
    elif task=='2':
        os.system('fab -f ./fabfile.py set_host service_stop  -u cyb.kpattamsetty  --show everything')
        time.sleep(2)
        #service_stop()
    elif task=='3':
        os.system('fab -f ./fabfile.py set_host service_start  -u cyb.kpattamsetty  --show everything')
        time.sleep(2)
        #service_start()
    else:
        print(red("\nInvalid selection.."))
        time.sleep(2)

    if input(blue("\nWant to try another service(y for yes)?: "))=='y':
        continue
    else:
        print(magenta("Good Bye..."))
        break



