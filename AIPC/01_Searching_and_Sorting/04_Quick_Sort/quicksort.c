/*Program of sorting using quick sort */
 
#include<stdio.h>
#define MAX 100
 
int partition(int arr[], int left, int right)
{
	int temp,i,j,pivot;
 
	i = left+1;
	j = right;
	pivot = arr[left];
 
	while(i <= j)
	{
		while(arr[i] < pivot && i<right)    
			i++;
 
		while(arr[j] > pivot)	
			j--;
 
		if(i < j)
		{
			temp=arr[i];
			arr[i]=arr[j];
			arr[j]=temp;
			i++;
			j--;
		}
		else 
			i++;
	}
	arr[left]=arr[j];
	arr[j]=pivot;
 
	return j;
}/*End of partition()*/
 
void quick_sort(int *arr,int left, int right)
{
	int pivloc;
 
	if(left >= right)
		return;
	pivloc = partition(arr,left, right);
	quick_sort(arr, left, pivloc-1); /*process left sublist*/
	quick_sort(arr, pivloc+1, right);  /*process right sublist*/
}/*End of quick()*/
 
int main()
{
	int arr[MAX],n,i;
	printf("Enter the number of elements : ");
	scanf("%d",&n);
 
	for(i=0;i<n;i++)
	{
		printf("Enter element %d : ",i+1);
		scanf("%d",&arr[i]);
	}
 
	quick_sort(arr, 0, n-1);
 
	printf("Sorted list is :\n");
 
	for( i=0; i<n; i++ )
		printf("%d ",arr[i]);
	printf("\n");
 
}/*End of main() */
 
 