def bfsDistancesUnweightedGraph(matrix, startVertex):
    distance = [-1 for i in range(len(matrix))]
    distance[startVertex] = 0
    queue = []
    queue.append(startVertex)
    while len(queue)>0:
        top = queue.pop()
        edges = matrix[top]
        for i in range(len(edges)):
            if edges[i]==True:
                if distance[i] == -1 or distance[i]>distance[top]+1:
                    distance[i] = distance[top]+1
                    queue.append(i)
    return distance
