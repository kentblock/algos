# Cracking the code 1.4 Palindrome Permutation

# Assumptions
# - String is assumed to contain only ascii chars

# Strategy
# Use ascii val of char and array of len 128 to keep track of how many times
# we have seen each character then iterate over it and see if it is a palindrome

def palindrome_permutation(input_str):
    """
    Check if the string is a permutation of a palindrome
    (Ignore spaces)
    """
    hash_map = [0 for _ in range(128)]
    char_length = 0
    for char in input_str:
        if ord(char) != 32:
            hash_map[ord(char)] += 1
            char_length += 1

    middle_value = True if char_length % 2 == 1 else False
    
    val = 0
    for item in hash_map:
        if item != 0:
            val = item
            break

    for item in hash_map:
        if item != val and item != 0:
            if not middle_value:
                return False
            middle_value = False 

    return True


if __name__ == "__main__":
    """
    Testing
    """
    assert palindrome_permutation('tact coa')
    assert not palindrome_permutation('tacdt coa')
    assert palindrome_permutation('big dgib')