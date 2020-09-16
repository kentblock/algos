# Problem 1 
# Count the number of ways to assign a unique cap to every person
# My Implementation of the solution described here: 
# https://www.geeksforgeeks.org/bitmasking-and-dynamic-programming-set-1-count-ways-to-assign-unique-cap-to-every-person/

def get_hats_per_person(hat_collections):
    """
    Helper returns an array where i represents a hat 
    and h_to_p[i] is the people that can wear hat i
    """
    h_to_p = [[] for _ in range(NUM_HATS + 1)]
    for i in range(len(hat_collections)):
        for hat in hat_collections[i]:
            h_to_p[hat].append(i)
    return h_to_p

def count_hat_arrangements(mask, hat_no):
    """
    Dynamic programming routine to recursively find the number 
    of hat arrangements
    """
    if mask == all_mask:
        return 1

    if hat_no > NUM_HATS:
        return 0

    if d[mask][hat_no] != -1:
        return d[mask][hat_no]

    ways = count_hat_arrangements(mask, hat_no + 1)
    for person in hats_to_person[hat_no]:
        if not (mask & 2 ** person):
            ways += count_hat_arrangements(mask | 2 ** person, hat_no + 1)

    d[mask][hat_no] = ways

    return ways

if __name__ == "__main__":
    """
    TESTING
    """
    NUM_PEOPLE = 3
    NUM_HATS = 100
    hat_collections = [[5, 100, 1], [2], [5, 100]]
    hats_to_person = get_hats_per_person(hat_collections)
    d = [[-1 for _ in range(NUM_HATS + 1)] for _ in range(NUM_PEOPLE ** 2)]
    all_mask = 2 ** NUM_PEOPLE - 1
    count_hat_arrangements(0, 1)