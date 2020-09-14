# Mergesort implementation for practice
import helpers

def merge(left, right):
    """
    Merge two lists back together in order
    """    
    merged_list = []
    while len(left) is not 0 and len(right) is not 0:
        if left[0] < right[0]:
            merged_list.append(left.pop(0))
        elif left[0] >= right[0]:
            merged_list.append(right.pop(0))
        
    while len(left) is not 0:
        merged_list.append(left.pop(0))

    while len(right) is not 0:
        merged_list.append(right.pop(0))

    return merged_list

def merge_sort(arr):
    """
    If list has length 1 then it is sorted and return,
    otherwise split the list at the middle and recursively sort each half,
    finally merge the two sorted halves back together
    """
    if len(arr) == 1:
        return arr
        
    mid = int(len(arr) / 2)
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

if __name__ == "__main__":
    """
    Testing
    """
    LENGTH = 100
    RANGE = 100
    for _ in range(10):
        arr = helpers.generate_random_list(LENGTH, RANGE)
        sorted_arr = merge_sort(arr)
        assert helpers.is_sorted(sorted_arr)
    