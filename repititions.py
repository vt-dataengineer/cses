# Input:
# ATTCGGGA
#
# Output:
# 3
s = str(input())
c = 0
ans = 1
l = 'A'
for x in s:
    if x == l:
        c+=1
        ans = max(c,ans)
    else:
        l = x
        c=1


print(ans)
