def return_last_element(items):
    return items[-1]
list = [(2,6),(3,1),(4,9),(3,2),(1,3)]
list1 = sorted(list,key=return_last_element)
print(list)