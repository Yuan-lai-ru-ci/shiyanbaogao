friends_data = {
    '小明': 88888,
    '阿花': 5555555,
    '大壮': 11111,
    '大毛': 1234321,
    '小毛': 1212121
}
def find_QQ(name):
    return friends_data.get(name)

if __name__ == "__main__":
    name_to_find_1 = '大毛'
    qq_number_1 = find_QQ(name_to_find_1)
    if qq_number_1:
        print(f"找到了 {name_to_find_1} 的QQ号: {qq_number_1}")
    else:
        print(f"未找到 {name_to_find_1} 的QQ号。")
    name_to_find_2 = '小红'
    qq_number_2 = find_QQ(name_to_find_2)
    if qq_number_2:
        print(f"找到了 {name_to_find_2} 的QQ号: {qq_number_2}")
    else:
        print(f"未找到 {name_to_find_2} 的QQ号。")
