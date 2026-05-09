servers = ["nginx-server", "mysql-server","ramu"]

for server in servers:
    if "nginx" in server and "-" in server and "server" in server:
        print(server)
#     if "nginx" in server or "-" in server or "server" in server:
#print(server)
