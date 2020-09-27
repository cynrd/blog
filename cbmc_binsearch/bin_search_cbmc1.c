#include <stdio.h>
#include <stdlib.h>

int binary_search(int arr[], int size, int target) {
    int low = 0;
    int high = size - 1;
    int mid;
    while (low <= high) {
        mid = (low + high)/2;
        if (arr[mid] == target) {
            return mid;
        }
        if (arr[mid] < target) {
            low = mid + 1;
        }
        if (arr[mid] > target) {
            high = mid - 1;
        }
    }
    return -1;
}

/*
void read_int(int *n) {
  int result = scanf("%d", n);
  if (result == EOF) {
    exit(-1);
  }
}

void read_array(int *a, int n) {
  for (int i = 0; i < n; i++) {
    read_int(&a[i]);
  }
}
*/

int main() {
  int n;
  //read_int(&n);
  if (n <= 0) return 1;
  int a[n];
  //read_array(a, n);
  int x;
  //read_int(&x);
  int result = binary_search(a, n, x);
  printf("result = %d\n", result);
  return 0;
}

