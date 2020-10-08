# Cracking the code q 1.1 Is Unique


def is_unique(input_string):
    """
    Return True if all characters in string are unique,
    otherwise False, using bit vector
    """
    
    if len(input_string) > 26:
        return False

    input_string = input_string.lower()
    ascii_shift = ord('a')

    bit_vector = 0
    for char in input_string:
        ord_char = ord(char) - ascii_shift
        if 2 ** ord_char & bit_vector == 2 ** ord_char:
            return False
        bit_vector = 2 ** ord_char | bit_vector
    return True

if __name__ == "__main__":
    """
    TESTING
    """

    assert is_unique('abcdefghijklmn')
    assert not is_unique('abcddefg')
