def numsChain(num):
    chain = []
    while num not in chain:
        chain.append(num)
        sum_of_squares = 0
        for digit in str(num):
            sum_of_squares += int(digit) ** 2
        num = sum_of_squares
    chain.append(num)
    return chain

if __name__ == "__main__":
    try:
        input_num = int(input("请输入一个正整数: "))
        if input_num <= 0:
            print("请输入正整数。")
        else:
            result_chain = numsChain(input_num)
            print("->".join(map(str, result_chain)))
    except ValueError:
        print("输入无效，请输入一个整数。")
