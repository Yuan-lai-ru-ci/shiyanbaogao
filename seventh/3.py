def process_contacts(input_file, output_file):
    contacts = {}
    try:
        with open(input_file, "r") as f_in:
            for line in f_in:
                parts = line.strip().split()
                if len(parts) == 2:
                    name, number = parts
                    contacts[name] = number
        with open(output_file, "w") as f_out:
            for name, number in contacts.items():
                f_out.write(f"{name} {number}\n")
        print(f"文件 {output_file} 已生成。")
        return contacts
    except FileNotFoundError:
        print(f"错误: 输入文件 {input_file} 未找到。")
        return None
def find_contact(name, contacts):
    return contacts.get(name, "Not found")
if __name__ == "__main__":
    initial_data = "Zhang 2301\nLi 2305\nSun 2304\nZhang 2302\nLi 2305\n"
    with open("data.txt", "w") as f:
        f.write(initial_data)
    processed_contacts = process_contacts("data.txt", "data_out.txt")
    if processed_contacts:
        name_to_find = input("请输入要查找的联系人姓名: ")
        result = find_contact(name_to_find, processed_contacts)
        print(result)
