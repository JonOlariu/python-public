a = float(input('side 1: '))
b = float(input('side 2: '))
c = float(input('side 3: '))
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('Triangle area %0.2f' %area)