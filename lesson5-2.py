x = int(input('學生數量'))
y = 0
a = []
for i in range(x):
    z = int(input('學生成績'))
    a.append(z)
    y = y+z
print(a)
print(float(y/x))
for i in a:
    print(i)