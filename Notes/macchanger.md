in kali
create file called mac1.py
open cmd prompt
ifconfig/ ip addr
    - ether: mac add
    - inet: IPv4 address
ifconfig eth0 down
ifconfig eth0 hw ether 00:11:22:33:44:55 *** changes MAC addr ***
ifconfig eth0 up


*** if no ip on eth0 ***
dhclient eth0
smdb  service restart
dhclient eth0


*** Scrip mac1.py ***

#! /usr/bin/env python

import subprocess

subprocess.call("ifconfig", shell=True)


*** Script mac2.py ***

#! /usr/bin/env python

import subprocess

subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 00:22:22:33:44:55", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)


*** Script mac4.py ***

#! /usr/bin/env python

import subprocess

interface = input('interface: ')
new_mac = input('new_mac: ')

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

*** Script mac6.py ***

#! /usr/bin/env python3

import subprocess

interface = input('interface: ')
new_mac = input('new_mac: ')

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether" + new_mac])
subprocess.call(["ifconfig", interface, "up"])


*** Script mac6.py ***

#! /usr/bin/env python3

import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest='interface', help="Interface to change mac address")
parser.add_option("-m", "--mac", dest='new_mac', help="add new mac address")


(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether" + new_mac])
subprocess.call(["ifconfig", interface, "up"])

*** pythex.org ***


*** Script mac11.py ***

#! /usr/bin/env python3

import subprocess
import optparse
import re

def getarguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest='interface', help="Interface to change mac address")
    parser.add_option("-m", "--mac", dest='new_mac', help="add new mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        # code to handle error
        parser.error("please specify an interface, use --help for more details)
    elif not options.new_mac:
        # code to handle error
        parser.error("please specify an new mac, use --help for more details)
    return options

def change_mac(interface, new_mac):
    #print
    
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether" + new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig"], interface)
    mac_add_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w')
    if mac_add_search_result:
        print(mac_add_search_result.group(0))
    else:
        print("Couldn't read mac add")

        

options = get_arguments()
change_mac(options.interface, options.new_mac)
