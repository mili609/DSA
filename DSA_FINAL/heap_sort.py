import heapq

arr=[12,3,17,8,34]

heapq.heapify(arr)

sorted_arr=[]
while arr:
    sorted_arr.append(heapq.heappop(arr))

print("Sorted array:",sorted_arr)
