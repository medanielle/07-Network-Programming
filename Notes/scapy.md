python3
>>> import scapy
>>> quit()
*** if not there ***
pip3 install scapy



then run scay in cmd prompt
scapy
>>>mypkt = IP()
>>>mypkt.show()
    ###[ IP ]### 
    version= 4
    ihl= None
    tos= 0x0
    len= None
    id= 1
    flags= 
    frag= 0
    ttl= 64
    proto= hopopt
    chksum= None
    src= 127.0.0.1
    dst= 127.0.0.1
    \options\

*** adding destination with auto-add the source ***
*** 10.0.2.2 = gateway => use route -n ***

>>> mypkt.dst = "10.0.2.2"
>>> mypkt.show()
###[ IP ]### 
  version= 4
  ihl= None
  tos= 0x0
  len= None
  id= 1
  flags= 
  frag= 0
  ttl= 64
  proto= hopopt
  chksum= None
  src= 10.0.2.15
  dst= 10.0.2.2
  \options\

*** route -n ***
route -n >>> for routing table (default gateway)
root@osboxes:~# route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.0.2.2        0.0.0.0         UG    100    0        0 eth0
10.0.2.0        0.0.0.0         255.255.255.0   U     100    0        0 eth0

*** start wire shark then run last comman ***

>>> myicmp = ICMP()
>>> myicmp.show()
###[ ICMP ]### 
  type= echo-request
  code= 0
  chksum= None
  id= 0x0
  seq= 0x0

>>> send(mypkt/myicmp/"scapy program")
.
Sent 1 packets.
>>> 

*** go to wireshark and see icmp packet ***


*** for icmp.py ***
# chmod +x icmp.py
# ./icmp.py

# footprinting
"""
netdiscover -i eth0 -r 10.0.2.0/24
"""
# output
"""
 3 Captured ARP Req/Rep packets, from 3 hosts.   Total size: 180               
 _____________________________________________________________________________
   IP            At MAC Address     Count     Len  MAC Vendor / Hostname      
 -----------------------------------------------------------------------------
 10.0.2.2        52:54:00:12:35:02      1      60  Unknown vendor              
 10.0.2.3        52:54:00:12:35:03      1      60  Unknown vendor              
 10.0.2.4        52:54:00:12:35:04      1      60  Unknown vendor   
 """

# netscan
def scan3(ip):
	arp_request = scapy.ARP(pdst = ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_req_broad = broadcast/arp_request
	ans_list = scapy.srp(arp_req_broad, timeout = 1)[0]  
	
	for element in ans_list:
		print(element[1].show())
# output
 ###[ Ethernet ]### 
  dst       = 08:00:27:41:7b:b3
  src       = 52:54:00:12:35:04
  type      = 0x806
###[ ARP ]### 
     hwtype    = 0x1
     ptype     = 0x800
     hwlen     = 6
     plen      = 4
     op        = is-at
     hwsrc     = 52:54:00:12:35:04
     psrc      = 10.0.2.4
     hwdst     = 08:00:27:41:7b:b3
     pdst      = 10.0.2.15
###[ Padding ]### 
        load      = '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

None


# change output/streamline
	print('IP\t\t\tMAC Address')
	for element in ans_list:
		print(element[1].psrc)
		print(element[1].hwsrc)
		print("-"*50)

# output
root@osboxes:~/Desktop# python netscan3.py 
Begin emission:
***Finished sending 256 packets.

Received 3 packets, got 3 answers, remaining 253 packets
IP			MAC Address
10.0.2.2
52:54:00:12:35:02
--------------------------------------------------
10.0.2.3
52:54:00:12:35:03
--------------------------------------------------
10.0.2.4
52:54:00:12:35:04
--------------------------------------------------
