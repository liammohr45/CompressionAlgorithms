""" Implemented by Liam Mohr """
import sys


def rl_encode(s):
    out = ""
    count = 0
    if len(s) != 0:
        out = s[0]
    for i in range(len(s)):
        if out[-1] == s[i]:
            count += 1
        else:
            out += str(count)
            out += s[i]
            count = 1
    return out + str(count)


def rl_decode(s):
    out = ""
    for i in range(len(s)):
        if not s[i].isnumeric():
            out += s[i]
        else:
            out += out[-1] * (int(s[i]) - 1)
    return out


if __name__ == "__main__":
    if len(sys.argv) != 3 and sys.argv[1].lower() not in ["encode", "decode"]:
        Exception("Illegal input")
    if sys.argv[1].lower() == "encode":
        print("Encoding " + sys.argv[2] + ":\n" + rl_encode(sys.argv[2]))
    else:
        print("Decoding " + sys.argv[2] + ":\n" + rl_decode(sys.argv[2]))
