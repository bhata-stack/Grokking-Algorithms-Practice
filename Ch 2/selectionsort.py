def find_min(arr):
    min = arr[0]
    min_ind = 0
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
            min_ind = i
    return min_ind


def select_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        ind = find_min(arr)
        sorted_arr.append(arr.pop(ind))
    return sorted_arr

if __name__ == "__main__":
    print(select_sort([4, 14, 59, 40, 13, 1, 4, 5, 2]))
