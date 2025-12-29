def count_str(s):
    words = s.split()
    first_char_counts = {}
    for word in words:
        if word: 
            first_char = word[0].lower()
            if 'a' <= first_char <= 'z':
                first_char_counts[first_char] = first_char_counts.get(first_char, 0) + 1
    result = []
    for i in range(ord('a'), ord('z') + 1):
        char = chr(i)
        result.append(first_char_counts.get(char, 0))
    return result
if __name__ == "__main__":
    test_string = "Python C Go Java PHP Python Java"
    counts = count_str(test_string)
    print(f"测试字符串: \"{test_string}\"")
    print(f"首字母统计结果 (a-z):\n{counts}")
    print("\n详细统计:")
    for i, count in enumerate(counts):
        if count > 0:
            print(f"  字母 '{chr(ord('a') + i)}' 出现了 {count} 次")
