#include <stdio.h>
    struct student
    {
        char *name;
    };
    struct student s;
    struct student fun(void)
    {
        s.name = "Technical";
        printf("%s\n", s.name);
        s.name = "Hub";
        return s;
    }
    int main()
    {
        struct student m = fun();
        printf("%s\n", m.name);
        m.name = "Aditya";
        printf("%s\n", s.name);
    }