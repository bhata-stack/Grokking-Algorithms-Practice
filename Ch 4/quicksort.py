import numpy as np

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        point = arr[0]
        sub_arr = [i for i in arr[1:] if i < point]
        sup_arr = [i for i in arr[1:] if i >= point]
        return quicksort(sub_arr) + [point] + quicksort(sup_arr)

if __name__ == "__main__":
    unsorted_arr = np.random.randint(-10, 10, 20)
    print(unsorted_arr)
    print(quicksort(unsorted_arr))