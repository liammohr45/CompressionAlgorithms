# This is a sample Python script.
from typing import List


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def b_i(prob: dict):
    sm = 1
    lst = {}
    for j in prob:
        lst[j]=sm
        sm += prob[j]

    return lst


def encodeAns(prob, M, x):
    r = []
    f = []
    s = []
    b = b_i(prob)
    s.append(b[x[0]])
    for i in range(1, len(x)):
        r.append(s[i - 1] % prob[x[i]])
        f.append((s[i - 1] - r[i-1]) / prob[x[i]])
        s.append(f[i-1] * M + b[x[i]] + r[i-1])
    return s

def decodeAns(prob:dict, M, c):
    r = []
    f = []
    s = []
    v=[]
    out = []
    b = b_i(prob)
    s.append(c)
    i=0
    possible_b = [b[x] for x in prob.keys()]
    while s[i] not in possible_b:
        v.append(1+(s[i]-1)%M)
        for j in prob:
            if b[j] <=v[i]<b[j]+prob[j]:
                out.append(j)
                break
        r.append(v[i]-b[out[i]])
        f.append((s[i] - v[i]) / M)
        s.append(prob[out[i]]*f[i]+r[i])
        i+=1
    for j in prob:
        if b[j] == s[i]:
            out.append(j)
            return out

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    prob = {"1": 3, "0": 7}
    c = encodeAns(prob,10, "0001010001")
    print(c)
    print(decodeAns(prob,10,1121))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
