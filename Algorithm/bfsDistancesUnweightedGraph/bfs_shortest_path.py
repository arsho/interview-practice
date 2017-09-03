adjacency = {}
node_list = []
with open("graph.txt","r") as fp:
    lines = fp.readlines()
    for line in lines:
        line = line.strip()
        if line=="":
            continue
        source,destination = line.split(" ")
        if source not in node_list:
            node_list.append(source)
        if destination not in node_list:
            node_list.append(destination)
        if source in adjacency:
            adjacency[source].append(destination)
        else:
            adjacency[source]=[destination]
    # Calculating distance from source Sylhet only
    distance = {}
    for node in node_list:
        distance[node] = -1
    queue = []
    queue.append('syl')
    distance['syl'] = 0
    while len(queue)>0:
        top = queue.pop()
        if top in adjacency:
            connected_nodes = adjacency[top]
            for node in connected_nodes:
                if distance[node] == -1 or distance[node]>distance[top]+1:
                    distance[node] = distance[top]+1
                    queue.append(node)
    for key in distance:
        print(key,distance[key])

