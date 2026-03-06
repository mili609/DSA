# Kruskal Algorithm

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    elif rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    else:
        parent[rootY] = rootX
        rank[rootX] += 1


def kruskal(vertices, edges):
    edges.sort(key=lambda x: x[2])

    parent = [i for i in range(vertices)]
    rank = [0]*vertices

    mst = []

    for u,v,w in edges:
        if find(parent,u) != find(parent,v):
            mst.append((u,v,w))
            union(parent,rank,u,v)

    return mst


edges = [
    (0,1,10),
    (0,2,6),
    (0,3,5),
    (1,3,15),
    (2,3,4)
]

print("MST:", kruskal(4, edges))