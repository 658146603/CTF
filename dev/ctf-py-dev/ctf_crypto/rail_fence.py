# 爆破
def d1(cipher):
    print('[d1] CIPHER=' + cipher)
    cipher_len = len(cipher)
    n_list = []
    for i in range(2, cipher_len):
        n_list.append(i)

    for n in n_list:
        group_num = cipher_len // n
        last_group_n = -1
        if (cipher_len % n) != 0:
            group_num += 1
            last_group_n = cipher_len % n
        group = {i: '' for i in range(group_num)}
        # 依次取出一个字符，并放在相应的分组中
        k = -1
        group_num_bak = group_num
        for j in range(cipher_len):
            k += 1
            if k == group_num:
                k = 0
            group.update({k: group[k] + cipher[j]})
            if (last_group_n != -1) and (k == (group_num - 1)) and (len(group[k]) == last_group_n):
                group_num -= 1
                k = -1
                last_group_n = -1
        result = ''
        for i in range(group_num_bak):
            result = result + group[i]
        print('N=' + str(n) + ', RESULT=' + result.lower())


# 只计算可整除的N
def d0(cipher):
    print('[d0] CIPHER=' + cipher)
    cipher_len = len(cipher)
    n_list = []
    for i in range(2, cipher_len):
        if cipher_len % i == 0:
            n_list.append(i)

    for n in n_list:
        group_num = cipher_len // n
        group = {i: '' for i in range(group_num)}
        # 依次取出一个字符，并放在相应的分组中
        for j in range(cipher_len):
            k = j % group_num
            group.update({k: group[k] + cipher[j]})
        result = ''
        for i in range(group_num):
            result = result + group[i]
        print('N=' + str(n) + ', RESULT=' + result.lower())


if __name__ == '__main__':
    d0('15263748')
    d1('15263748')
    d1('15a26b37c48')
    d1('16c27384a5b')
    d1('Gnsol}elhranyakgimri{uednssa-g1onwf8')
    d1('lk2j9Gh}AgfY4ds-a6QW1#k5ER_T[cvLbV7nOm3ZeX{CMt8SZo]U')
    d0('lk2j9Gh}AgfY4ds-a6QW1#k5ER_T[cvLbV7nOm3ZeX{CMt8SZo]U')
