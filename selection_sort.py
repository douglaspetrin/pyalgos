""" Sort Selection"""


def sort(array):
    for index in range(0, len(array)):
        index_min = index
        for right in range(index + 1, len(array)):
            if array[right] < array[index_min]:
                index_min = right
            array[index], array[index_min] = array[index_min], array[index]


array = [8, 7, 5, 3, 1, 2, 9, 6, 4]
sort(array)
print(array)