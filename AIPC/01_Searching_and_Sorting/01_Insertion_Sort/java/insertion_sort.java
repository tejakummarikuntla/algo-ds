class InsertionSort
{
    void sort(int arr[])
    {
        int n = arr.length;
        int key = 0;
        int i = 0;
        for(int j=1; j<n; j++)
        {
            key = arr[j];
            i = j-1;

            while(i>0 && arr[i] < key)
            {
                arr[i+1] = arr[i];
                i = i-1;
            }
            arr[i+1] = key;
        }
    }
static void print_arr(int arr[])
{
        int n = arr.length;
        for(int i=0; i<n; i++)
        {
            System.out.println(arr[i] + " ");
        }
}

public static void main(String args[])
    {
        int arr[] = {12, 11, 15, 2, 3, 5};
        InsertionSort ins_obj = new InsertionSort();
        ins_obj.sort(arr);
        print_arr(arr);
    }
}
