#include <iostream>
using namespace std;

int main()
{
    // Array declaration and initialization
    int arr[5] = {4, 12, 7, 15, 9};
    // Iterate over the array
    for(int idx=0; idx<5; idx++)
    {
        // Print out each element in a new line
        cout << arr[idx] << endl;
    }
    return 0;


// Multi D

#include <iostream>
using namespace std;

int main()
{
    // Array declaration and initialization
    int arr[3][5] = {{5, 12, 17, 9, 3}, {13, 4, 8, 14, 1}, {9, 6, 3, 7, 21}};
    // Iterate over the array
    for(int i=0; i<3; i++)
    {
        for(int j=0; j<5; j++)
        {
            // Print out each element
            cout << arr[i][j];
        }
        // Print new line character after the row is printed in above loop
        cout << endl;
    }
    return 0;
}}
