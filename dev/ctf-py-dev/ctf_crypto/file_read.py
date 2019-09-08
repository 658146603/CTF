import binascii


def b2h(path):
    with open(path, 'rb') as data:
        return binascii.b2a_hex(data.read())


if __name__ == "__main__":
    pass
