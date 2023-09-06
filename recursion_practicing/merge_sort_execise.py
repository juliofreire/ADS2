


def merge_sorted_lists(list1, list2):

    index1 = 0
    index2 = 0

    merged_list = []
    
    while index1 < len(list1) and index2 < len(list2): 
        if list1[index1] < list2[index2]:
            merged_list.append(list1[index1])
            index1 += 1
        else:
            merged_list.append(list2[index2])
            index2 += 1

    merged_list += list1[index1:]
    merged_list += list2[index2:]

    return merged_list



def merge_sorte(values):

    tam = len(values)
    if tam <2:
        return values
    
    mid = tam//2
    sorted_first_half = merge_sorte(values[:mid])
    sorted_second_half = merge_sorte(values[mid:])
    return merge_sorted_lists(sorted_first_half, sorted_second_half)


ss = merge_sorte([2, 4, 7, 8, 1, 3, 5, 6])
print(ss)