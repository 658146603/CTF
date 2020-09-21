from ctf_crypto import hash

h = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

if __name__ == '__main__':
    s = ''
    for i in range(16):
        for j in range(16):
            for k in range(16):
                s = "{0}{1}{2}{3}{4}{5}{6}".format('c3b', h[i], '0f1a', h[j], '123ab23', h[k], 'c7cb21909f61778')
                print(s)
                ha = hash.md5(s)
                if ha.startswith('cf3') and ha.endswith('08bc'):
                    print(hash.md5(s))
                    exit(0)
