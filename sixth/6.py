import keyword

def is_valid_identifier(s):
    if keyword.iskeyword(s):
        return False, "Valid Identifier, but is a keyword."
    if not (s[0].isalpha() or s[0] == '_'):
        return False, "Invalid Identifier, first char must be alpha or _."
    for char in s[1:]:
        if not (char.isalnum() or char == '_'):
            return False, f"Invalid Identifier, char '{char}' is not alpha, number or _."
    return True, "Valid Identifier."
if __name__ == "__main__":
    test_cases = ['_my_var', 'var123', '1var', 'my-var', 'for', 'MyVar']
    for case in test_cases:
        is_valid, message = is_valid_identifier(case)
        print(f"'{case}': {message}")
