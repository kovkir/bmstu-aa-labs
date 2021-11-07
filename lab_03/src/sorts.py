from input_array import input_arr


def sort(method):
    arr = input_arr()
    print("\n", method(arr, len(arr)))


def bubble_sort(arr, n):
    n -= 1

    for i in range(n):
        for j in range(n - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def select_sort(arr, n):

    for i in range(n - 1):
        min_j = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_j]:
                min_j = j

        if min_j != i:
            arr[i], arr[min_j] = arr[min_j], arr[i]

    return arr


def insertion_sort(arr, n):
    
    for i in range(1, n):
        j = i - 1
        tmp = arr[i]

        while j >= 0 and arr[j] > tmp:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = tmp

    return arr
