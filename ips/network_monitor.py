import scapy.all as scapy

def capture_traffic(callback):
    scapy.sniff(prn=callback, filter="ip", store=0)
