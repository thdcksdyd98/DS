# creating merge function (helper function) for merge sort
# only works at sorted list
def merge(list1, list2):
    combined = []
    i = j = 0
    while i < len(list1) and j < len(list2): # as long as both lists have items
        # if one of list became empty, while loops are going to be broken
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    # appending leftover elements to the combined list
    # in this case, one of list is empty
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    
    return combined


# mergesort
# 1. Breaks lists in half
# 2. Base case: when len(the_list) is 1
# 3. Uses merge() to put lists together

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list)/2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])
    # remember, when the function called return, the top of the call stack would pop.
    # -> since merge() has return and we use return merge(left, right), should pop the call stack twice

    return merge(left, right)

# space complexity = O(n)
# time complexity = O(nlogn)















