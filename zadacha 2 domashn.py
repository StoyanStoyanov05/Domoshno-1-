n = input('Kolko chisla iskash da nipishesh ')
a = []

for i in range(int(n)):
    a.append(input('Napishi chislo:'))
    
min = int(a[0])
max = int(a[0])

for i in a:
    if int(i) > max:
        max = int(i)
    elif int(i) < min:
        min = int(i)
print(max - min)