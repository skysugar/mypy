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
            # self.handle_requst(conn,addr)
            t = threading.Thread(target=self.handle_request, args=(conn, addr))
            t.start()

    def handle_request(self, conn, addr):
        while self.status:
            data = conn.recv(4096)
            if not data: break
            environ = self.make_env(data)
            environ['REMOTE_HOST'] = addr

            def start_response(*l):
                http_header = '{}  {}\r\n'.format(environ['VERSION'], l[0])
                header = l[1]
                for i in header:
                    http_header += '{}:{}\r\n'.format(*i)
                http_header += '\r\n'
                conn.send(http_header.encode('utf-8'))
            reply= self.app(environ, start_response)+ b'\r\n'
            conn.send(reply)
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


def hello(environ, start_response):
    #print(environ)
    start_response("200 OK", [('Content-Type', 'text/html')])
    # time.sleep(2)
    return b'hello cgi'


if __name__ == '__main__':
    server = mycgi(app=hello)
    server.start()
