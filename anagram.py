def is_anagram_quadratic(s1, s2):
    """O(n**2)"""

    if len(s1) != len(s2):
        is_anagram = False
    
    s2_list = list(s2)

    is_anagram = True
    
    for letter1 in s1:
        for idx, letter2 in enumerate(s2_list):
            if letter1 != letter2:
                is_anagram = False
            else:
                s2_list[idx] = None
                is_anagram = True
                break
        if not is_anagram:
            break

    return is_anagram



print(is_anagram_quadratic('python', 'typhon'))
print(is_anagram_quadratic('python', 'typhoe'))
print(is_anagram_quadratic('javascript', 'scarviapjt'))
print(is_anagram_quadratic('abcd','dcba'))