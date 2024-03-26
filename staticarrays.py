myArray = [1,3,5,7,8,12]

# for i in range(len(myArray)):
#     print(myArray[i])



# removeMiddle(Specify which array, which index to remove, and how many we're removing)
def removeMiddle(array, i, removal):
    for index in range(i + removal, len(array)):
        array[index - removal] = array[index]
        ##So, if we consider myArray = [1, 3, 5, 7, 8, 12] and the first iteration of the loop:
        ##Before the assignment: myArray = [1, 3, 5, 7, 8, 12]
        ##After the assignment: myArray = [1, 5, 5, 7, 8, 12]
    array = array[:-removal]
    return array
result = removeMiddle(myArray, 1, 1)
print(result)

