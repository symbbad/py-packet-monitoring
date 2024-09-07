import psutil

nic = psutil.net_if_addrs()
for interface, address in nic.items():
    print(f"{interface}")
    for addr in address:
        print(f"  {addr.family.name} {addr.address}")