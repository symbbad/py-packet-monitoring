import psutil

connections = psutil.net_connections(kine='inet')
for conn in connections:
    print(f"프로세스 {conn.pid} {conn.status} {conn.laddr.ip} {conn.laddr.port} {conn.raddr.ip} {conn.raddr.port}")