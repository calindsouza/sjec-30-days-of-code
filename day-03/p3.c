#include <stdio.h>
int main(){
    int n,i,sum=0;
    float avg;
    printf("enter number of inputs\n ");
    scanf(" %d",&n );
    int a[n];
    printf("enter n numbers");
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++)
    {
        sum=sum+a[i];
    }
    avg=sum/n;
    for(i=0;i<n;i++)
    {
        if(avg<=a[i])
        {
            printf("%d ", a[i]);
        }
    }
}