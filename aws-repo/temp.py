 1.tegna
    2.nxs
    3.mtss
    4.sps
    5.gmg
    6.cmg
    7.fox
1.prod
    2.dev
    3.uat
    4.stage
    5.qa

if(x==1):
    environment='prod'
if(x==2):
    environment='dev'
if(x==3):
    environment='uat'
if(x==4):
    environment='stage'
if(x==5):
    environment='qa'
if(x==6):
    client='cmg'
if(x==7):
    client='fox'
if(x==1):
    client=''

    
    
 #print(response)

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
