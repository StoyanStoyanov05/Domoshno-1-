c = 0
b = 0
a = []
for i in range(2000, 5001):
    c = 0
    b = i
    a.clear()
for j in range(4):
    if ((b % 10) % 2) == 0:
    c += 1
a.append((y % 10))

    b //= 10
    a.reverse()
if c == 4:
    print(i, end = ':')
    
for j in range(len(a)):
    if j != 3:
        print(a[j], end=',')
        
    else:
        print(a[j])