import sys
import time
from os import popen
from random import randrange, randint
import time
#remove annoying ipv6 error
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import sendp, IP,UDP, Ether, TCP

def sourceIPgen():

  first = 140
  second = 28
  third = 0

  ip = ".".join([str(first),str(second),str(third),str(randrange(1,12))])
  print ip
  return ip

def main():
  for i in range (1,5):
    mymain()
    time.sleep (10)

def mymain():

  dstIP = sys.argv[1:]
  print dstIP
  #src_port = 80
  #dst_port = 1

  interface = popen('ifconfig | awk \'/eth0/ {print $1}\'').read()

  for i in xrange(0,500):
    packets = Ether()/IP(dst=dstIP,src=sourceIPgen())/TCP(dport=randint(1,1024),sport=randint(1,1024))
    print(repr(packets))
    sendp( packets,iface=interface.rstrip(),inter=0.025)

if __name__=="__main__":
  main()
