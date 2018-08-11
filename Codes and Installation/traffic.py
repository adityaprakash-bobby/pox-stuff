import sys
import getopt
import time
from os import popen
from random import randrange, randint
#remove annoying ipv6 error
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import TCP, IP, UDP, Ether

def sourceIPgen():
    
    first = 140
    second = 28
    third = 0

    ip = ".".join([str(first),str(second),str(third),str(randrange(1,140))])
    return ip

def gendest(start, end):

    first = 10
    second =0; third =0;
    ip = ".".join([str(first),str(second),str(third),str(randrange(start,end))])
    return ip

def main(argv): 
    print argv
    try:
        opts, args = getopt.getopt(sys.argv[1:],'s:e:',['start=','end='])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt =='-s':
            start = int(arg)
        elif opt =='-e':
            end = int(arg)
    if start == '':
        sys.exit()
    if end == '':
        sys.exit()

    interface = popen('ifconfig | awk \'/eth0/ {print $1}\'').read()

    for i in xrange(1000):
        packets = Ether()/IP(dst=gendest(start, end),src=sourceIPgen())/UDP(dport=randint(1,1024),sport=randint(1,1024))
        print(repr(packets))
        sendp( packets,iface=interface.rstrip(),inter=0.1)

if __name__ == '__main__':
  main(sys.argv)


