#!/usr/bin python3

from scapy.all import *

def icmp():
    dst_ip = "10.0.2.2"    # your gateway
    pkt = IP(dst=dst_ip)/ICMP()/"hello world"
    send(pkt)

# chmod +x icmp.py
# ./icmp.py

# footprinting

# netdiscover -i eth0 -r 10.0.2.0/24



#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
	arp_request = scapy.ARP(pdst = ip)
	# print(arp_request.show())
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_req_broad = broadcast/arp_request
	print(arp_req_broad.summary())
	print(arp_req_broad.show())


def scan2(ip):
	arp_request = scapy.ARP(pdst = ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_req_broad = broadcast/arp_request
	# scapy.srp(arp_req_broad)
	ans_list = scapy.srp(arp_req_broad, timeout = 1)[0]  #removed , unans_list
	# print(ans_list.summary())
	# print(unans_list.summary())
	
	for element in ans_list:
		print(element)
		
def scan3(ip):
	arp_request = scapy.ARP(pdst = ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_req_broad = broadcast/arp_request
	ans_list = scapy.srp(arp_req_broad, timeout=1, verbose=False)[0]  
	
	print('IP\t\t\tMAC Address')
	for element in ans_list:
		print(element[1].psrc + '\t\t' + element[1].hwsrc)
		print("-"*50)

scan3("10.0.2.0/24")

#last Output
"""
IP			MAC Address
10.0.2.2		52:54:00:12:35:02
--------------------------------------------------
10.0.2.3		52:54:00:12:35:03
--------------------------------------------------
10.0.2.4		52:54:00:12:35:04
--------------------------------------------------
"""