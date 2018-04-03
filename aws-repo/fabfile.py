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
    print("Choose client from the list")
    print('''
    1.tegna
    2.nxs
    3.mtss
    4.sps
    5.gmg
    6.cmg
    7.fox
    \n ''')
    

    x=input("Enter client number: ")
    client
    print('''\nChoose environment
    1.prod
    2.dev
    3.uat
    4.stage
    5.qa
    \n''')
    y=input("Enter enviroment number: ")
    environment
    print('''\nchoose system type
    1.cms
    2.web
    3.feed
    \n''')
    z=input("Enter system type number: ")
    system_type
    rep=ec2.describe_instances(Filters=[{'Name':'tag:client','Values':[client]},{'Name':'tag:env','Values':[environment]},{'Name':'tag:system_type','Values':[system_type]}])
    print(rep)
    env.hosts=['172.31.12.150']
    
def uname():
    run("uname -s")
def hostname():
    run("hostname")
def service_status():
    run("service liferay status")


