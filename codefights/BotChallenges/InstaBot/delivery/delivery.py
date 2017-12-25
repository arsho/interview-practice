def delivery(order, shoppers):
    ar = []
    for shop in shoppers:
        x = order[1]+order[2]
        calc = ((shop[0]+order[0])/shop[1])+shop[2]
        ar.append(order[1]<=calc<=x)
    return ar
