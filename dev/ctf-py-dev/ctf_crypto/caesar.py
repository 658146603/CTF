if __name__ == '__main__':
    s = input()
    for i in range(26):
        t = ""
        for c in s:
            if 'a' <= c <= 'z':
                t += chr(ord('a') + ((ord(c) - ord('a')) - i) % 26)
            elif 'A' <= c <= 'Z':
                t += chr(ord('A') + ((ord(c) - ord('A')) - i) % 26)
            else:
                t += c
        print(t.lower())
