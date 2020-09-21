if __name__ == '__main__':
    for i in 'bAcon iS a MEaT prodUcT prePared frOm a pig and UsuALLy cUReD':
        if i.islower():
            print('a', end='')
        elif i.isupper():
            print('b', end='')
    print()

    s = "cbtcqLUBChERV[[Nh@_X^D]X_YPV[CJ"
    num = 0x37
    for i in s:
        print(chr(ord(i) ^ num), end='')