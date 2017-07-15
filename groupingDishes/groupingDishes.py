def groupingDishes(dishes):
    d = {}
    for ar in dishes:
        dish = ar[0]
        ingredients = ar[1:]
        for ingredient in ingredients:
            if ingredient in d.keys():
                d[ingredient].append(dish)
            else:
                d[ingredient]=[dish]
    for key in d.keys():
        d[key] = sorted(d[key])
    sorted_ingredients = sorted(d.keys())
    all_res = [[i] + d[i] for i in sorted_ingredients]
    return [i for i in all_res if len(i)>2]
