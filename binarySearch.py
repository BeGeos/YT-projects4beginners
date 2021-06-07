# Binary Search

class Item:

    def __init__(self, num, idx):
        self.num = num
        self.idx = idx


class Collection:

    def __init__(self, array):
        self.items = [Item(n, idx) for idx, n in enumerate(array)]


def binary_search_recursive(n, array):
    # Base case
    if not array:
        return None

    middle = len(array) // 2
    if array[middle] == n:
        return n
    if array[middle] > n:
        # go left
        return binary_search_recursive(n, array[:middle])
    if array[middle] < n:
        # go right
        return binary_search_recursive(n, array[middle + 1:])


# For Collection class
def binary_search_recursive_collection(n, array):
    # Base case
    if not array:
        return None

    middle = len(array) // 2
    if array[middle].num == n:
        return array[middle].idx
    if array[middle].num > n:
        # go left
        return binary_search_recursive_collection(n, array[:middle])
    if array[middle].num < n:
        # go right
        return binary_search_recursive_collection(n, array[middle + 1:])


def binary_search_iterative(n, array):
    while len(array) > 0:
        middle = len(array) // 2

        if array[middle] == n:
            return n
        if array[middle] > n:
            array = array[:middle]
            continue
        if array[middle] < n:
            array = array[middle + 1:]
            continue
    return None


def is_in_array_recursive(n, array):
    return binary_search_recursive(n, array) is not None


def is_in_array_iterative(n, array):
    return binary_search_iterative(n, array) is not None


input_list = [1, 4, 3, 7, 6, 10, 13, 11, 16]
# Sorting the array
input_list.sort()

collection = Collection(input_list)
print(input_list)


print(binary_search_recursive_collection(10, collection.items))
# print(is_in_array_recursive(7, collection.items))
# print(is_in_array_iterative(10, input_list))


# Find index with binary search
def binary_search_recursive_idx(n, array, start, end):
    # Base case
    if start <= end:

        middle = start + (end - start) // 2

        if array[middle] == n:
            return middle
        elif array[middle] < n:
            # print("Going Right!")
            return binary_search_recursive_idx(n, array, middle + 1, end)
        else:
            # print("Going Left!")
            return binary_search_recursive_idx(n, array, start, middle - 1)

    else:
        return - 1


# print(binary_search_recursive_idx(10, input_list, 0, len(input_list) - 1))
