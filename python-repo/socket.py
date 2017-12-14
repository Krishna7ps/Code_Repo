import socket


mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(("52.11.233.90",80))
cmd='GET http://52.11.233.90/test.txt HTTP/1.0 \n'.encode()
mysock.send(cmd)

while True:
	data=mysock.recv(512)
	if(len(data)>1):
		break
	print(data.decode())
mysock.close()

