# Quicksort implementation for practice
import helpers

def swap(arr, index1, index2):
    """
    Helper function, swaps two values in place
    """
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp

def partition(arr, low, high):
    """
    Choose pivot, then partition array with values less than pivot to the left,
    and values greater than pivot to the right
    """
    pivot_pos, pivot = high, arr[high]
    high -= 1
    while True:
        while arr[low] < pivot:
            low += 1
        while arr[high] >= pivot and high >= 0:
            high -= 1
        if low > high:
            break
        else:
            swap(arr, low, high)
    swap(arr, low, pivot_pos)
    return low

def quick_sort(arr, low, high):
    """
    If the length of the list to sort is 1 then we are done and do nothing,
    otherwise partion the list and recursively sort on each partition
    """
    if high - low > 0:
        pivot_pos = partition(arr, low, high)
        quick_sort(arr, low, pivot_pos - 1)
        quick_sort(arr, pivot_pos + 1, high)
    
if __name__ == "__main__":
    """
    Testing
    """
    LENGTH = 100
    RANGE = 100
    for _ in range(10):
        arr = helpers.generate_random_list(LENGTH, RANGE)
        quick_sort(arr, 0, len(arr) - 1)
        print(arr)
        assert helpers.is_sorted(arr)