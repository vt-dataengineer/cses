# Input:
# 5
# 2 3 1 5
#
# Output:
# 4

n = int(input())
s = 0
for _ in range(n-1):
    arr = map(int,input().split())
    for x in arr:
        s+=x


print(int(n*(n+1)/2-s))
