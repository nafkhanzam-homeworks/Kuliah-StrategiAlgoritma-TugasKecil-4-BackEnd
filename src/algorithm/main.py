import sys
import json
import re
import kmp_alg
import regex_alg
import boyer_moore_alg


def fail(alg: str):
    raise RuntimeError(f"Algorithm {alg} is not found!")


def split_sentences(text: str):
    pattern = r"(?:(?<=\. )|(?<=\.$)|(?<=^))((?!\n).*?)(?:(?=\. |\.$|\n))"
    return re.findall(pattern, text, re.MULTILINE)


def calc_range(a: tuple, b: tuple) -> int:
    return b[0] - a[1] if a[1] < b[0] else a[0] - b[1]


def get_count(sentence: str, keyword: str) -> str:
    """
    Abandoned function, but felt very disturbing to delete
    """
    pattern = r"(?:(?:(?:^| )(\d+(?:\.\d+)*) (?:.*))|(?:.?))(" + \
        keyword + r")(?:(?:(?:.*?) (\d+(?:\.\d+)*))(?: |$)|(?:.?))"
    match = re.search(pattern, sentence, re.IGNORECASE)
    return match[3] if calc_range(match.span(1), match.span(2)) > calc_range(match.span(2), match.span(3)) else match[1]


def get_count_by_span(sentence: str, keyword_span: tuple) -> str:
    pattern = r"(?:^|[^\w\.-_-])(\d+(?:[\.,]\d{3})*)(?:$|[^\w\.-_-])"
    matches = re.finditer(pattern, sentence, re.IGNORECASE)
    res = None
    min = len(sentence) + 1
    for match in matches:
        v = calc_range(match.span(), keyword_span)
        if v < min:
            min = v
            res = match[1]
    return res


def get_time(sentence: str, keyword: str, default: str) -> str:
    return ""


if __name__ == "__main__":
    data = json.loads(sys.argv[1])
    alg = data["algorithm"]
    get_result = {
        "Boyer-Moore": boyer_moore_alg,
        "KMP": kmp_alg,
        "Regex": regex_alg
    }.get(alg, lambda: fail(alg)).get_result

    """
        Result format: {
            sentence: string;
            index_found: number;
            time: string;
            count: number;
        }[]
    """
    keyword = data["keyword"]
    result = []
    for sentence in split_sentences(data["text"]):
        idx = get_result(sentence, keyword)
        if idx != -1:
            result.append({
                "sentence": sentence,
                "index_found": idx,
                "time": get_time(sentence, keyword, ""),
                "count": get_count_by_span(sentence, (idx, idx + len(keyword)))
            })
    print(json.dumps(result))
