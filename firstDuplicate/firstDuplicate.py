def firstDuplicate(a):
    len_a = len(a)
    d = {}
    answer = -1
    for i,v in enumerate(a):
        if v in d.keys():
            answer = v
            break
        else:
            d[v] = i
    return answer
