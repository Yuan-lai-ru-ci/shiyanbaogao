def modify_lyrics(file_path):
    try:
        with open(file_path, 'r+') as f:
            lines = f.readlines()
            if lines:
                lines[0] = "Blowin' in the wind\n"
            lines.append("\nBob Dylan\n")
            lines.append("1962 by Warner Bros. Inc.")
            f.seek(0)
            f.truncate()
            f.writelines(lines)
        print(f"文件 {file_path} 修改成功。")
    except FileNotFoundError:
        print(f"错误: {file_path} 未找到。")
if __name__ == "__main__":
    initial_lyrics = (
        "How many roads must a man walk down\n"
        "Before they call him a man\n"
        "How many seas must a white dove sail\n"
        "Before she sleeps in the sand\n"
        "How many times must the cannon balls fly\n"
        "Before they're forever banned\n"
        "The answer my friend is blowing in the wind\n"
        "The answer is blowing in the wind\n"
    )
    with open("Blowing in the wind.txt", "w") as f:
        f.write(initial_lyrics)
    modify_lyrics("Blowing in the wind.txt")
