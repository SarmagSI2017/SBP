# Learning Vector Quantization

import math


def W1Loop1(w1, x, a):
    for i in range(len(w1)):
        print("Data W1 Ke", i + 1)
        w1[i] = w1[i] + (a * (x[i] - w1[i]))
        print(w1[i])
    return w1


def W1Loop2(w1, x, a):
    for i in range(len(w1)):
        print("Data W1 Ke", i + 1)
        w1[i] = w1[i] - (a * (x[i] - w1[i]))
        print(w1[i])
    return w1


def W2Loop1(w2, x, a):
    for i in range(len(w2)):
        print("Data W2 Ke", i + 1)
        w2[i] = w2[i] + (a * (x[i] - w2[i]))
        print(w2[i])
    return w2


def W2Loop2(w2, x, a):
    for i in range(len(w2)):
        print("Data W2 Ke", i + 1)
        w2[i] = w2[i] - (a * (x[i] - w2[i]))
        print(w2[i])
    return w2


def LVQRule(x, w1, w2, a, t):
    w1flag = 0
    w2flag = 0
    for i in range(len(x)):
        print("---------------Data ke-", i + 1, "--------------------")
        for j in range(len(x[i])):
            p = math.pow(x[i][j] - w1[j], 2)
            w1flag = w1flag + p
            q = math.pow(x[i][j] - w2[j], 2)
            w2flag = w2flag + q
        w1flag = math.sqrt(w1flag)
        w2flag = math.sqrt(w2flag)

        if t[i] == 1:
            if w1flag <= w2flag:
                w1 = W1Loop1(w1, x[i], a)
                print(w1)
            else:
                w2 = W2Loop2(w2, x[i], a)
                print(w2)
        if t[i] == 2:
            if w1flag <= w2flag:
                w1 = W1Loop2(w1, x[i], a)
                print(w1)
            else:
                w2 = W2Loop1(w2, x[i], a)
                print(w2)

    return w1, w2


def TesLVQRule(x, w1, w2):
    w1flag = 0
    w2flag = 0
    for k in range(len(x)):
        p = math.pow(x[k] - w1[k], 2)
        w1flag = w1flag + p
        q = math.pow(x[k] - w2[k], 2)
        w2flag = w2flag + q
    if w1flag <= w2flag:
        return 1
    else:
        return 2


if __name__ == "__main__":
    # Bobot Awal
    w1 = [1, 0, 0, 0, 1, 0]  # Menjadi W1 Bobot Awal
    w2 = [0, 1, 1, 1, 1, 0]  # Menjadi W2 Bobot Awal

    # Nilai Alpha
    a = 0.05

    # Max Iter
    maxIter = 10

    # Vektor Input
    x = [[0, 0, 1, 0, 0, 1],
         [0, 0, 1, 0, 1, 0],
         [0, 1, 0, 0, 0, 1],
         [1, 0, 1, 0, 1, 1],
         [0, 0, 1, 1, 0, 0],
         [0, 1, 0, 1, 0, 0],
         [1, 0, 0, 1, 0, 1],
         [0, 1, 1, 1, 1, 1]]

    t = [1, 1, 1, 1, 2, 2, 2, 2]

    # Pemanggilan Fungsi
    for i in range(maxIter):
        print("---------------Epoh ke-", i + 1, "--------------------")
        w1, w2 = LVQRule(x, w1, w2, a, t)
        a = a - (0.1 * a)
        print(a)

    # Nilai W1 dan W2 Baru
    print("\nNilai W1 Akhir : ", w1)
    print("Nilai W2 Akhir : ", w2)

    # Matrix Uji Coba
    x1 = [0, 1, 0, 1, 0, 0]
    x2 = [0, 0, 1, 0, 0, 1]

    # Pemanggilan Fungsi
    x1Class = TesLVQRule(x1, w1, w2)
    x2Class = TesLVQRule(x2, w1, w2)

    # Cetak
    print("\nX1 Memiliki Jarak Terdekat Ke Arah Bobot ke-", x1Class)
    print("X2 Memiliki Jarak Terdekat Ke Arah Bobot ke-", x2Class)