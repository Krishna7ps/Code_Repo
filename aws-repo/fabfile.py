from fabric.api import run, env
import boto3

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
def all():
    
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
    
    print("client is ",client)
 
    print('''\nChoose environment
    1.prod
    2.dev
    3.uat
    4.stage
    5.qa
    \n''')
    y=input("Enter enviroment number: ")
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
    if(z=='1'):
        system_type='cms'
    if(z=='2'):
        system_type='web'
    if(z=='3'):
        system_type='feed'
    
    print("Details for %s - %s - %s "% (client,environment,system_type))

    rep=ec2.describe_instances(Filters=[{'Name':'tag:client','Values':[client]},{'Name':'tag:env','Values':[environment]},{'Name':'tag:system_type','Values':[system_type]}])
#    print(rep)
    env.hosts=['172.31.12.150']
    
def uname():
    run("uname -s")
def hostname():
    run("hostname")
def service_status():
    run("service liferay status")


