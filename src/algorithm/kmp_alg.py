def generate_table(pattern: str) -> [int]:
    table = [0] * (len(pattern) - 1)
    i = 1
    j = 0
    while i < len(pattern) - 1:
        if pattern[i] == pattern[j]:
            j += 1
        else:
            j = 0
        table[i] = j
        i += 1
    return table


def get_result(text: str, pattern: str) -> int:
    table = generate_table(pattern)
    start_index = 0
    i = 0
    while start_index <= len(text) - len(pattern):
        print(i)
        while i < len(pattern) and text[start_index + i] == pattern[i]:
            i += 1
        if i == len(pattern):
            return start_index
        i = table[i - 1] if i > 0 else 0
        start_index += 1
    return -1
