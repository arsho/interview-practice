def launchSequenceChecker(systemNames, stepNumbers):
    d = {}
    for i in range(len(systemNames)):
        cur_sys = systemNames[i]
        cur_step = stepNumbers[i]
        if cur_sys not in d:
            d[cur_sys] = [cur_step]
        else:
            d[cur_sys].append(cur_step)
    
    for k in d.keys():
        if len(d[k])>1:
            for i in range(1,len(d[k])):
                if d[k][i]<=d[k][i-1]:
                    return False
    return True

