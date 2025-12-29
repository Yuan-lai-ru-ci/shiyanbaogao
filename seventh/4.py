try:
    with open("file1.dat", "rb") as f_in:
        content = f_in.read()
    modified_content = content.replace(b'\r\n', b' ')
    with open("file2.dat", "wb") as f_out:
        f_out.write(modified_content)
    print("文件 file2.dat 已生成。")
except FileNotFoundError:
    print("错误: file1.dat 未找到。请先创建该文件。")
