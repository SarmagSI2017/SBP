# Hebb Rule


def HebbRule(x1, x2, b, t):
    w1 = 0
    w2 = 0
    bflag = 0
    for i in range(len(t)):
        print("Data Ke -", i + 1)
        w1 = w1 + x1[i] * t[i]
        print(w1)
        w2 = w2 + x2[i] * t[i]
        print(w2)
        bflag = bflag + b[i] * t[i]
        print(bflag)
    return w1, w2, bflag


def TesHebbRule(x1, x2, t, w1, w2, bflag):
    print("Uji Coba : ")
    for j in range(len(t)):
        a = bflag + (x1[j] * w1) + (x2[j] * w2)
        if a > 0:
            b = 1
        elif a == 0:
            b = 0
        else:
            b = -1
        print("Uji Coba Data [", x1[j], x2[j], "] : ", a, "Dengan Nilai Tanpa Bobot : ", b)


if __name__ == '__main__':
    print("Input Data")
    x1 = [int(x1) for x1 in input("Masukkan Nilai X1 : ").split()]
    x2 = [int(x2) for x2 in input("Masukkan Nilai x1 : ").split()]
    t = [int(t) for t in input("Masukkan Nilai Target : ").split()]
    b = [1 for b in range(len(t))]
    w1, w2, bflag = HebbRule(x1, x2, b, t)
    TesHebbRule(x1, x2, t, w1, w2, bflag)
