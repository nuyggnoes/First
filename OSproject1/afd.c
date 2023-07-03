#include <stdio.h>
#include <stdbool.h>

bool check_SubsetSum(int arr[], int n, int sum, bool subset[])
{
    bool table[n + 1][sum + 1];

    for (int i = 0; i <= n; i++)
        table[i][0] = true;

    for (int i = 1; i <= sum; i++)
        table[0][i] = false;

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= sum; j++)
        {
            if (j < arr[i - 1])
                table[i][j] = table[i - 1][j];
            else
                table[i][j] = table[i - 1][j] || table[i - 1][j - arr[i - 1]];
        }
    }
    printf("완성된 table (true = 1, false = 0)\n");
    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= sum; j++)
        {
            if (table[i][j])
                printf("1 ");
            else
            {
                printf("0 ");
            }
        }
        printf("\n");
    }
    printf("\n");
    if (!table[n][sum])
        return false;

    int i = n, j = sum;
    while (i > 0 && j > 0)
    {
        if (table[i - 1][j])
        {
            i--;
        }
        else
        {
            subset[i - 1] = true;
            j -= arr[i - 1];
            i--;
        }
    }

    return true;
}

void print_Subset(int arr[], bool subset[], int n)
{
    for (int i = 0; i < n; i++)
    {
        if (subset[i])
            printf("%d ", arr[i]);
    }
    printf("\n");
}

int main()
{
    int sum;
    int arr[100];
    int n = 0;
    bool subset[100];
    printf("배열의 크기 n:");
    scanf("%d", &n);
    printf("찾고자 하는 합:");
    scanf("%d", &sum);
    printf("배열의 원소 입력:");

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    printf("\n");

    if (check_SubsetSum(arr, n, sum, subset))
    {
        printf("입력한 합에 해당하는 결과에 대한 배열: ");
        print_Subset(arr, subset, n);
    }
    else
    {
        printf("입력한 합에 해당하는 결과가 배열에 존재하지 않습니다.");
    }

    return 0;
}
