S = int(input())    #총 몇 번 반복할지

for i in range(S):
    R, P = input().split(' ')   #R: 문자열 반복 횟수, P: 해당 문자열
    res = ''
    for i in P:
        res += int(R) * i
    print(res)