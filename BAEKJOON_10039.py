total = 0

for i in range(5):
    score = int(input("Enter your score: "))

    if score < 40:
        score = 40
    
    total += score

avg = int(total / 5)
print(avg)