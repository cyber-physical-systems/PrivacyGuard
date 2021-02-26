from scapy.all import *
import os


def filtertcp(path):
    os.chdir(path)
    pcap = rdpcap('1.pcap')
    filtered = (pkt for pkt in pcap if 'TCP' in pkt)       # Filter out TCP packets.
    wrpcap('tcp.pcap', filtered)


read_path = 'C:/penv/PGOnline/1sthour'
filtertcp(read_path)
