def twonumSum(n, lst):
    seen = set()
    for num in lst:
        complement = n - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    return "not found"

if __name__ == "__main__":
    default_list = [1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 18, 19, 20, 21, 29, 34, 54, 65]
    try:
        target_sum = int(input("请输入目标整数 n: "))
        result = twonumSum(target_sum, default_list)
        print(result)
    except ValueError:
        print("输入无效，请输入一个整数。")
