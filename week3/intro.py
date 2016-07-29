import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect( ('www.py4inf.com', 80) )
