
client=''
environment=''
sys_type=''


def all():
    
    global client
    global environment
    global sys_type
    

    ec2=boto3.client('ec2')
    
    print('''Choose client from the list
    1.tegna
    2.nxs
    3.mtss
    4.sps
    5.gmg
    6.cmg
    7.fox
    \n ''')

    x=input("Enter client number: ")
    os.system("clear")

    
    if(x=='1'):
        client='tegna'
    if(x=='2'):
        client='nxs'
    if(x=='3'):
        client='mtss'
    if(x=='4'):
        client='sps'
    if(x=='5'):
        client='gmg'
    if(x=='6'):
        client='cmg'
    if(x=='7'):
        client='fox'
    
    #print("client is ",client)
 
    print('''\nChoose environment
    1.prod
    2.dev
    3.uat
    4.stage
    5.qa
    \n''')
    y=input("Enter enviroment number: ")
    os.system("clear")
    if(y=='1'):
        environment='prod'
    if(y=='2'):
        environment='dev'
    if(y=='3'):
        environment='uat'
    if(y=='4'):
        environment='stage'
    if(y=='5'):
        environment='qa'
    print('''\nchoose system type
    1.cms
    2.web
    3.feed
    \n''')
    z=input("Enter system type number: ")
    os.system("clear")
    if(z=='1'):
        sys_type='cms'
    if(z=='2'):
        sys_type='web'
    if(z=='3'):
        sys_type='feed'
    
    
    shortName=input("Enter instance short name(EX: cms01,web06,feed01): ")
    keyInstance=client+"-"+environment+"-"+shortName+"-us-east-1"
    #print(keyInstance)
    env.hosts=[]
    response=ec2.describe_instances(Filters=[{'Name':'tag:client','Values':[client]},{'Name':'tag:env','Values':[environment]},{'Name':'tag:system_type','Values':[sys_type]},{"Name":'tag:Name','Values':[keyInstance]}])
    
    print("Info: %s --> %s"%(keyInstance,response['Reservations'][0]["Instances"][0]["PrivateIpAddress"]))
    env.hosts.append(response['Reservations'][0]["Instances"][0]["PrivateIpAddress"])
    print("Env hosts is: ",env.hosts)
    

    while True:
        print('''\nAvailable Tasks
        1.Service Status
        2.Service Stop
        3.Service Start
        ''')
        task=input("Enter Task number: ")
        if task=='1':
            service_status()
        elif task=='2':
            service_stop()
        elif task=='3':
            service_start()
        else:
            print("Choice not available")
        if input("Want to try another service(y for yes)?: ")=='y':
            continue
        else:
            break
    '''
    response=ec2.describe_instances(Filters=[{'Name':'tag:client','Values':[client]},{'Name':'tag:env','Values':[environment]},{'Name':'tag:system_type','Values':[system_type]}])
    for i in range(len(response['Reservations'])):
        for j in range(len(response['Reservations'][i]["Instances"][0]["Tags"])):
            if(response['Reservations'][i]["Instances"][0]["Tags"][j]["Key"])=="Name":
                print("%d %s" %(j,response['Reservations'][i]["Instances"][0]["Tags"][j]["Value"]))
                #servers=[]
                #servers.append(response['Reservations'][i]["Instances"][0]["Tags"][j]["Value"])
                
    env.hosts=[] #['172.31.12.150']
    keyvalue=input("Enter server short name(EX: web01, cms03, feed02): ")
    for i in range(len(response['Reservations'])):
        for j in range(len(response['Reservations'][i]["Instances"][0]["Tags"])):
            if keyvalue in response['Reservations'][i]["Instances"][0]["Tags"][j]["Value"]:
                print("\n%s ----> %s"%(response['Reservations'][i]["Instances"][0]["Tags"][j]["Value"],response['Reservations'][i]["Instances"][0]["PrivateIpAddress"]))
    
    print("\n{} ----> {}".format((a["Value"] for a in response['Reservations'][0]["Instances"][0]["Tags"]if a["Key"]=="Name"), response['Reservations'][0]["Instances"][0]["PrivateIpAddress"]))
    '''
    #print(keyInstance,"-------------->",response['Reservations'][0]["Instances"][0]["PrivateIpAddress"])

    '''
def actions():
    print("1.uname \n2.hostname \n3.Service status")
    ip=input("Please enter task number to perform: ")
    if (ip==1):
        print(run("uname -s"))
    if(ip==2):
        run("hostname")
    if(ip==3):
        run("service liferay status")
    
'''


ec2=boto3.client('ec2')

print('''Choose client from the list
1.tegna
2.nxs
3.mtss
4.sps
5.gmg
6.cmg
7.fox
\n ''')
x=input("Enter client number: ")
os.system("clear")

if(x=='1'):
    client='tegna'
if(x=='2'):
    client='nxs'
if(x=='3'):
    client='mtss'
if(x=='4'):
    client='sps'
if(x=='5'):
    client='gmg'
if(x=='6'):
    client='cmg'
if(x=='7'):
    client='fox'

#print("client is ",client)
print('''\nChoose environment
1.prod
2.dev
3.uat
4.stage
5.qa
\n''')
y=input("Enter enviroment number: ")
os.system("clear")
if(y=='1'):
    environment='prod'
if(y=='2'):
    environment='dev'
if(y=='3'):
    environment='uat'
if(y=='4'):
    environment='stage'
if(y=='5'):
    environment='qa'
print('''\nchoose system type
1.cms
2.web
3.feed
\n''')
z=input("Enter system type number: ")
os.system("clear")
if(z=='1'):
    sys_type='cms'
if(z=='2'):
    sys_type='web'
if(z=='3'):
    sys_type='feed'


shortName=input("Enter instance short name(EX: cms01,web06,feed01): ")
keyInstance=client+"-"+environment+"-"+shortName+"-us-east-1"
#print(keyInstance)
hosts=[]
response=ec2.describe_instances(Filters=[{'Name':'tag:client','Values':[client]},{'Name':'tag:env','Values':[environment]},{'Name':'tag:system_type','Values':[sys_type]},{"Name":'tag:Name','Values':[keyInstance]}])

print("Info: %s --> %s"%(keyInstance,response['Reservations'][0]["Instances"][0]["PrivateIpAddress"]))
hosts.append(response['Reservations'][0]["Instances"][0]["PrivateIpAddress"])
print("Env hosts is: ",hosts)



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