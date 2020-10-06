# Cracking the code q 1.3 URLify
# A bit hacky but it works

def replace_char_at(index, new_char, old_str):
    """
    helper method to replace a char at a certain index
    """
    return f"{old_str[0:index]}{new_char}{old_str[index+1:]}" 

def urlify(input_str):
    """
    replace all spaces in string with %20
    """
    rev_str = input_str[::-1]
    next_open = 0
    seen_letter = False
    for i in range(len(rev_str)):

        if next_open > 0 and next_open == i:
            break

        if rev_str[i] == ' ' and seen_letter:
            rev_str = replace_char_at(next_open, '0', rev_str)
            rev_str = replace_char_at(next_open + 1, '2', rev_str)
            rev_str = replace_char_at(next_open + 2, '%', rev_str)
            next_open += 3

        elif rev_str[i] != ' ':
            if not seen_letter:
                seen_letter = True
            rev_str = replace_char_at(next_open, rev_str[i], rev_str)
            rev_str = replace_char_at(i, ' ', rev_str)
            next_open += 1      

    return rev_str[::-1]


if __name__ == "__main__":
    """
    Testing
    """
    assert urlify('Mr John Smith    ') == 'Mr%20John%20Smith'
