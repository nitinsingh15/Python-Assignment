list1 = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
# Trying to Remove duplicate elements by converting list to set and then back to list for Sorting
list2 = list(set(list1))
# Sorting not on the basis of Value but the key here is list1.index
list2.sort(key=list1.index)
print(list2)
