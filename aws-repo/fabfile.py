from fabric.api import run, env
from fabric.tasks import execute
from fabric.colors import green,red,yellow,white,cyan
import boto3
import os
import time
import sys
'''

'''
env.hosts=[]
client=''
environment=''
sys_type=''
# servers_list=[]
def set_host():
    
    global client
    global environment
    global sys_type

    ec2=boto3.client('ec2')
    
    while True:
        
        print(white('''Choose client from the list

        1.tegna
        2.nxs
        3.mtss
        4.sps
        5.gmg
        6.cmg
        7.fox
        \n '''))
        x=input("\nEnter client number: ")

        os.system("clear")
        if(x=='1'):
            client='tegna'
            break
        elif(x=='2'):
            client='nxs'
            break
        elif(x=='3'):
            client='mtss'
            break
        elif(x=='4'):
            client='sps'
            break
        elif(x=='5'):
            client='gmg'
            break
        elif(x=='6'):
            client='cmg'
            break
        elif(x=='7'):
            client='fox'
            break
        else:
            print(yellow("\nNot a valid client number, choose again!\n"))
            time.sleep(2)

    #print("client is ",client)
    while True:
        print(white('''\nChoose environment
        1.prod
        2.dev
        3.uat
        4.stage
        5.qa
        6.adk
        \n'''))

        y=input("Enter enviroment number: ")
        os.system("clear")
        if(y=='1'):
            environment='prod'
            break
        elif(y=='2'):
            environment='dev'
            break
        elif(y=='3'):
            environment='uat'
            break
        elif(y=='4'):
            environment='stage'
            break
        elif(y=='5'):
            environment='qa'
            break
        elif(y=='6'):
            environment='adk'
            break

        else:
            print(yellow("\nNot a valid environment number, choose again! \n"))
            time.sleep(2)


    while True:
        print(white('''\nchoose system type
        1.cms
        2.web
        3.feed
        \n'''))
        z=input("Enter system type number: ")
        os.system("clear")
        if(z=='1'):
            sys_type='cms'
            break
        elif(z=='2'):
            sys_type='web'
            break
        elif(z=='3'):
            sys_type='feed'
            break
        else:
            print(yellow("\nNot a valid system_type number, choose again!"))
            time.sleep(2)


    #shortName=input("Enter instance short name(EX: cms01,web06,feed01): ")
    #keyInstance=client+"-"+environment+"-"+shortName+"-us-east-1"
    #print(keyInstance)
    env.hosts=[]
    try:
        #begin
        print("\nAvailable hosts: \n")
        servers_list=[]
        fulldata=ec2.describe_instances(Filters=[{'Name':'tag:client','Values':[client]},{'Name':'tag:env','Values':[environment]},{'Name':'tag:system_type','Values':[sys_type]}])
        for i in range(len(fulldata['Reservations'])):
            servers_list+=[y["Value"] for y in [x for x in fulldata['Reservations'][i]["Instances"][0]['Tags']] if y["Key"]=="Name"]
        if len(servers_list)==0:
            print(yellow("No instances available\n"))
            sys.exit(0)
        else:
            for i in range(len(servers_list)):
                print(white(servers_list[i]))
            
            shortName=input("\nEnter instance short name(EX: cms01,web06,feed01): ")
            keyInstance=client+"-"+environment+"-"+shortName+"-us-east-1"
        
        #end

            response=ec2.describe_instances(Filters=[{'Name':'tag:client','Values':[client]},{'Name':'tag:env','Values':[environment]},{'Name':'tag:system_type','Values':[sys_type]},{"Name":'tag:Name','Values':[keyInstance]}])
        
            print(green("Info: %s --> %s"%(keyInstance,response['Reservations'][0]["Instances"][0]["PrivateIpAddress"])))
            env.hosts.append(response['Reservations'][0]["Instances"][0]["PrivateIpAddress"])
            #print("Env hosts is: ",env.hosts)
    except:
        print(yellow('''\n
        Can not connect to the server, reasons can be
        1. Selected instance might have connectivity problems(network issue, Terminated etc
        2. Choosen wrong short name
        3. Pressed ctrl+c
         
        Please try after sometime \n'''))

    

def uname():
    run("uname -s")

def hostname():
    if(len(env.hosts)==0):
        sys.exit(0)
    run("hostname")

def service_status():
    global sys_type
    hostname()
    if(len(env.hosts)==0):
        sys.exit(0)    
    if not sys_type=='feed':
        time.sleep(2)
        #confirm=input("Is hostname correct(y/n)?: ")
        confirm='y'
        if confirm=='y':
            run("service liferay status")
        else:
            time.sleep(1)
            print(red("Aborted..."))
    else:
        confirm=input("Is hostname correct(y/n)?: ")
        if confirm=='y':
            run("sudo service jboss-feeds status && sleep 1")
            
        else:
            time.sleep(1)
            print(red("Aborted..."))

def service_stop():
    
    global sys_type
    hostname()
    
    if not sys_type=='feed':
        run("sudo service liferay stop && sleep 1")
        ask=yellow(input("Do you what to start the service(y/n): "))
        if ask=='y':
            run("sudo service liferay start && sleep 1")
            
    else:
        run("sudo service jboss-feeds stop && sleep 1")
        ask=yellow(input("Do you what to start the service(y/n): "))
        if ask=='y':
            run("sudo service jboss-feeds start && sleep 1")
            

def service_start():
    
    hostname()
    global sys_type
    
    if not sys_type=='feed':
        time.sleep(2)
        #confirm=input("Is hostname correct(y/n)?: ")
        confirm='y'
        if confirm=='y':
            run("sudo service liferay start")
        else:
            time.sleep(1)
            print(red("Aborted..."))
    else:
        confirm=input("Is hostname correct(y/n)?: ")
        if confirm=='y':
            run("sudo service jboss-feeds start && sleep 1")
            
        else:
            time.sleep(1)
            print(red("Aborted..."))
