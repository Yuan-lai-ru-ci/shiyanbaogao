n = int(input('请输入一个整数(1-9): '))
count=0
for i in range(1, 101):
    if (i % n == 0) or (str(n) in str(i)):
        continue
    count += 1
    if count % 10 == 0:
        print(i)
    else:
        print(i, end=',')
if count % 10 != 0:
    print()

