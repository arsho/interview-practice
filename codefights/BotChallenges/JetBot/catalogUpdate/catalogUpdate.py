def catalogUpdate(catalog, updates):
    d = {}
    for cat in catalog:
        d[cat[0]]=cat[1:]
    for cat in updates:
        if cat[0] in d.keys():
            d[cat[0]]+=cat[1:]
        else:
            d[cat[0]] = cat[1:]
    final_catalog = []
    for cat in sorted(d.keys()):
        temp_list = [cat]
        temp_list+=sorted(d[cat])
        final_catalog.append(temp_list)
    return final_catalog
