import urllib.parse
import urllib.request


def request(url, values=None):
    if values is not None:
        data = urllib.parse.urlencode(values)
        data = data.encode('ascii')
    else:
        data = None
    req = urllib.request.Request(url, data)
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    with urllib.request.urlopen(req) as response:
        return response.read()


def request_all(url, values=None):
    if values is not None:
        data = urllib.parse.urlencode(values)
        data = data.encode('ascii')
    else:
        data = None
    req = urllib.request.Request(url, data)
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    req.add_header('X-Requested-With', 'XMLHttpRequest')
    with urllib.request.urlopen(req) as response:
        return response.headers['Set-Cookie']


def request_temp(url, values=None):
    if values is not None:
        data = urllib.parse.urlencode(values)
        data = data.encode('ascii')
    else:
        data = None
    req = urllib.request.Request(url, data)
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    req.add_header('X-Requested-With', 'XMLHttpRequest')
    req.add_header('Cookie', session)
    with urllib.request.urlopen(req) as response:
        return response.read()


if __name__ == '__main__':
    # print(request('http://www.baidu.com/'))
    session = request_all('http://sec.hdu.edu.cn:7100/game/push', {'token': '666666666tokennn'})
    print(session)
    flag = request_temp('http://sec.hdu.edu.cn:7100/game/push', {'token': '666666666tokennn'})
    print(flag)
