def merge_files(subtitles_file, article_file, output_file):
    try:
        with open(subtitles_file, 'r') as f_sub, open(article_file, 'r') as f_art:
            sub_lines = f_sub.readlines()
            art_lines = f_art.readlines()
        with open(output_file, 'w') as f_out:
            max_len = max(len(sub_lines), len(art_lines))
            for i in range(max_len):
                if i < len(sub_lines):
                    f_out.write(sub_lines[i])
                if i < len(art_lines):
                    f_out.write(art_lines[i])
        print(f"文件 {output_file} 已生成。")
    except FileNotFoundError as e:
        print(f"错误: {e.filename} 未找到。")
def find_longest_line(file_path):
    longest_line = ""
    line_number = -1
    try:
        with open(file_path, 'r') as f:
            for i, line in enumerate(f, 1):
                if len(line) > len(longest_line):
                    longest_line = line
                    line_number = i
        return line_number, longest_line.strip()
    except FileNotFoundError:
        return -1, "文件未找到"
if __name__ == "__main__":
    with open("subtitles.srt", "w") as f:
        f.write("00:00:00,100 --> 00:00:01,700\n每天产生大量的数据\n\n")
        f.write("00:00:01,740 --> 00:00:03,620\n实时的动态的\n\n")
        f.write("00:00:04,740 --> 00:00:05,980\n实时的非结构性数据\n\n")
        f.write("00:00:06,220 --> 00:00:08,380\n甚至教育每个人都会产生很多数据\n\n")
        f.write("00:00:28,220 --> 00:00:30,380\n这些数据可以以文件的形式\n\n")
    with open("article.txt", "w") as f:
        f.write("line 0\nline 1\nline 2\nline 3\nline 4\nline 5\nline 6\nline 7\n")
    merge_files("subtitles.srt", "article.txt", "file.txt")
    ln, line_content = find_longest_line("file.txt")
    if ln != -1:
        print(f"\n在 file.txt 中，第 {ln} 行的长度最长。")
        print(f"内容为: {line_content}")
        print(f"该行共有 {len(line_content)} 个字符。")
