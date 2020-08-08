#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
 
// Function to find minimum of two elements
int min(int x, int y) { return (x < y) ? x: y; }
 
// Find minimum jumps required to reach the destination
int findMinJumps(int arr[], int i, int n, int lookup[])
{
    // base case: destination is reached
    if (i == n - 1)
        return 0;
 
    // base case: array index out of bound or destination is
    // unreachable from source
    if (i >= n || arr[i] == 0)
        return INT_MAX;
 
    // if the sub-problem is seen before
    if (lookup[i] != 0)
        return lookup[i];
 
    // find the minimum jumps required to reach the destination by considering
    // the minimum of all elements reachable from arr[i]
    int min_jumps = INT_MAX;
    for (int j = i + 1; j <= i + arr[i]; j++)
    {
        int cost = findMinJumps(arr, j, n, lookup);
        if (cost != INT_MAX)
            min_jumps = min(min_jumps, cost + 1);
    }
 
    // save sub-problem solution and return minimum jumps required
    return (lookup[i] = min_jumps);
}
 
// main function
int main(void)
{
    int arr[] = { 1, 3, 6, 1, 0, 9 };
    int n = sizeof(arr) / sizeof(arr[0]);
 
    // create an auxiliary array for storing solution to the sub-problems and
    // initialize it with 0
    int lookup[n];
    memset(lookup, 0, n * sizeof(int));
 
    printf("Minimum jumps required to reach the destination are %d\n",
        findMinJumps(arr, 0, n, lookup));
 
    return 0;
}