import heapq

graph = {
    0: [(1,2),(3,6)],
    1: [(0,2),(2,3),(3,8),(4,5)],
    2: [(1,3),(4,7)],
    3: [(0,6),(1,8)],
    4: [(1,5),(2,7)]
}

def prim(graph,start):
    visited=set()
    pq=[(0,start)]
    mst=[]

    while pq:
        weight,node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        mst.append((node,weight))

        for neighbor,w in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq,(w,neighbor))

    return mst

print(prim(graph,0))