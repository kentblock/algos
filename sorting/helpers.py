import random

def generate_random_list(length, max):
    """
    Generates a list of length, containing random values
    from 0 to max
    """
    random_list = []
    for _ in range(length):
        random_list.append(random.randint(0, max))

    return random_list

def is_sorted(sorted_list):
    """
    Checks if list is sorted
    """
    for i in range(len(sorted_list) - 1):
        if sorted_list[i] > sorted_list[i + 1]:
            print(sorted_list[i])
            return False
    return True