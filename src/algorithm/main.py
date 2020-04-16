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


def get_count(sentence: str, keyword: str) -> str:
    pattern = r"(?:(?: (\d+(?:[\.,]\d)*) (?:\D*))|(?:.?))(" + \
        keyword + r")(?:(?:(?:\D*?) (\d+(?:[\.,]\d)*)) |(?:.?))"
    match = re.search(pattern, sentence, re.IGNORECASE)
    border_left = match.span(1)[1]
    span = match.span(2)
    border_right = match.span(3)[0]
    if border_left == -1 and border_right == -1:
        return ""
    if border_left == -1:
        return match[3]
    elif border_right == -1:
        return match[1]
    else:
        return match[3] if span[0]-border_left > border_right-span[1] else match[1]


def get_time(sentence: str, keyword: str) -> str:
    pass


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
    print(json.dumps(map(lambda sentence: {
        "sentence": sentence,
        "index_found": get_result(sentence, keyword),
        "time": get_time(sentence, keyword),
        "count": get_count(sentence, keyword)
    }, split_sentences(data["text"]))))
