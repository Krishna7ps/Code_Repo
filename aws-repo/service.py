import os
import time

while True:
    os.system("clear")
    print('''\nAvailable Tasks
    1.Service Status
    2.Service Stop
    3.Service Start
    ''')
    task=input("Enter Task number: ")
    if task=='1':
        os.system('fab -f ./fabfile.py set_host service_status -i ~/id -u cyb.kpattamsetty  --show everything')
        time.sleep(2)
        #service_status()
    elif task=='2':
        os.system('fab -f ./fabfile.py set_host service_stop -i ~/id -u cyb.kpattamsetty  --show everything')
        time.sleep(2)
        #service_stop()
    elif task=='3':
        os.system('fab -f ./fabfile.py set_host service_start -i ~/id -u cyb.kpattamsetty  --show everything')
        time.sleep(2)
        #service_start()
    else:
        print("\nInvalid selection..")
        time.sleep(2)

    if input("\nWant to try another service(y for yes)?: ")=='y':
        continue
    else:
        print("Good bye...")
        break



