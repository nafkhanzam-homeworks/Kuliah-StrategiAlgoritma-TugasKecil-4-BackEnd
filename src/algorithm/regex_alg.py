import re


def get_result(text: str, keyword: str) -> int:
    match = re.search(keyword, text, re.IGNORECASE)
    if match is None:
        return -1
    return match.span()[0]
