import re
import requests

url = 'http://cn-proxy.com/'
header = {'Host': 'cn-proxy.com',
          'Referer': 'https://www.google.com/',
          'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

research = re.compile(r'<td>(?P<ip>.*)</td>\n<td>(?P<port>.*)</td>\n<td>(?P<iplocal>.*)</td>')


def runtime(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        run = func(*args, **kwargs)
        end = time.time()
        timeuse = end - start
        return run,timeuse
    return wrapper


def getip():

    r = requests.get(url,headers = header)
    a = research.findall(r.text)
    buf = []
    for i in a[1:]:
        buf.append(i)
    return buf


@runtime
def checkip(ip, port):

    proxies = {
        "http": "http://{}:{}".format(ip, port),
        "https": "http://{}:{}".format(ip, port)
    }
    try:
        print("开始验证 {}:{}".format(ip, port))
        r = requests.get('http://ip.cn', proxies=proxies, timeout=30)
        check = re.findall(r'<code>(.*?)</code>', r.text)
        if check:
            return 1
    except:
        return 0


def cleanresult():
    
    with open('./result.txt', 'w') as f:
        pass


def save(ip, port, iplocal, timeuse):

    with open('./result.txt', 'a+') as f:
        f.write("{}:{} {} {}\n".format(ip, port, iplocal, timeuse))


if __name__ == "__main__":
    cleanresult()
    proxyips = getip()
    for i in proxyips:
        ip, port, iplocal = i
        checkresult, timeuse = checkip(ip, port)
        if checkresult:
            print("可用代理: {}:{} {} 用时:{}".format(ip, port, iplocal, timeuse))
            save(ip, port, iplocal, timeuse)
