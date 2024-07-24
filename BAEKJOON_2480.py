A, B, C = map(int, input().split())

if A == B == C :
    prize = B * 1000 + 10000
elif A == B :
    prize = A * 100 + 1000
elif B == C : 
    prize = B * 100 * 1000
elif C == A :
    prize = C * 100 + 1000
else :
    dice = [A, B, C]
    dice.sort()
    prize = dice[2] * 100

print(prize)