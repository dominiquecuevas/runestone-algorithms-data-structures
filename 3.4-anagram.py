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

def is_anagram_sort(s1, s2):
    """O(n2**2) for sort method"""
    s1_list = list(s1)
    s2_list = list(s2)
    s1_list.sort()
    s2_list.sort()

    return s1_list == s2_list

def is_anagram(s1, s2):
    """O(n) runtime, but sacrificed space to make dictionaries.
    the dictionary is short, so not sacrificing a lot of computing."""
    s1_dict = {}
    for letter in s1:
        s1_dict[letter] = s1_dict.get(letter, 0) + 1
    
    s2_dict = {}
    for letter in s2:
        s2_dict[letter] = s2_dict.get(letter, 0) + 1

    return s1_dict == s2_dict

print(is_anagram_quadratic('python', 'typhon'))
print(is_anagram_quadratic('python', 'typhoe'))
print(is_anagram_quadratic('javascript', 'scarviapjt'))
print(is_anagram_quadratic('abcd','dcba'))
print()
print(is_anagram_sort('python', 'typhon'))
print(is_anagram_sort('python', 'typhoe'))
print(is_anagram_sort('javascript', 'scarviapjt'))
print(is_anagram_sort('abcd','dcba'))
print()
print(is_anagram('python', 'typhon'))
print(is_anagram('python', 'typhoe'))
print(is_anagram('javascript', 'scarviapjt'))
print(is_anagram('abcd','dcba'))