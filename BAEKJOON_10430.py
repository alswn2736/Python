A = input("Enter A: ")
B = input("Enter B: ")
C = input("Enter C: ")

A = int(A)
B = int(B)
C = int(C)

print(int((A + B) % C))
print(int(((A % C) + (B % C)) % C))
print(int((A * B) % C))
print(int(((A % C) * (B % C)) % C))