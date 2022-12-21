
a1, d, n = map(int, input().split())
for i in range (1,n+1):
    if(i == 1):
        print(a1, end= " ")
    else:
        print(a1 + d, end= " ")
        a1 += d