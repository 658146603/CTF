import time

import requests

if __name__ == '__main__':
    session = requests.session()
    t = session.get(url="http://pangolinlabs.cn:34170/").text
    while True:
        print(t)
        t = t.split("</div>")
        s = ""
        for i in range(0, len(t) - 2):
            s = s + t[i][len(t[i]) - 1]

        i = eval(s)
        time.sleep(1)
        t = session.post(url="http://pangolinlabs.cn:34170/", data={"ans": i}).text
