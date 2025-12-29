import random
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
is_prime1 = True
if num1 < 2:
    is_prime1 = False
else:
    for i in range(2, num1):
        if num1 % i == 0:
            is_prime1 = False
            break 
if is_prime1:
    print(f"{num1} 是素数。")
else:
    print(f"{num1} 不是素数。")
is_prime2 = True
if num2 < 2:
    is_prime2 = False
else:
    for i in range(2, num2):
        if num2 % i == 0:
            is_prime2 = False
            break
if is_prime2:
    print(f"{num2} 是素数。")
else:
    print(f"{num2} 不是素数。")
gcd_val = 1
for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd_val = i 
if gcd_val == 1:
    print(f"{num1} 和 {num2} 互质。")
else:
    print(f"{num1} 和 {num2} 不互质，它们的最大公约数是 {gcd_val}。")
