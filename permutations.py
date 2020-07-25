n = int(input())
if n == 1:
    print(1)
elif n == 2 or n == 3:
    print('NO SOLUTION')
else:
    for x in range(2,n+1,2):
        print(x,end=' ')
    for x in range(1,n+1,2):
        print(x,end=' ')
