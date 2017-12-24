import socket,hashlib,os

client = socket.socket()
client.connect(("localhost",8888))
while True:
    str = input("send masages").strip()
    client.send(str.encode("utf-8"))
    if(len(str)==0):
        continue
    res_len = client.recv(1024).decode()
    client.send(b"ack")
    m = hashlib.md5()
    print(os.path.basename(str.split()[1]))
    f = open(os.path.basename(str.split()[1]),"wb")
    print("recevied data len(%s)" % int(res_len))
    if int(res_len)==0:
        continue
    res_data = 0
    data = b''
    size = 1024
    while True:
        if int(res_len)-res_data < 1024:#最后一次接受可以能会多出来，所以要控制
            size = int(res_len)-res_data
        msg = client.recv(size)
        m.update(msg)
        f.write(msg)
        data += msg
        res_data += int(len(msg))
        if(res_data>=int(res_len)):
            break
    client.send(b"ack")
    md5 = client.recv(1024)
    f.close()
    print(len(data))
    print(md5.decode())
    print(m.hexdigest())
client.close()
