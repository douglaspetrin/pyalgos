""" Insertion Sort """

def sort(array):
    for position in range(len(array)):
        while position > 0:
            if array[position - 1] > array[position]:
                array[position], array[position - 1] = array[position - 1], array[position]
            position -= 1


def sortB(arrayB):
    for position in range(len(arrayB)):
        current_element = arrayB[position]

        while position > 0 and arrayB[position - 1] > current_element:
                arrayB[position] = arrayB[position - 1]
                position -= 1

        arrayB[position] = current_element

array = [8, 7, 5, 3, 1, 2, 9, 6, 4]
arrayB = [8, 7, 5, 3, 1, 2, 9, 6, 4]

sort(array)
sortB(arrayB)
print(array)
print(arrayB)

