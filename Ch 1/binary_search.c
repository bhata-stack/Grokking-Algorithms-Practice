#include <stdio.h>

int binary_search(int in_array[], int size, int x) {
    int low = 0, high = size-1;
    while (low <= high) {
        int midpoint = (low + high) / 2;

        if (in_array[midpoint] == x) {
            return midpoint;
        } else if (in_array[midpoint] < x) {
            low = midpoint + 1;
        } else {
            high = midpoint - 1;
        }
    }
    return -1;
}


void main() {
    int test_array[] = {3, 4, 5, 6, 7, 8, 9};
    int n = sizeof(test_array) / sizeof(*test_array);
    int solution = binary_search(test_array, n, 4);
    printf("\nThe index is %d, which corresponds to %d\n", solution, test_array[solution]);

    solution = binary_search(test_array, n, 8);
    printf("The index is %d, which corresponds to %d", solution, test_array[solution]);
} 