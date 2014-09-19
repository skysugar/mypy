import urllib.request
import re
from bs4 import BeautifulSoup

r_id = re.compile('[0-9]+')
r_picre = re.compile('[0-9]+\.00')
r_name = re.compile('name: \'(.+)\'')



def make_headers(urlheader):
    s_headers = {
#    "Accept":"application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*",
#    "Accept-Encoding":"gzip, deflate",
#    "Accept-Language":"zh-CN",
#    "Connection":"Keep-Alive",
#    "Cookie":"mt_ext=%7b%22adu%22%3a%222a80912176a73e1092d1921dc37c563a%22%7d; aview=655.1057746|655.1023428|1648.130979; atw=655.1057746.11|1648.130979.1; __jda=122270672.2019175435.1408530739.1409131637.1409135688.4; __jdv=122270672|direct|-|none|-; __jdu=2019175435; ipLocation=%u5317%u4EAC; areaId=1; ipLoc-djd=1-72-2799-0",
#    "If-Modified-Since":"Wed, 27 Aug 2014 03:35:15 GMT",
    "User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3)",
    }
    for k in s_headers.keys():
        urlheader.add_header(k,s_headers[k])
    return(urlheader)

def get_data(openurl):
    req = urllib.request.Request(openurl)
    req = make_headers(req)
    return(urllib.request.urlopen(req).read())

class jdproductinfo:
    def __init__(self,url=None):
        self.url = url
        self.id = r_id.findall(url)[0]
        self.pr_url = "http://p.3.cn/prices/get?skuid=J_"+self.id
        self.ur_url = "http://club.jd.com/review/"+self.id+"-0-1-0.html"

    def getname(self):
        data = get_data(self.url)
#        p_name = r_name.findall(data.decode('gb2312'))[0]
        soup = BeautifulSoup(data.decode('gb2312','ignore'))
        p_name = soup.find('div',id='name').h1.get_text()
        return(p_name)

    def getprices(self,n='now'):
        data = get_data(self.pr_url)
        n_p,o_p = r_picre.findall(data.decode('utf8'))
        if n == 'now':
            return(n_p)
        elif n == 'old':
            return(o_p)
        else:
            return(None)
