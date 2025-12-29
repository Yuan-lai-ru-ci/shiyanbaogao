def clean_list(coffee_data):
    """
    处理咖啡列表，只提取其中的咖啡名称。
    """
    cleaned_names = []
    for item in coffee_data:
        name = "".join(filter(str.isalpha, item))
        cleaned_names.append(name)
    return cleaned_names

if __name__ == "__main__":
    coffee_list = ['32Latte', 'Americano30', '34Cappuccino', 'Mocha35']
    cleaned_coffee_names = clean_list(coffee_list)
    print("处理后的咖啡列表如下:")
    for i, name in enumerate(cleaned_coffee_names, 1):
        print(f"{i}. {name}")
