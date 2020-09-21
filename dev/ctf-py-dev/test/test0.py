import hashlib

if __name__ == '__main__':
    key = '#2U)W'
    pwd = 'ueint'
    result = []
    # pwd为密文
    for j in range(len(key)):
        result.append(chr(ord(pwd[j]) ^ ord(key[j])))  # 跟KEY异或回去就是原明文
    result = ''.join(result)
    print(result)
    hl = hashlib.md5()
    hl.update(result.encode(encoding='utf-8'))
    print(hl.hexdigest())
