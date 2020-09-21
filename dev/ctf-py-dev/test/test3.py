import zlib


def crc32(s):
    return zlib.crc32(s.encode('utf8'))


if __name__ == '__main__':
    for y in range(3000+1):
        for M in range(12+1):
            for d in range(31+1):
                s = '{0}{1}{2}'.format('%04d' % y, '%02d' % M, '%02d' % d)
                c = crc32(s)
                if c == 0x367BFAFC:
                    print(s)
                    print(crc32(s))
                    exit(0)
