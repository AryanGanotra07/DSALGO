#include<iostream>;
using namespace std;

double findMedianSortedArrays(const vector<int> &a, const vector<int> &b) {
int x = a.size(), y = b.size();
if(x > y)
    return findMedianSortedArrays(b, a);
x = a.size(), y = b.size();

long low = 0, high = x, partitionX, partitionY;
while(low <= high)
{
    partitionX = low + (high-low)/2;
    partitionY = (x + y + 1)/2 - partitionX;
    
    long maxLeftX = (partitionX == 0) ? INT_MIN : a[partitionX - 1];
    long minRightX = (partitionX == x) ? INT_MAX : a[partitionX];
    
    long maxLeftY = (partitionY == 0) ? INT_MIN : b[partitionY - 1];
    long minRightY = (partitionY == y) ? INT_MAX : b[partitionY];
    
    if(maxLeftX <= minRightY and maxLeftY <= minRightX){
        if ((x + y) % 2 == 0)
            return ((double)max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2;
        else
            return (double)max(maxLeftX, maxLeftY);
        }
    else if(maxLeftX > minRightY) { 
        high = partitionX - 1;
    }
    else
    {
        low = partitionX + 1;
    }
}
}