#include<stdio.h>
#include<string.h>
int main()
{
    char str[] = "Technical\0\Bits\0";
    printf("%s\n", str);
    return 0;
}
