# Disjoint Set (Union Find)

parent = {}

def make_set(n):
    for i in range(n):
        parent[i] = i

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        parent[rootY] = rootX

make_set(5)

union(0,1)
union(1,2)

print(find(0))
print(find(2))