from fabric.api import run, env
from fabric.tasks import execute
import boto3
import os
import time

env.hosts=[]
client=''
environment=''
sys_type=''

def set_host():
    
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
    

def uname():
    run("uname -s")
def hostname():
    run("hostname")
def service_status():
    global sys_type
    hostname()
    
    if not sys_type=='feed':
        time.sleep(2)
        confirm=input("Is hostname correct(y/n)?: ")
        if confirm=='y':
            run("service liferay status")
        else:
            time.sleep(1)
            print("Aborted...")
    else:
        confirm=input("Is hostname correct(y/n)?: ")
        if confirm=='y':
            run("sudo service jboss-feeds status && sleep 1")
            
        else:
            time.sleep(1)
            print("Aborted...")

def service_stop():

    global sys_type
    hostname()
    
    if not sys_type=='feed':
        time.sleep(2)
        confirm=input("Is hostname correct(y/n)?: ")
        if confirm=='y':
            run("sudo service liferay stop")
        else:
            time.sleep(1)
            print("Aborted...")
    else:
        confirm=input("Is hostname correct(y/n)?: ")
        if confirm=='y':
            run("sudo service jboss-feeds stop && sleep 1")
        else:
            time.sleep(1)
            print("Aborted...")
def service_start():
    
    hostname()
    global sys_type
    
    if not sys_type=='feed':
        time.sleep(2)
        confirm=input("Is hostname correct(y/n)?: ")
        if confirm=='y':
            run("sudo service liferay start")
        else:
            time.sleep(1)
            print("Aborted...")
    else:
        confirm=input("Is hostname correct(y/n)?: ")
        if confirm=='y':
            run("sudo service jboss-feeds start && sleep 1")
            
        else:
            time.sleep(1)
            print("Aborted...")
