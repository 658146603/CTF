table = input()
key = '2,3,7,5,13,12,9,1,8,10,4,11,6'
cipher_text = 'NFQKSEVOQOFNP'

first_encrypt = []
for line in table.split('\n'):
    first_encrypt.append(line)

key_index = key.split(",")
second_encrypt = []
for k in key_index:
    second_encrypt.append(first_encrypt[int(k) - 1])
    print(first_encrypt[int(k) - 1])

for i, ch in enumerate(cipher_text):
    line = second_encrypt[i]
    split_index = line.index(ch)
    temp = []
    temp[0:len(line) - split_index + 1] = line[split_index:len(line)]
    temp[len(temp):] = line[0:split_index]
    second_encrypt[i] = "".join(temp)
print('----------------------------------------------')
for plain in second_encrypt:
    print(plain)
print('----------------------------------------------')
for index in range(len(second_encrypt[0])):
    s = ''
    for plain in second_encrypt:
        s += plain[index]
    print(s.lower())
