
def main():
    encrypt()
    #decrypt(10,860,[7,3],2)
    #decrypt(7,972,[6,3,1],3)



def encrypt():
    c = []
    k = int(input("enter number of symbols: "))
    for i in range(k):
        c.append(int(input("enter c number " + str(i+1)+": ")))
    M = sum(c)
    msg = input("enter your message(allowed numbers are 1 to "+str(k)+"): ")
    x = [int(msg[i]) for i in range(len(msg))]
    length = len(x)
    b = [1]
    for i in range(k-1):
        b.append(b[i]+c[i])
    r = [0]
    f = [0]
    s = [b[x[0]-1]]
    for i in range(length-1):
        r.append(s[i]%c[x[i+1]-1])
        f.append((s[i]-r[i+1])/c[x[i+1]-1])
        s.append(f[i+1]*M+b[x[i+1]-1]+r[i+1])
    # print("s:" + str(s))
    # print("f:" + str(f))
    # print("x:" + str(x))
    # print("r:" + str(r))
    print("final result: output is: "+str(s[-1]))
    return int(s[-1])

def decrypt(word_length,final_s,c,symbol_number):
    M = sum(c)
    length = word_length
    k = symbol_number
    b = [1]
    f = []
    x = []
    s = [final_s]
    r = []
    for i in range(k - 1):
        b.append(b[i] + c[i])
    for i in range(length-1):
        f.append(int((s[-1]-1)/M))
        remain = s[-1]-(M*f[-1])
        for j in range(k):
            if((j==k-1) and (b[j]<=remain)):
                x.append(j + 1)
                r.append(remain - b[j])
            elif(b[j]<=remain and b[j+1]>remain):
                x.append(j+1)
                r.append(remain-b[j])
        s.append(f[-1]*c[x[-1]-1]+r[-1])
    for j in range(k):
        if(int(b[j])==int(s[-1])):
            x.append(j+1)
    # print("s:" + str(s))
    # print("f:" + str(f))
    # print("x:" + str(x))
    # print("r:" + str(r))
    msg = [x[len(x)-1-i] for i in range(len(x))]
    print("msg is: "+str(msg))



if __name__ == '__main__':
    main()