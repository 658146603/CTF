import hashlib


def sha256(s):
    sha = hashlib.sha256()
    sha.update(s.encode())
    return sha.hexdigest()


def md5(s):
    md = hashlib.md5()
    md.update(s.encode())
    return md.hexdigest()


def sha1(s):
    md = hashlib.sha1()
    md.update(s.encode())
    return md.hexdigest()


if __name__ == '__main__':
    print(sha256('783'))
    print(sha1('783'))
    print(md5('522018D665387D1DA931812B77763410').upper())
