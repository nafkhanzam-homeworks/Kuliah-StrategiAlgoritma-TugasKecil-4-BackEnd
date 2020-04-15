import sys
import json
import kmp_alg
import regex_alg
import boyer_moore_alg


def fail(alg: str):
    raise RuntimeError(f"Algorithm {alg} is not found!")


if __name__ == "__main__":
    data = json.loads(sys.argv[1])
    alg = data["algorithm"]
    function = {
        "Boyer-Moore": boyer_moore_alg.get_result,
        "KMP": kmp_alg.get_result,
        "Regex": regex_alg.get_result
    }.get(alg, lambda: fail(alg))

    """
        Result format: {
            time: string;
            count: number;
        }
    """
    print(json.dumps(function(data["text"], data["keyword"])))
