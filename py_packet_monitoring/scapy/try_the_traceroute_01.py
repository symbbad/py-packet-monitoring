from scapy.all import traceroute

target = "www.google.com"
result, _ = traceroute(target)