cas = int(input())
for t in range(cas):
    n = int(input())
    woman = {}
    man = {}
    for i in range(n):
        ar = list(map(int, input().split()))
        woman[ar[0]] = ar[1:]
    for i in range(n):
        ar = list(map(int, input().split()))
        man[ar[0]] = ar[1:]
        
    engaze = {}
    man_free = [i for i in man.keys()]
    while len(man_free)>0:
        for pos, current_man in enumerate(man_free):
            for preferred_woman in man[current_man]:
                if preferred_woman not in engaze:
                    engaze[preferred_woman] = current_man
                    man_free.remove(current_man)
                    break
                else:
                    current_lover = engaze[preferred_woman]
                    current_lover_score = woman[preferred_woman].index(current_lover)
                    current_man_score = woman[preferred_woman].index(current_man)
                    if current_man_score<current_lover_score:
                        engaze[preferred_woman] = current_man
                        man_free.remove(current_man)
                        man_free.append(current_lover)
                        break
    engaze_updated = {}
    for key in engaze:
        engaze_updated[engaze[key]] = key
    for key in sorted(engaze_updated):
        print(key,engaze_updated[key])
