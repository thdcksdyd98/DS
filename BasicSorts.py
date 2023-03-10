# bubble sort

def bubble_sort(my_list):
    for i in range(len(my_list)-1,0,-1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                tmp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = tmp
    return my_list

# selection sort

def selelction_sort(my_list):
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index: # for the case where min_index is equal to i -> already sorted
            tmp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = tmp
    return my_list

# insertion sort
# always starts from the second element (index = 1)

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        tmp = my_list[i]
        j = i - 1
        while tmp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = tmp
            j -= 1
            
    return my_list
















