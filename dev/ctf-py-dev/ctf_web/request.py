import urllib.parse
import urllib.request


def request(url, values=None):
    if values is not None:
        data = urllib.parse.urlencode(values)
        data = data.encode('ascii')
    else:
        data = None
    req = urllib.request.Request(url, data)
    # req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with urllib.request.urlopen(req) as response:
        return response.read()


if __name__ == '__main__':
    print(request('http://www.baidu.com/'))
