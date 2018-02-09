import fabric
from fabric.api import run

def print_hello():
    print("Hello Krishna, welcome to fabfile")

def hostN():
    run('/homedirs/cyb.hbhatnagar/admin-tools/jgroups-probe/jgroup-probe.rb mtss-prod-cms04-us-east-1.lakana-prod.com')

def feeds():
    run("systemctl ")
