import pandas as pd
import csv
from scapy.all import *
import os


def size(path):
    os.chdir(path)
    pcap = rdpcap('tcp.pcap')
    headers = ['time', 'size']
    with open('tcp.csv', 'w', newline='') as f:
        fcsv = csv.writer(f)
        fcsv.writerow(headers)
    for i in range(0, len(pcap)):
        pcap0 = pcap[i]
        print(pcap0.time)
        print(len(pcap0))
        a1 = pcap0.time
        a2 = len(pcap0)
        rows = [a1, a2]
        with open('tcp.csv', 'a', newline='') as f:
            fcsv = csv.writer(f)
            fcsv.writerow(rows)


def resample(path):
    os.chdir(path)
    df = pd.read_csv('tcp.csv')
    d_col = ['Time', 'Size']
    df.columns = d_col
    df.index = pd.to_datetime(df['Time'], unit='s')
    df = df.resample('S').sum()
    df = df.drop('Time', axis=1)
    print(df)
    # df.to_csv('resampled.csv', header=False)


read_path = 'C:/penv/PGOnline/1sthour'
size(read_path)
resample(read_path)
