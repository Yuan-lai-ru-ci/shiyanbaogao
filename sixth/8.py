def minNum(*args):
    if not args:
        return None 
    digits = []
    for num in args:
        digits.extend(str(num))
    digits.sort()
    if digits[0] == '0':
        for i in range(1, len(digits)):
            if digits[i] != '0':
                digits[0], digits[i] = digits[i], digits[0]
                break
    return int("".join(digits))
if __name__ == "__main__":
    test_case_1 = (1, 3, 0, 5)
    result_1 = minNum(*test_case_1)
    print(f"用数字 {test_case_1} 组成的最小数是: {result_1}")
    test_case_2 = (4, 6, 2, 9)
    result_2 = minNum(*test_case_2)
    print(f"用数字 {test_case_2} 组成的最小数是: {result_2}")
    test_case_3 = (0, 0, 2, 1)
    result_3 = minNum(*test_case_3)
    print(f"用数字 {test_case_3} 组成的最小数是: {result_3}")
