n = int(input())
y = list(map(int, input().split()))

odd_count = sum([1 for num in y if num % 2 != 0])
even_count = sum([1 for num in y if num % 2 == 0])

if odd_count > even_count:
    for i in range(n):
        if y[i] % 2 == 0:
            print(i + 1) 
            break
else:
    for i in range(n):
        if y[i] % 2 != 0:
            print(i + 1)  
            break