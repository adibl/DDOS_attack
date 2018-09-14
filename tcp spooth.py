from scapy.all import *
pkt = Ether()/IP(src="10.0.0.2", dst='10.0.0.1', ttl=24) / TCP(dport=80)
pkt.show()
reply = srp1(pkt, verbose=0)
reply.show()