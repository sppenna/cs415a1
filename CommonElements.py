'''
input: two lists of any size and one empty list
Return: two lists are checked and common elements from the list are appended to output list
'''
def comElems(list1, list2, output):
    for number in list1:
        if number in list2:
            output.append(number)
    
list1 = [3, 4, 424, 23, 515, 7, 88, 45, 46]
list2 = [4, 4334, 6626, 23, 231515, 463, 42141, 231315, 7477, 234, 45]
output = list()
comElems(list1, list2, output)
print(output)


