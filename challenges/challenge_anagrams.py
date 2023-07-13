def is_anagram(first_string, second_string):
    array = [list(first_string.lower()), list(second_string.lower())]

    for index in range(len(array)):
        array[index] = merge_sort(array[index])
        array[index] = "".join(array[index])

    if len(array[0]) == 0 or first_string is None:
        return ("", array[1], False)
    elif len(array[1]) == 0 or second_string is None:
        return (array[0], "", False)
    else:
        return (array[0], array[1], array[0] == array[1])


def merge_sort(string):
    if len(string) <= 1:
        return string

    mid = len(string) // 2
    left = string[:mid]
    right = string[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result_sort = []
    # left = 0
    # right = 0
    while left and right:
        if left[0] <= right[0]:
            result_sort.append(left.pop(0))
        else:
            result_sort.append(right.pop(0))
    result_sort.extend(left)
    result_sort.extend(right)
    return result_sort


# print(is_anagram('amor', 'roma'))
