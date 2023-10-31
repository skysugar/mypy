import socket


def consumer():
  while True:
    conn, addr = yield
    data = conn.recv(1024)
    print(data)
    conn.send(bytes(f'HTTP/1.1 200\r\n\r\nhello {addr[0]}', "utf-8"))
    conn.close()

sock  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 12345

sock.bind((host, port))
sock.listen(5)

cs = consumer()
cs.send(None)

while True:
  conn, addr =  sock.accept()
  print(f"{addr} connected.")
  cs.send((conn, addr))


sock.close()


#协程测试学习
#
#curl -i 127.0.0.1:12345
#ab -c 5 -n 5000  http://127.0.0.1:12345/
#
# yield的用法
# send(None) 启动一个生成器(generator)
# 在接受参数时 value = yield， 接受数据,函数名调用 send() 方法发送。
# 在返回数据时 yield value,  返回数据,vaule = 方法名()。
