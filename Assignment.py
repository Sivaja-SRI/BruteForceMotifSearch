import itertools

DNA = [ "acaccggcaacctgaaacaaacgctcagaaccagaagtgccctgatagac",
        "ccaggtacttaggtcctctgtgcgaatctatgcgtttccaagtactggtg",
        "aaacgttagtgcaccctctttcttcgtggctctggccaacaaacgttagt"]
        
t = 3
n = 50
l =7

def bruteForceMotifSearch(DNA, t, n, l):
    data = itertools.product(range(n - l), repeat=t)
    bestScore = 0
    bestMotif = []
    for s in data:
        score = scoreCalculate(DNA, s)
        if score > bestScore:
            bestMotif = s
            bestScore = score

    print("BestScore is: ", bestScore)
    print("BestMotif is: ", bestMotif)

    return bestMotif

def scoreCalculate(DNA, s):
    differentArr = ['a', 'c', 'g', 't']
    arr = []
    z = 0
    for x in DNA:
        array = []
        for y in x[s[z]:s[z] + l]:
            array.append(y)

        z += 1
        arr.append(array)
    i = 0
    arrayM = []

    p = 0
    while p < len(differentArr):
        q = 0
        arr1 = []
        while q < l:
            arr1.append(0)
            q += 1
        arrayM.append(arr1)
        p += 1
    while i < len(differentArr):
        j = 0
        while j < l:
            k = 0
            while k < t:
                if differentArr[i] == arr[k][j]:
                    arrayM[i][j] += 1
                k += 1
            j += 1
        i += 1

        x = 0
        sum = 0
        while x < l:
            y = 0
            max = 0
            while y < len(arrayM):
                if arrayM[y][x] > max:
                    max = arrayM[y][x]
                y += 1
            sum += max
            x += 1
    return sum

bruteForceMotifSearch(DNA, t, n, l)
