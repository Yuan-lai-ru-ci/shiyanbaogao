import random
nb = random.randint(1, 27)
x = 37*nb
h = x // 100
t = (x % 100) // 10
u = x % 10
b = [h, t, u]
b_shifted = [b[2], b[0], b[1]]
y = b_shifted[0] * 100 + b_shifted[1] * 10 + b_shifted[2]
print(f"原始数字x: {x}")
print(f"轮换后的数字y: {y}")
if y % 37 == 0:
    print('验证结果: 真')
else:
    print('验证结果: 假')
