import kmp_alg
import regex_alg
import boyer_moore_alg

tests = [
    ("Doubt", "Here's the thing. She doesn't have anything to prove, but she is going to anyway. That's just her character. She knows she doesn't have to, but she still will just to show you that she can. Doubt her more and she'll prove she can again. We all already know this and you will too."),
    ("", "It was a concerning development that he couldn't get out of his mind. He'd had many friends throughout his early years and had fond memories of playing with them, but he couldn't understand how it had all stopped. There was some point as he grew up that he played with each of his friends for the very last time, and he had no idea that it would be the last."),
    ("came", "Then came the night of the first falling star. It was seen early in the morning, rushing over Winchester eastward, a line of flame high in the atmosphere. Hundreds must have seen it and taken it for an ordinary falling star. It seemed that it fell to earth about one hundred miles east of him."),
    ("baaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaa"),
    ("to it.", "The red glint of paint sparkled under the sun. He had dreamed of owning this car since he was ten, and that dream had become a reality less than a year ago. It was his baby and he spent hours caring for it, pampering it, and fondling over it. She knew this all too well, and that's exactly why she had taken a sludge hammer to it.")
]


def res(test):
    res = -1
    try:
        res = test[1].index(test[0])
    except:
        pass
    return res


def test_kmp():
    for test in tests:
        assert kmp_alg.get_result(test[1], test[0]) == res(test)


def test_regex():
    for test in tests:
        assert regex_alg.get_result(test[1], test[0]) == res(test)


def test_bm():
    for test in tests:
        assert boyer_moore_alg.get_result(test[1], test[0]) == res(test)
