# Working With modules ( sys, os, subprocess, argparse, etc....)
"""
Write a script that runs a command (like "ls -l", it can be any command you choose).
"""

import subprocess
import optparse
import sys
#import scapy.all as scapy

def my_ls():
	print("Getting listing!")
	subprocess.call(["ls", "-l"])

# my_ls()

"""
Write a script that runs a command and captures the number of bytes in a print statement.
"""

def num_bytes(cmd):
	string = subprocess.check_output(cmd.split())
	print(string)
	bytes = 0
	for item in string:
		bytes += sys.getsizeof(item)
		
	print("The number of bytes in " + cmd + " is " + str(bytes))

# num_bytes('ls')

"""
Write a script that runs a command to display your current directory.
"""

import os
def get_mycwd():
	cwd = os.getcwd()
	print(cwd)

get_mycwd()
"""
write a ping script where we get user input, and then run a ping request to that host.
"""

def my_ping():
	ip = sys.argv[1]    # command line argument 
	print("pinging the target: " + ip)
	icmp = scapy.IP(dst=ip)/scapy.ICMP()
	# IP defines the protocol for IP addresses
	# dst is the destination IP address
	# ICMP defines the protocol for the ports
	resp = scapy.sr1(icmp, timeout=10, verbose=False)
	if resp == None:
	    print("This host is down")
	else:
	    print("This host is up")
	
# my_ping()


from scapy.all import *

from netaddr import IPNetwork

def scan(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether()
	scapy.ls(scapy.ARP())

def hydrick_scan():
	for ip in IPNetwork('10.240.234.0/24'):
		print('\n')
		scan(ip)
		
hydrick_scan()
"""
Create a script that will accept a single integer as a positional argument, and will print a hash symbol that amount of times.
"""

def my_hash():
	num = int(sys.argv[1])    # command line argument 
	if num is int:
		print("hashes needed: " + num)
		for x in range(num):
			print("#", end="")
		print()
	else:
		print("Please enter an int")

# my_hash()








