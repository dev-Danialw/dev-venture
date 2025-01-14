# Implement a queue using a doubly linked list

# Create a node for the doubly linked list
def create_node(data, next_node=None, prev_node=None):
    return {
        "data": data,
        "next": next_node,
        "prev": prev_node
    }

# Enqueue an element to the end of the queue
def enqueue(head, data): 
    if head is None:
        return create_node(data)
    current = head
    while current['next'] is not None:
        current = current['next'] # Traverse to the end of the queue
    current['next'] = create_node(data, None, current) # Set the previous node to the current node in the new node
    return head

# Dequeue an element from the front of the queue
def dequeue(head):
    if head is None:
        return None
    head = head['next'] # Move the head to the next node
    if head is not None:
        head['prev'] = None # Set the previous node of the new head to None
    return head

# Check if the queue is empty
def is_empty(head):
    return head is None

# Implementing queue using fixed sized array

# Create a queue with a fixed size array
def create_queue(size, data, front=0, rear=0):
    return {
        "size": size,
        "data": [data] * size,
        "front": front,
        "rear": rear
    }

# Enqueue an element to the end of the queue
def enqueue_array(queue, data):
    if (queue['rear'] + 1) % queue['size'] == queue['front']: # Check if the queue is full by checking if the next rear index is the front index
        return queue  # Queue is full
    queue['data'][queue['rear']] = data # Add the data to the rear index 
    queue['rear'] = (queue['rear'] + 1) % queue['size'] # Move the rear index to the next index
    return queue

# Dequeue an element from the front of the queue
def dequeue_array(queue):
    if queue['front'] == queue['rear']: # Check if the queue is empty
        return queue  # Queue is empty
    queue['front'] = (queue['front'] + 1) % queue['size'] # Move the front index to the next index
    return queue

# Check if the queue is empty
def is_empty_array(queue):
    return queue['front'] == queue['rear']

# Check if the queue is full
def is_full_array(queue):
    return (queue['rear'] + 1) % queue['size'] == queue['front']



# Testing the queue using doubly linked list
def print_queue(head):
    current = head
    while current is not None:
        print(current['data'], end=" ")
        current = current['next']
    print()

print("Queue using a doubly linked list:")
head = None

print("Initial queue:")
print_queue(head)

print("\nEnqueuing elements:")
for i in range(5):
    head = enqueue(head, i)
    print(f"After enqueue {i}:")
    print_queue(head)

print("\nDequeuing elements:")
for i in range(5):
    head = dequeue(head)
    print(f"After dequeue {i}:")
    print_queue(head)

# Testing the queue using fixed size array
def print_queue_array(queue):
    if queue['front'] == queue['rear']:
        print("Queue is empty")
        return
    current = queue['front']
    while current != queue['rear']:
        print(queue['data'][current], end=" ")
        current = (current + 1) % queue['size']
    print()

print("Queue using a fixed size array:")
size = 5
queue = create_queue(size, 0)

print("Initial queue:")
print_queue_array(queue)

print("\nEnqueuing elements:")
for i in range(size):
    queue = enqueue_array(queue, i)
    print(f"After enqueue {i}:")
    print_queue_array(queue)

print("\nDequeuing elements:")
for i in range(size):
    queue = dequeue_array(queue)
    print(f"After dequeue {i}:")
    print_queue_array(queue)
