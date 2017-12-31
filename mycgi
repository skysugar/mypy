import socket
import threading
import time

class mycgi:
    def __init__(self, host='', port=10000, app=None):
        if app == None:
            assert 'Must be set app'
        self.app = app
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, port))
        self.sock = sock
        self.status = True

    def start(self):
        self.sock.listen()
        while self.status:
            conn, addr = self.sock.accept()
            print('new access {}:{}'.format(*addr))
            #self.handle_requst(conn,addr)
            t = threading.Thread(target=self.handle_requst, args=(conn, addr))
            t.start()

    def start_respone(self, *l):
        code = '{}  {}\r\n'.format(self.environ['VERSION'], l[0])
        header = l[1]
        self.conn.send(code.encode('utf-8'))
        for i in header:
            self.conn.send('{}:{}\r\n\r\n'.format(*i).encode('utf-8'))

    def handle_requst(self, conn, addr):
        self.conn = conn
        while self.status:
            data = conn.recv(1024)
            if not data:
                break
            self.environ = environ = self.make_env(data)
            environ['REMOTE_HOST'] = addr
            reply = self.app(self.environ, self.start_respone)
            conn.send(reply)
            conn.send(b'\r\n')
            conn.close()
            break

    def make_env(self, r):
        e = r.decode('utf-8')
        environ = dict()
        v, *h, p = e.split('\r\n')
        environ['MOTHED'], environ['PATH_INFO'], environ['VERSION'] = v.split()
        if '?' in environ['PATH_INFO']:
            temp = environ['PATH_INFO']
            environ['PATH_INFO'], environ['Query_String'] = temp.split('?')
        for i in h:
            if ':' not in i:
                continue
            k, v = i.split(': ')
            environ[k] = v
        if environ['MOTHED'] == "POST":
            environ['data'] = p
        return environ

    def stop(self):
        self.status = False
        self.sock.close()


def hello(environ, start_respone):
    print(environ)
    start_respone("200 OK", [('Content-Type', 'text/html')])
    #time.sleep(2)
    return b'hello cgi'


if __name__ == '__main__':
    server = mycgi(app=hello)
    server.start()
