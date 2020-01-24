# Heteroassociative Memory


def HAMRule(s, t, w):
    for i in range(len(s)):
        print("Data ke-", i + 1)
        for j in range(len(t[0])):
            for k in range(len(s[0])):
                w[k][j] = w[k][j] + s[i][k] * t[i][j]
                print("Data ke-[", k + 1, j + 1, "] : ", w[k][j])
    return w


def TesHAMRule(tes, t, w):
    print()
    for i in range(len(t[0])):
        print("Uji Coba Data Y-in-", i + 1)
        a = 0
        for j in range(len(tes)):
            a = a + (w[j][i] * tes[j])
        if a > 1:
            b = 1
        elif a == 0:
            b = 0
        else:
            b = -1
        print(b)


if __name__ == "__main__":
    # Matrix Input
    s = [[-1, -1, 1, -1, -1, 1],
         [-1, -1, 1, -1, 1, -1],
         [-1, 1, -1, -1, -1, 1],
         [1, -1, 1, -1, 1, 1],
         [-1, -1, 1, 1, -1, -1],
         [-1, 1, -1, 1, -1, -1],
         [1, -1, -1, 1, -1, 1],
         [-1, 1, 1, 1, 1, 1]]

    # Matrix Target/Output
    t = [[-1, 1],
         [-1, 1],
         [-1, 1],
         [-1, 1],
         [1, -1],
         [1, -1],
         [1, -1],
         [1, -1]]

    # Matrix Bobot
    w = [[0 for x in range(len(t[0]))] for y in range(len(s[0]))]

    # Pemanggilan Fungsi
    w = HAMRule(s, t, w)
    print()
    # Matrix Tes
    tes1 = [-1, -1, 1, -1, 1, -1]
    tes2 = [-1, 1, 1, 1, 1, 1]

    # Pemanggilan Fungsi Tes Data
    print("Data Tes Pertama")
    TesHAMRule(tes1, t, w)

    print("\nData Tes Kedua")
    TesHAMRule(tes2, t, w)
