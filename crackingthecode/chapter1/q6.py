# Cracking the code question 1.6 String Compression


def str_compression(input_str):
    """
    Return compressed string if it is shorter than original otherwise
    return the original string
    """
    reps = 1
    compress_str = ""
    for i in range(len(input_str)):
        if i is len(input_str) - 1:
            compress_str = f"{compress_str}{input_str[i]}{reps}"
            break
        if input_str[i + 1] != input_str[i]:
            compress_str = f"{compress_str}{input_str[i]}{reps}"
            reps = 1
        else:
            reps += 1
    
    if len(compress_str) < len(input_str):
        return compress_str

    return input_str


if __name__ == "__main__":
    """
    Testing
    """
    assert str_compression("aabccccaaa") == "a2b1c4a3"
    assert str_compression("abcd") == "abcd"