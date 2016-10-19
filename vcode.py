import pytesseract
import urllib.request
from PIL import Image
from io import BytesIO

'''
依赖关联：
先安装 tesseract
然后安装python需要的相关模块

Archlinux :
  pacman -S tesseract tesseract-data-chi_sim  tesseract-data-eng

Python pip:
  pip install pillow pytesseract
'''

def parse(img):

    if img.startswith('http'):
        req = urllib.request.urlopen(img)
        data = req.read()
        im = BytesIO()
        im.write(data)
        image = Image.open(im)
        vcode = pytesseract.image_to_string(image)
        return vcode
    else:
        im = Image.open(img)
        vcode = pytesseract.image_to_string(im)
        return vcode
