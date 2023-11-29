import math


def get_interval(plaintext: list[int], prob: list[float]):
    start = 0
    delta = 1
    for i, x in enumerate(plaintext):
        start += delta * sum(prob[:x])
        delta *= prob[x]
    return start, delta


def get_binary(x: float, delta: float):
    digits = 1 + math.ceil(-math.log2(delta / 2))
    n = int(x * 2 ** digits)
    return bin(n)


def encode(plaintext: list[int], prob: list[float]):
    start, delta = get_interval(plaintext=plaintext, prob=prob)
    x = start + delta / 2
    binary = get_binary(x=x, delta=delta)[2:]
    return binary


def get_plaintext(x: float, length: int, prob: list[float]):
    plaintext = []
    for _ in range(length):
        char = len(prob) - 1
        while sum(prob[:char]) > x:
            char -= 1
        plaintext.append(char)
        x = (x - sum(prob[:char])) / prob[char]
    return plaintext


def get_x(binary: str):
    N = int(binary, base=2)
    x = N / 2 ** len(binary)
    return x


def decode(binary: str, prob: list[float], length: int):
    x = get_x(binary=binary)
    plaintext = get_plaintext(x=x, length=length, prob=prob)
    return plaintext


def main():
    prob = [0.6, 0.3, 0.1]
    plaintext = [1, 0, 0, 0, 2, 0, 0]
    binary = encode(plaintext=plaintext, prob=prob)
    print(binary)
    decoded = decode(binary=binary, prob=prob, length=len(plaintext))
    print(decoded)


if __name__ == '__main__':
    main()
