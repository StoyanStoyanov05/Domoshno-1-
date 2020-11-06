y = ''
str = input('napishi simvoli: ')

str = list(str)
str.sort()

print(str)

for i in range(len(str)):
    print(i)
    if str[i] != y:
        print(''', str[i], ''', 'poqvi se ', str.count(str[i]), 'puti v tozi string')
    y = str[i]