import itertools

if __name__ == '__main__':
    s = "aeoiu"
    sum_result = []
    num_sum_result = []
    cipher = "ouauuuoooeeaaiaeauieuooeeiea"
    for i in itertools.permutations(s, 5):  # 找出所有全排列
        sum_result.append("".join(i))
    for i in sum_result:
        temp = ""
        for j in cipher:
            temp += str(i.index(j) + 1)
        num_sum_result.append(temp)
    for i in num_sum_result:
        ans = ""
        for j in range(0, len(i), 2):
            xx = (int(i[j]) - 1) * 5 + int(i[j + 1]) + 96
            if xx > ord('i'):
                xx += 1
            ans += chr(xx)
        print(ans)
