
test_input_1 = [2, 4, 12, 3, 4, 5, 6, 23, 7, 17, 22, 20, 11, 31]


def merge(left, right):
    
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


def merge_sort(list):
    
    if len(list) == 1:
        return list
        
    mid = int(len(list) / 2)
    left = merge_sort(list[0:mid])
    right = merge_sort(list[mid:])
    return merge(left, right)


if __name__ == "__main__":

    sorted_test_input_1 = merge_sort(test_input_1)
    print(sorted_test_input_1)