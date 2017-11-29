def containsCloseNums(nums, k):
    d = {}
    for i,v in enumerate(nums):
        if v in d:
            d[v].append(i)
            if d[v][-1] - d[v][-2]<=k:
                return True
        else:
            d[v]=[i]
    return False
