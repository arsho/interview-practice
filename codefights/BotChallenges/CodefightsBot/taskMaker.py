import re
def taskMaker(source, challengeId):
    ar = []
    flag = False
    for line in source:
        try:
            comment = re.search(r'//DB \d+//',line)
            num = int(comment.group()[2:-2].split(" ")[1])
            if num==challengeId and flag==False:
                start,end = comment.span()
                flag = True
                line = list(line)
                s = "".join(line[:start])
                s+= "".join(line[end:])
                del ar[-1]
                ar.append(s)
        except:
            ar.append(line)
    return ar
            

