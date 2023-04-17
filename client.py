import socket
target_host = "192.168.122.255"
target_port = 9997


# Create a client

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Start a connection
client.connect((target_host, target_port))
# send some data

client.send(b"HiThere")

# recieve some data

data, addr = client.recvfrom(4096)

print(data.decode())
client.close()
