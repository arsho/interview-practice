def rotateImage(a):
    res = []
    a = a[::-1]
    for i in range(len(a)):
        ar = []
        for j in range(len(a)):
            ar.append(a[j][i])
        res.append(ar)
    return res
