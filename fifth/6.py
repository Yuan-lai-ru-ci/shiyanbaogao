zimu = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
x = input('请输入一句话（英文）')
y = x.upper()
count = []
for a in zimu:
    c = y.count(a)
    count.append(c)
print(count)

