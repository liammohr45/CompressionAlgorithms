from difflib import SequenceMatcher
from typing import List, Tuple


def find_longest_match(s1:str, s2:str):
    best = 0,0
    for i in range(1, len(s1)+1):
        pre = s1[0:i]
        if pre in s2:
            best = len(s2)-s2.rfind(pre), i
    return best

def lampel_ziv_encode(s: str) -> List[Tuple[int, int, str]]:
    sub = ""
    lst = []
    while s != "":
        tup = find_longest_match(s,sub)
        sub += s[0:tup[1]+1]
        s = s[tup[1]:]
        lst.append((tup[0],tup[1],s[0]))
        s = s[1:]

    return lst



def lampel_ziv_decode(code: List[Tuple[int, int, str]]) -> str:
    s = ""
    for i in code:
        s += s[len(s) - i[0]:len(s) - i[0] + i[1]] + i[2]
    return s


if __name__ == '__main__':
    print(lampel_ziv_encode("ababcbababaa"))
    code = [(0, 0, "a"), (0, 0, "b"), (2, 2, "c"), (4, 3, "a"), (2, 2, "a")]
    print(lampel_ziv_decode(code))
