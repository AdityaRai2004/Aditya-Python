def get_possible_sums(list1, list2):
    return [x+y for x in list1 for y in list2]

list1 = [1,2,3,4]
list2 = [5,6]
print(get_possible_sums(list1,list2))                                                                                          