from typing import Dict


def generate_last_occurences_table(pattern: str) -> Dict[str, int]:
    size = len(pattern)
    res = {}
    for i in range(size):
        res[pattern[i]] = i
    return res


def get_result(text: str, pattern: str) -> int:
    table = generate_last_occurences_table(pattern)
    plen = len(pattern)
    p = plen - 1
    start_index = 0
    while start_index <= len(text) - plen:
        if p < 0:
            return start_index
        t = start_index + p
        if pattern[p] == text[t]:
            p -= 1
        else:
            last = table.get(text[t])
            if last == None or last >= p:
                start_index += p + 1
            else:
                start_index += p - last
            p = plen - 1
    return -1
