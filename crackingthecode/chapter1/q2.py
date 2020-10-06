# Cracking the code q 1.2 Check Permutation

def check_permutation(str1, str2):
    """
    Check if two strings are a permutations of one 
    another
    """
    if len(str1) != len(str2):
        return False
    str1_sorted = sorted(str1)
    str2_sorted = sorted(str2)
    for i in range(len(str1_sorted)):
        if str1_sorted[i] != str2_sorted[i]:
            return False
    return True

if __name__ == "__main__":
    """
    Testing
    """
    assert check_permutation('abc', 'acb')
    assert check_permutation('xabgfh', 'hfgbax')
    assert not check_permutation('xabgfhy', 'hfgbaxt')