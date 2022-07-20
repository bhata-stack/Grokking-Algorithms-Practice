def binary_search(input_array, item):
    '''
    Takes a sorted list and a variable as inputs and
    returns the index of the item if it is in the array,
    otherwise it returns -1.

    Parameters:
    input_array (list): A sorted list to be searched.
    item (any): The variable to be searched for.

    Examples:
    >>> binary_search()

    '''

    lower = 0
    higher = len(input_array)
    if input_array[lower] > item or input_array[higher-1] < item:
        return -1
    
    while (higher - lower) > 1:
        search_index = (lower + higher) // 2
        if input_array[search_index] == item:
            return search_index
        elif input_array[search_index] > item:
            higher = search_index
        else:
            lower = search_index
    
    if input_array[lower] == item:
        return lower
    else:
        return -1

if __name__ == "__main__":
    print(binary_search([1, 3, 5, 7, 9, 11, 13], 9))
    print(binary_search([1, 3, 5, 7, 9, 11, 13], 4))
    print(binary_search([1, 3, 5, 7, 9, 11, 13], 13))
    print(binary_search([1, 3, 5, 7, 9, 11, 13], 15))