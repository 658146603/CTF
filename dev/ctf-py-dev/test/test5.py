import urllib.request

if __name__ == '__main__':
    req = urllib.request.Request('http://das.wetolink.com:8941/6GTest.file')
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    req.add_header('Content-Range', 'bytes=6291455850-6291456050')
    with urllib.request.urlopen(req) as response:
        while True:
            a = response.read(1000)
            print(a)
