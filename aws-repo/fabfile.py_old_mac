from fabric.api import run, env
from fabric.tasks import execute
import boto3
import os
import time

def uname():
    run("uname -s")
def hostname():
    run("hostname")
def service_status():
    
    
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



