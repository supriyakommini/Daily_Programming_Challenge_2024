def sortColors(arr):
    low, mid, high = 0, 0, len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1

# Test Cases
print("Test Case 1:", end=" ")
arr1 = [0, 1, 2, 1, 0, 2, 1, 0]
sortColors(arr1)
print(arr1)  # Output: [0, 0, 0, 1, 1, 1, 2, 2]

print("Test Case 2:", end=" ")
arr2 = [2, 2, 2, 2]
sortColors(arr2)
print(arr2)  # Output: [2, 2, 2, 2]

print("Test Case 3:", end=" ")
arr3 = [0, 0, 0, 0]
sortColors(arr3)
print(arr3)  # Output: [0, 0, 0, 0]

print("Test Case 4:", end=" ")
arr4 = [1, 1, 1, 1]
sortColors(arr4)
print(arr4)  # Output: [1, 1, 1, 1]

print("Test Case 5:", end=" ")
arr5 = [2, 0, 1]
sortColors(arr5)
print(arr5)  # Output: [0, 1, 2]

print("Test Case 6:", end=" ")
arr6 = []
sortColors(arr6)
print(arr6)  # Output: []
