import binascii
import struct
import zxing
from PIL import Image


def png_crc32(path):
    with open(path, 'rb') as misc:
        pic = misc.read()
        for w in range(1024):
            for h in range(1024):
                data = pic[12:16] + struct.pack('>I', w) + struct.pack('>I', h) + pic[24:29]
                crc = pic[29:33]
                if (binascii.crc32(data) & 0xffffffff) == struct.unpack('>I', crc)[0]:
                    return w, h


def bin2qr(data, size, path):
    image = Image.new('RGB', (size, size))
    for i in range(size):
        for j in range(size):
            if data[i * size + j] == '0':
                image.putpixel([i, j], (0, 0, 0))
            else:
                image.putpixel([i, j], (255, 255, 255))
    image.save(path)


def parse_qrcode(path):
    reader = zxing.BarCodeReader()
    barcode = reader.decode(path)
    return barcode.parsed


if __name__ == '__main__':
    print(png_crc32('temp/newpng.png'))
    print(png_crc32('temp/1116722-20180930112354057-2055962329.png'))
    b = '00000001001110110101010000000' \
        '01111101010100111011110111110' \
        '01000101110010011111010100010' \
        '01000101001010010111010100010' \
        '01000101111011000111110100010' \
        '01111101110000100000010111110' \
        '00000001010101010101010000000' \
        '11111111011111001101111111111' \
        '10010000110011010010000110100' \
        '10100111101010000111100011111' \
        '00110000111001010111001010001' \
        '11111110000000001101101110110' \
        '11100001000011110000111100001' \
        '11001010000010010011111111100' \
        '10010100001001011000101011100' \
        '11100110100000000000000000001' \
        '01010101010101000001010000100' \
        '10010111001011011011001010011' \
        '11011000001001011010000111111' \
        '11100010111001100011101110010' \
        '01011000000011111010000001100' \
        '11111111110010000000011101111' \
        '00000001001100011001010100111' \
        '01111101001001000110011101000' \
        '01000101011010010101000001000' \
        '01000101110101010101001001110' \
        '01000101011010011001011011011' \
        '01111101000001011000110110100' \
        '00000001111100001100011110011'
    # bin2qr(b, 29, 'temp/class10.png')
    print(parse_qrcode('temp/class10.png'))
    print(parse_qrcode('temp/1116722-20180930112354057-2055962329.png'))



