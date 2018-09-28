'''
input: two lists of any size and one empty list
Return: two lists are checked and common elements from the list are appended to output list
'''
def comElems(list1, list2, output, count):
    i = 0
    j = 0
    while (i < len(list1) and j < len(list2)):
        count+=1
        if (list1[i] > list2[j]):
            j+=1
        elif (list1[i] < list2[j]):
            i+=1
        else:
            output.append(list1[i])
            i+=1
            j+=1
    return count




