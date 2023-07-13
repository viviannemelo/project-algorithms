def is_anagram(first_string, second_string):
    str1 = first_string.lower()
    str2 = second_string.lower()
    sorted_str1 = sort(str1)
    sorted_str2 = sort(str2)
    if len(sorted_str1) | len(sorted_str2) == 0:
        return (first_string, second_string, False)
    result_str1 = ''.join(sorted_str1)
    result_str2 = ''.join(sorted_str2)
    return (result_str1, result_str2, result_str1 == result_str2)


def sort(string):
    if len(string) < 2:
        return string
    else:
        mid = string.pop(0)
        left = []
        right = []
        for i in string:
            right.append(i) if i <= mid else left.append(i)
        return sort(right) + [mid] + sort(left)


# print(is_anagram('ave', 'eva'))
