def hyperloop(city1, city2, tunnels):
    adjacency = {}
    cost = {}
    node_list = []
    for path in tunnels:
        source,destination,weight = path
        weight = int(weight)
        if source in adjacency:
            adjacency[source].append(destination)
            cost[source].append(weight)
        else:
            adjacency[source] = [destination]
            cost[source] = [weight]
        node_list.append(source)
        node_list.append(destination)        
    node_list = list(set(node_list))
    travel_cost = {}
    for node in node_list:
        travel_cost[node] = 10000
    travel_cost[city1] = 0
    queue = []
    queue.append(city1)
    while len(queue)>0:
        top = queue.pop()
        if top in adjacency:
            connected_nodes = adjacency[top]
            connected_costs = cost[top]
            for i in range(len(connected_nodes)):
                node = connected_nodes[i]
                current_cost = connected_costs[i]
                if travel_cost[top]+current_cost<travel_cost[node]:
                    travel_cost[node]=travel_cost[top]+current_cost
                    queue.append(node)
    return travel_cost[city2]
