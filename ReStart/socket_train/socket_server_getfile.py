import os,socket,hashlib

serv = socket.socket()
serv.bind(("localhost",8888))
serv.listen(5)
while True:
    try:
        conn,addr = serv.accept()
        while True:
            data = conn.recv(1024)
            if not data:
                break
            else:
                cmd,filename = data.decode().split()
                if os.path.isfile(filename):
                        conn.send(str(os.stat(filename).st_size).encode("UTF-8"))
                        client_ack = conn.recv(1024)
                        m = hashlib.md5()
                        print(filename)
                        f = open(filename,"rb")
                        for i in f :
                                conn.send(i)
                                m.update(i)
                        conn.recv(1024)
                        conn.send(m.hexdigest().encode("utf-8"))
                        f.close()
    except ConnectionResetError as e:
        print(e)
serv.close()