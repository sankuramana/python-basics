servers = ["prod-app", "test-app", "prod-db", "dev-server"]

for server in servers:
    if "prod" in server:
        print(server)