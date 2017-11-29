def isCryptSolution(crypt, solution):
    solution  = dict((x[0],x[1]) for x in solution)
    ar = []
    flag = True
    for word in crypt:
        word = "".join(solution[i] for i in word if i in solution)
        ar.append(word)
        if word[0]=="0" and len(word)>1:
            flag = False
    ar = list(map(int,ar))
    if (ar[0] + ar[1])!=ar[2]:
        flag = False
    return flag
