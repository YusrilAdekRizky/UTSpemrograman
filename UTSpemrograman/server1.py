# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 10:55:22 2020

@author: yusril
"""
#import module socket
import socket

#deklarasi socket
s = socket.socket()
#menentukan alamat server
host = socket.gethostname()
#menentukan port server
port = 1234
#bind kealamat server
s.bind((host,port))
#mendengarkan koneksi dari client
s.listen(5)
print("menunggu koneksi dari client...")
#menerima koneksi dari client
conn,addr = s.accept()
print("Client telah terkoneksi..")
#mengirim pesan balasan ke client bahwa sudah tersambung ke server
conn.send("Welcome to the Server...".encode())

while 1:
    #memasukkan pesan
    msg = input(str("Anda : "))
    #mengubah string menjadi bytes
    msg = msg.encode()
    #mengirim pesan
    conn.send(msg)
    print("Pesan Terkirim ...")
    #menerima pesan dari client
    recv_msg = conn.recv(1024)
    print("client :", recv_msg.decode())
    	
