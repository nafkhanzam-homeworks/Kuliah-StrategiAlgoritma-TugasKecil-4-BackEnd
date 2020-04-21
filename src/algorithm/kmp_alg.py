def generate_longest_prefix_suffix_table(pattern: str) -> [int]:
    plen = len(pattern)
    table = [0] * (plen - 1)
    i = 1
    j = 0
    while i < plen - 1:
        if pattern[i] == pattern[j]:
            j += 1
        else:
            j = 0
        table[i] = j
        i += 1
    return table


def get_result(text: str, pattern: str) -> int:
    table = generate_longest_prefix_suffix_table(pattern)
    start_index = 0
    i = 0
    plen = len(pattern)
    while start_index <= len(text) - plen:
        while i < plen and text[start_index + i] == pattern[i]:
            i += 1
        if i >= plen:
            return start_index
        start_index += 1 if i == 0 else i - table[i - 1]
        i = 0 if i == 0 else table[i - 1]
    return -1
