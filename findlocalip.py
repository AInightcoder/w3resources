import socket

hostname=socket.gethostname()
IP=socket.gethostbyname(hostname)
print(f'{IP} that is your ip address')