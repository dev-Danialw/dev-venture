def array_practice():

    myArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("Array: ", myArray)

    print("Array Length/Size: ", len(myArray)) # Length of the array

    print("Capacity: ", myArray.__sizeof__())   # Capacity of the array

    print("Is the array empty: ", myArray == []) # Check if the array is empty

    print("Element at (n)th index: ", myArray[5]) # at(index) element of the array at the given index

    myArray.append(11)
    print("Pushing an element to the end of the array: ", myArray) # Pushing an element to the end of the array

    myArray.insert(0, 0)
    print("Inserting an element at the start of the array: ", myArray) # Inserting an element at the start of the array

    myArray.pop()
    print("Popping an element from the end of the array: ", myArray) # Popping an element from the end of the array

    myArray.__delitem__(0)
    print("Deleting an element at the start of the array: ", myArray) # Deleting an element at the start of the array

    myArray.remove(4)
    print("Removing an element from the array: ", myArray) # Removing an element from the array

    print("Finding an element in the array: ", myArray.__contains__(5),
    myArray.__contains__(4)) # Finding an element in the array

    myArray.insert(5, 13)
    print("Replacing an element in the array: ", myArray) # Replacing an element in the array

    print("Reversing the array: ", myArray[::-1]) # Reversing the array

    print("Sorting the array: ", sorted(myArray)) # Sorting the array

    myArray.clear()
    print("Array after clearing: ", myArray) # Clearing the array
    

def main():
    array_practice()

if __name__ == "__main__":
    main()