from fabric.api import run, env
from fabric.tasks import execute
from fabric.colors import green,red,yellow,white,cyan
import boto3
import os
import time
import sys

#env.password= ''
env.hosts=[]
client=''
environment=''
sys_type=''

def set_host():
    
    global client
    global environment
    global sys_type

    ec2=boto3.client('ec2')
    
    while True:
        
        print(white('''Available Clients list

        1.tegna 2.nxs 3.mtss 4.sps 5.gmg 6.cmg 7.fox
        \n '''))
        client=input("\nEnter Client Name: ")
        if client not in ['tegna', 'nxs', 'mtss', 'sps', 'gmg', 'cmg', 'fox']:
            enter=input("Enter wrong client name?, Do you want to continue?:(y/n) ")
            if enter =='y':
                break
            else:
                continue
        break

    while True:
        print(white('''\n Available environments
        1.prod 2.dev 3.uat 4.stage 5.qa 6.adk 7.sandbox
        \n'''))


        environment=input("Enter Enviroment Name: ")
        os.system("clear")
        if environment not in ['prod', 'dev', 'qa', 'stage', 'uat', 'sandbox', 'adk']:
            enter=input("Wrong environment name?, Do you want to continue?(y/n): ")
            if enter=='y':
                break
            else:
                continue
        break


    env.hosts=[]
    try:

        print("\nAvailable hosts: \n")
        servers_list=[]
        fulldata=ec2.describe_instances(Filters=[{'Name':'tag:client','Values':[client]},{'Name':'tag:env','Values':[environment]},{"Name":"instance-state-name",'Values':['pending','running']}])
        for i in range(len(fulldata['Reservations'])):
            for j in range(len(fulldata['Reservations'][i]['Instances'])):
                servers_list+=[y["Value"] for y in [x for x in fulldata['Reservations'][i]["Instances"][j]['Tags']] if y["Key"]=="Name"]
                #print(fulldata['Reservations'][0]["Instances"][0]['ImageId'])
        if len(servers_list)==0:
            print(yellow("No instances available\n"))
            sys.exit(0)
        else:
            for i in range(len(servers_list)):
                print(white(servers_list[i]))
            
            
            shortName=input("\nEnter instance short names(EX: cms01,web06,feed01): ").split()
            for i in shortName:
                keyInstance=client+"-"+environment+"-"+i+"-us-east-1"
                print(keyInstance)
                response=ec2.describe_instances(Filters=[{'Name':'tag:client','Values':[client]},{'Name':'tag:env','Values':[environment]},{"Name":'tag:Name','Values':[keyInstance]}])
                print(green("Info: %s --> %s"%(keyInstance,response['Reservations'][0]["Instances"][0]["PrivateIpAddress"])))
                env.hosts.append(response['Reservations'][0]["Instances"][0]["PrivateIpAddress"])
                print(response['Reservations'][0]["Instances"][0]['ImageId'])
            print(env.hosts)

                

    except:
        print(yellow('''\n
        Can not connect to the server, reasons can be
        1. Selected instance might have connectivity problems(network issue, Terminated etc
        2. Choosen wrong short name
        3. Pressed ctrl+c
         
        Please try after sometime \n'''))

    

def hostname():
    if(len(env.hosts)==0):
        sys.exit(0)
    run("hostname")


def service_status():
    hostname()
    if(len(env.hosts)==0):
        sys.exit(0)    
    try:
        run("sudo service liferay status")
        
        
    except:
        run("sudo service jboss-feeds status && sleep 1")
            
        
def service_stop():
    
    
    hostname()
    try:
        run("sudo service liferay stop")
        ask=input("Do you what to start the service(y/n): ")
        if ask=='y':
            run("sudo service liferay start && sleep 1")

    except:
        run("sudo service jboss-feeds stop && sleep 1")
        ask=input("Do you what to start the service(y/n): ")
        if ask=='y':
            run("sudo service jboss-feeds start && sleep 1")
            

            

def service_start():
    
    hostname()
    try:
        run("sudo service liferay start && sleep 1")

    except:
        run("sudo service jboss-feeds start && sleep 1")
