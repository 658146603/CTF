import uu

if __name__ == '__main__':
    with open('h', 'rb') as i:
        with open('h.uud', 'wb') as o:
            uu.encode(i, o)
    with open('h.uud', 'rb') as i:
        with open('h.txt', 'wb') as o:
            uu.decode(i, o)
