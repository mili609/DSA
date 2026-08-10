# Build Segment Tree for Range Sum

def build(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        build(arr, tree, 2*node, start, mid)
        build(arr, tree, 2*node+1, mid+1, end)
        tree[node] = tree[2*node] + tree[2*node+1]

arr = [1, 3, 5, 7, 9, 11]
n = len(arr)
tree = [0]*(4*n)

build(arr, tree, 1, 0, n-1)

print("Segment Tree:", tree)