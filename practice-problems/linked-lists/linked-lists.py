# Creating a linked lists
def create_node(data, next_node=None): 
    return {
        "data": data,
        "next": next_node
    }

# Append function
def append(head, data):
    if head is None: # If the list is empty
        return create_node(data) # Create [data] -> None
    else:
        current = head # Current -> [data] -> None
        while current['next'] is not None:
            current = current['next'] # Move to the next node
        current['next'] = create_node(data) # Current -> [data] -> [data] -> None
        return head 

# Check if the list is empty
def is_empty(head):
    return head is None # If head is None, the list is empty

# Size function
def size_of_linked_list(head):
    count = 0
    current = head 
    while current is not None:
        count += 1
        current = current['next'] 
    return count

# Search function
def search(head, target):
    current = head 
    while current is not None:
        if current['data'] == target: # If the current node's data is the target
            return True
        current = current['next']
    return False

# Push Front
def push_front(head, data):
    return create_node(data, head)

# Pop Front
def pop_front(head):
    if head is None:
        return None
    else:
        head = head['next'] # Move the head to the next node
        return head

# Push Back
def push_back(head, data):
    return append(head, data)

# Pop Back
def pop_back(head):
    if head is None:
        return None
    else:
        current = head
        while current['next']['next'] is not None: # While the next node's next node is not None
            current = current['next']
        current['next'] = None # Set the next node to None
        return head

# Get the front node
def get_front(head):
    return head['data'] # Return the data of the head node

# Get the back node
def get_back(head):
    current = head
    while current['next'] is not None: 
        current = current['next'] 
    return current['data'] # Return the data of the last node

# Insert at index
def insert_at_index(head, index, data):
    if index == 0: 
        return push_front(head, data) 
    else:
        current = head
        for _ in range(index - 1): # Move to the node before the index
            if current is None:
                return head
            current = current['next'] 
        if current is None:
            return head
        current['next'] = create_node(data, current['next']) # Insert the new node
        return head

# Remove at index
def remove_at_index(head, index):
    if index == 0:
        return pop_front(head)
    else:
        current = head
        for _ in range(index - 1): 
            if current is None:
                return head
            current = current['next']
        if current is None or current['next'] is None: 
            return head
        current['next'] = current['next']['next'] 
        return head

# Value(n) from the end(n)
def nth_from_end(head, n):
    current = head
    for _ in range(size_of_linked_list(head) - n): # Move to the node before the nth node from the end
        current = current['next']
    return current['data'] # Return the data of the nth node from the end

# Reverse the linked list
def reverse_linked_list(head):
    prev = None 
    current = head
    while current is not None:
        next_node = current['next'] # Store the next node
        current['next'] = prev # Reverse the link  
        prev = current # Move the prev node to the current node
        current = next_node # Move the current node to the next node
    return prev # Return the new head node

# Remove value
def remove_value(head, value):
    if head is None:
        return None
    while head['data'] == value: # If the head node's data is the value
        head = head['next'] # Move the head to the next node
        if head is None:
            return None
    current = head
    while current['next'] is not None: 
        if current['next']['data'] == value: # If the next node's data is the value
            current['next'] = current['next']['next'] # Remove the next node by skipping it 
        else:
            current = current['next'] 
    return head

# Print list function
def print_list(head):
    current = head
    while current is not None:
        print(current['data'] , end = ' -> ' if current['next'] is not None else ' -> None')
        current = current['next']


def main():
    head = None
    
    for i in range(10):
        head = append(head, i)

    print_list(head)
    print()

    print("Size of the list: ", size_of_linked_list(head))
    print("Is the list empty? ", is_empty(head))
    print("Is 5 in the list? ", search(head, 5))
    
    print()
    print("Push Front:")
    head = push_front(head, 11)
    print_list(head)

    print()
    print("Pop Front:")
    head = pop_front(head)   
    print_list(head)

    print()
    print("Push Back:")
    push_back(head, 12)
    print_list(head)

    print()
    print("Pop Back:")
    pop_back(head)
    print_list(head)

    
    print("\n \nGet Front:", get_front(head))
    print("Get Back:", get_back(head))

    print()
    print("Insert at index:")
    insert_at_index(head, 3, "inserted")
    print_list(head)

    print()
    print("Remove at index:")
    remove_at_index(head, 3)
    print_list(head)

    print("\n \n(n)th from end:", nth_from_end(head, 3))

    print()
    print("Reverse linked list:")
    head = reverse_linked_list(head)
    print_list(head)

    print()
    print("Remove value:")
    remove_value(head, 5)
    print_list(head)
    
    
if __name__ == "__main__":
    main()