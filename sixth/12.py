def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

if __name__ == "__main__":
    try:
        num1 = int(input("请输入第一个整数: "))
        num2 = int(input("请输入第二个整数: "))
        
        if num1 < 0 or num2 < 0:
            print("请输入非负整数。")
        else:
            result = gcd_recursive(num1, num2)
            print(f"{num1} 和 {num2} 的最大公约数是: {result}")
            
    except ValueError:
        print("输入无效，请输入整数。")
