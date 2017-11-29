def areFollowingPatterns(strings, patterns):
    flag = True
    d = {}
    e = {}
    for i in range(len(patterns)):
        p = patterns[i]
        w = strings[i]
        if p in d:
            if d[p]!=w:
                flag = False
                break
        else:
            d[p] = w
        if w in e:
            if e[w]!=p:
                flag = False
                break
        else:
            e[w] = p        
    return flag
