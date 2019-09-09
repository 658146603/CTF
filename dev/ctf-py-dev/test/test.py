import libnum
import base64
import hashlib
import binascii
from urllib import parse
from ctf_crypto import file_read

if __name__ == '__main__':
    # sha256 = hashlib.sha256()
    # sha256.update('155989'.encode())
    # print(sha256.hexdigest())
    # print('BAABAABBAAAAAAAABABBABABBBAABABAABBABBBAABBABAABAA'.lower())
    # print(libnum.n2s(0xe6849fe8a789e58da1e58da1e79a840a))
    # print(base64.b64decode('MFEwTzBNMEswSTAJBgUrDgMCGgUABBReAhtobFzTvhaRmVeJ38QUchY9AwQUu69+Aj36pvE8hI6t7jiY7NkyMtQCEAui0B3Ly3d26KxlCXrBJUE='))
    # print(file_read.b2h('../temp/crc32_test.png'))

    # d = 'yo=%40eval%01%28base64_decode%28%24_POST%5Bz0%5D%29%29%3B&z0=QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO2VjaG8oIi0%2BfCIpOzskcD1iYXNlNjRfZGVjb2RlKCRfUE9TVFsiejEiXSk7JHM9YmFzZTY0X2RlY29kZSgkX1BPU1RbInoyIl0pOyRkPWRpcm5hbWUoJF9TRVJWRVJbIlNDUklQVF9GSUxFTkFNRSJdKTskYz1zdWJzdHIoJGQsMCwxKT09Ii8iPyItYyBcInskc31cIiI6Ii9jIFwieyRzfVwiIjskcj0ieyRwfSB7JGN9IjtAc3lzdGVtKCRyLiIgMj4mMSIsJHJldCk7cHJpbnQgKCRyZXQhPTApPyIKcmV0PXskcmV0fQoiOiIiOztlY2hvKCJ8PC0iKTtkaWUoKTs%3D&z1=Y21k&z2=Y2QgL2QgImM6XGluZXRwdWJcd3d3cm9vdFwiJndob2FtaSZlY2hvIFtTXSZjZCZlY2hvIFtFXQ%3D%3D'
    # b = 'QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO2VjaG8oIi0+fCIpOzskcD1iYXNlNjRfZGVjb2RlKCRfUE9TVFsiejEiXSk7JHM9YmFzZTY0X2RlY29kZSgkX1BPU1RbInoyIl0pOyRkPWRpcm5hbWUoJF9TRVJWRVJbIlNDUklQVF9GSUxFTkFNRSJdKTskYz1zdWJzdHIoJGQsMCwxKT09Ii8iPyItYyBcInskc31cIiI6Ii9jIFwieyRzfVwiIjskcj0ieyRwfSB7JGN9IjtAc3lzdGVtKCRyLiIgMj4mMSIsJHJldCk7cHJpbnQgKCRyZXQhPTApPyIKcmV0PXskcmV0fQoiOiIiOztlY2hvKCJ8PC0iKTtkaWUoKTs=&z1=Y21k&z2=Y2QgL2QgImM6XGluZXRwdWJcd3d3cm9vdFwiJndob2FtaSZlY2hvIFtTXSZjZCZlY2hvIFtFXQ=='
    # print(parse.unquote(d))
    # print(base64.b64decode(b))
    # s = ""

    a = [0x48, 0x5D, 0x8D, 0x24, 0x84, 0x27, 0x99, 0x9F, 0x54, 0x18, 0x1E, 0x69, 0x7E, 0x33, 0x15, 0x72, 0x8D, 0x33,
         0x24, 0x63, 0x21, 0x54, 0x0C, 0x78, 0x78, 0x78, 0x78, 0x78, 0x1B]

    b = []
    c = 'lk2j9Gh}AgfY4ds-a6QW1#k5ER_T[cvLbV7nOm3ZeX{CMt8SZo]U'
    s = ''
    for i in range(len(a)):
        b.append(int(a[i] / 3 - 2))
        for j in range(len(b)):
            s += c[b[j]]

    print(s)
