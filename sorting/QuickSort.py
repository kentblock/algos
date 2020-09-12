
test_input_1 = [2, 4, 12, 3, 4, 5, 6, 23, 7, 17, 22, 20, 11, 31]
test_input_2 = [4, 3, 1, 7, 2]


def swap(arr, low, high):
    low_val = arr[low]
    arr[low] = arr[high]
    arr[high] = low_val

def partition(arr, low, high):
    pivot_pos = high
    pivot = arr[high]
    high -= 1
    while True:
        while arr[high] > pivot:
            high -= 1

        while arr[low] < pivot:
            low += 1
        
        
        if low >= high:
            break
        else:
            swap(arr, low, high)

    print(low)
    print(high)
    swap(arr, high, pivot_pos)

    return high


def quick_sort(arr, low, high):

    if low < high:
        pivot_pos = partition(arr, low, high)
        quick_sort(arr, low, pivot_pos - 1)
        quick_sort(arr, pivot_pos + 1, high)
    
if __name__ == "__main__":
    quick_sort(test_input_1, 0, len(test_input_1) - 1)
    quick_sort(test_input_2, 0, len(test_input_2) - 1)
    print(test_input_1)
    print(test_input_2)