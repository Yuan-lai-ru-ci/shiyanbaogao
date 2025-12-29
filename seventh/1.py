def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
try:
    m_str = input("请输入起始整数m: ")
    n_str = input("请输入结束整数n: ")
    m = int(m_str)
    n = int(n_str)
    if m >= n:
        print("m 必须小于 n")
    else:
        with open("out.txt", "w") as f_out:
            for num in range(m, n + 1):
                if is_prime(num):
                    f_out.write(str(num) + "\n")
        with open("out.txt", "r") as f_in, open("out2.txt", "w") as f_out2:
            for line in f_in:
                stripped_line = line.strip()
                new_line = f"abcde{stripped_line}abcde\n"
                f_out2.write(new_line)
        print("文件 out.txt 和 out2.txt 已生成。")
except ValueError:
    print("输入无效，请输入整数。")
