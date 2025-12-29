x = int(input('请输入一个2-1000整数'))
x_input = x
n = 2
i = 1
list = []
for i in range(1000):
    while x % n == 0:
        list.append(n)
        x //= n
    n += 1

end = ''
for i in list[:-1]:
    end += str(i) + '*'
end += str(list[-1])
print(x_input, '=', end)
