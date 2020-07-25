# Input:
# 3
#
# Output:
# 3 10 5 16 8 4 2 1

n = int(input())
l =[]
l.append(n)
while(n!=1):
    if n%2 ==0:
        n = n//2
        l.append(n)
    else:
        n = n*3+1
        l.append(n)

for x in l:
    print(x,end=' ')

