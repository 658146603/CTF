from PIL import Image

pic = Image.new("RGB", (60, 60))
data = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001111111111110000000100110000100000000011100001111111111100001111111111110000000110111000100000000011100001111111111100001100000000110010011111110010000000001100111001000000000100001100000000110010000110110010000000000001111001000000000100001100111100110010000100110010011100000011101001001111100100001100111100110000100000001110011111110010000001001111100100001100111100110000000000001110011110110010000001001111100100001100111100110011100100111111111100110011100000001111100100001100000000110011000000000111100110110110000001000000000100001100000000110010011000000011100011111110011001000000000100001111111111110010011001001001100110110010011001111111111100001111111111110010011001001100000100110010011001111111111100000000000000000010011111110010011000111000100000000000000000000000000000000010001111100010011000011101100000000000000000001110011000111100000001000000011000001111111001111000111000000110000000000000000001000000011000000000011001000000000000000010000001000011100001000000111100110000011000000010000000001110011001111110000000000000010001001110011111000010011000001110011001111110000000000000011001001110011111000010011000001100111000000011111000000010000100000100100111000000100100000001100000000111011000000111000100001100000111000000000000000011100000111110011000001111111100001100011111110010000000000000111001001100000000001100000111001110011111001000100100000000111001001000000000001000000111001110011111001100100100000011100000110011111111000000011100001111111000001110011100000011000000010011111110000000011100001111111000000110001100000000000100000010000000000000011000001110011001000000100100000000000000000110000000000000000000001110011011100000000000000010001001111110000100000000100000011111111101111100000000000011000000001110000000111111100110000001100000000010000000000011100000001110000000111111100111000000100000000010000000001110000100111111111111000000011100111000011000001100000000001111000110001001100111000000011000011100011000000000000000001111100111001100100101111111111001111100001001110011111100001100000111110000100000000010000000111100011000000011100100001000000111110000100000000010000000111000011000000011100100000011011100000011100000000000000001110000011111000001100100000111111100000011000000000000000011100000001101000000100100001111100000110010000100000000011111000010000000001100010000000111100000000010000110000000000000000110000000001100000000000011100100000010011111000011100000001110000000111000100000001100111000111110011111001111111100001010011111111100011000001000111000111110011111001111111100001110011011111100011000000000000000000010011001001110000001110001111000001100000100000000000000000010011000001100000000110000011000001100000100001111111111110010011000111000110000111100011001001100111100001100000000110000111100000011111111001110001000001100111000001100000000110000111100000011111111001110011000001100111000001100111100110000100001000000100001001110011111111100000000001100111100110000100001000001100001001100001111111000000000001100111100110010011000111111111000111110000111000011011100001100111100110000011000110000000000000110000000000011011100001100111100110000011111110000000100001110011000000000011100001100000000110011100100111000011001111100011111111111100000001100000000110011100100111000011001111100011111111111100000001011111111010010011111110011111001001110011111100000011000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"

i = 0

for x in range(0, 60):
    for y in range(0, 60):
        if data[i] == '1':
            pic.putpixel([x, y], (0, 0, 0))
        else:
            pic.putpixel([x, y], (255, 255, 255))
        i = i + 1

pic.show()
pic.save("flag.png")