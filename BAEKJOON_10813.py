N, M = map(int, input().split())
total = []
for i in range(1,N+1):
    total.append(i)
tmp=0
for n in range(M):
    i,j=map(int,input().split())
    
    tmp=total[i-1]
    total[i-1]=total[j-1]
    total[j-1]=tmp

for i in range(N):
    print(total[i],end=" ")