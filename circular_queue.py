size = 5
queue = [None]*size
front = rear = -1

def enqueue(data):
    global front, rear
    if (rear + 1) % size == front:
        print("Queue is full")
    elif front == -1:
        front = rear = 0
        queue[rear] = data
    else:
        rear = (rear + 1) % size
        queue[rear] = data

def display():
    if front == -1:
        print("Queue empty")
        return
    i = front
    while True:
        print(queue[i], end=" ")
        if i == rear:
            break
        i = (i + 1) % size
    print()

enqueue(10)
enqueue(20)
enqueue(30)
display()
