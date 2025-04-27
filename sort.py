arr1 = [64, -25, 12, 0, 22, 11]
def selection_sort_iterative(arr):
    n = len(arr)

    for i in range(n - 1):  # Iterate through the array
        min_index = i
        for j in range(i + 1, n):  # Find the minimum element in the remaining array
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap the found minimum element
        print("After", i+1,  "Pass:", arr)

selection_sort_iterative(arr1)
print("Selection Sort (Iterative):", arr1)
