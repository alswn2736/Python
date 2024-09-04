duplication = input()
string = ''

length = len(duplication) - 1
for i in range(length):
    if duplication[i] != duplication[i + 1]:
        string += duplication[i]

string += duplication[length]
print(string)