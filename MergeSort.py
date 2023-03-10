# creating merge function (helper function) for merge sort
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