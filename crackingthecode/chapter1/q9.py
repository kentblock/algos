# Cracking the code question 1.9 String Rotation

def is_substring(s1, s2):
    """
    Helper checks if s2 is substring of s1,
    very naively
    """
    if len(s1) <= len(s2) and s1 != s2:
        return False
    
    for i in range(len(s1)):
        for j in range(i, len(s1) + 1):
            if s2 == s1[i:j]:
                return True

    return False

def string_rotation(s1, s2):
    """
    Checks if s2 is a rotation of s1 with only one call to is_substring
    """
    # don't really need the call to is sub_string???
    if len(s1) != len(s2):
        return False

    substr_start_index = 0
    matched = False
    j = 0
    for i in range(len(s1)):

        if s1[i] == s2[j]:
            j += 1
            if not matched:
                matched = True
                substr_start_index = i
        else:
            j = 0 
            matched = False

    if not matched:
        return False
    
    return s1[0:substr_start_index] == s2[j:]

if __name__ == "__main__":
    """
    Testing
    """
    assert is_substring("abcdef", "def")
    assert is_substring("abcde", "bcd")
    assert not is_substring("abcd", "bd")

    assert not string_rotation("waterbottlea", "erbottlewatb")
    assert string_rotation("waterbottle", "erbottlewat")