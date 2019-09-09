import binascii
import collections


def b2h(path):
    with open(path, 'rb') as data:
        return binascii.b2a_hex(data.read())


def alphabet_counter(path):
    with open(path, 'r') as data:
        return collections.Counter(data.read())


if __name__ == "__main__":
    print(b2h('../temp/crc32_test.png'))
    print(alphabet_counter('../temp/pub.key'))
