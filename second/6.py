x,y = input('请输入两个数字用 隔开').split()
x_y1 = int(x)**int(y)
def zhishu(n, m):
    result = 1
    for i in range(m):
        result *= n
    return result
x_y2 = zhishu(int(x),int(y))
print(x_y1)
print(x_y2)