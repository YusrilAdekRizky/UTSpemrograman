# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 10:55:01 2020

@author: yusril
"""

#import module socket
import socket

#deklarasi socket
s = socket.socket()
#menentukan host
host = socket.gethostname()
#menentukan port
port = 1234
#menghubungkan socket ke alamat server
s.connect((host,port))
print("Connected to the server")
#menerima pesan dari server
msg = s.recv(1024)
msg = msg.decode()
print("Server Message : ", msg)

while 1:
    #menerima pesan dari server
    msg = s.recv(1024)
    msg = msg.decode()
    print("Server : ",msg)
    #menulis pesan ke server
    new_message = input(str("Anda : "))
    new_message = new_message.encode()
    #mengirim pesan ke server
    s.send(new_message)
		
	