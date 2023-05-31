// BESTOFTWO | Best of Two
// Chef took an examination two times. In the first attempt, he scored X marks while in the second attempt he scored Y marks. 
// According to the rules of the examination, the best score out of the two attempts will be considered as the final score.
// Determine the final score of the Chef.

//Solution
#include <stdio.h>

int main()
{
    int t;
    scanf("%d", &t);
    while (t--)
    {
        int x, y;
        scanf("%d %d", &x, &y);
        if (x >= y)
            printf("%d\n", x);
        else
            printf("%d\n", y);
    }
    return 0;
}
