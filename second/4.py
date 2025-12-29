x = input('请输入一个四位数：')
x = int(x)
aList = list(str(x))
bList = aList[::-1]
n = ''.join(bList)
print(n)
