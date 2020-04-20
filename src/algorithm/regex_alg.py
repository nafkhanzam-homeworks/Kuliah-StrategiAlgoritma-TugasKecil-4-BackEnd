import re


def get_result(text: str, pattern: str) -> int:
    match = re.search(pattern, text, re.IGNORECASE)
    if match is None:
        return -1
    return match.span()[0]
