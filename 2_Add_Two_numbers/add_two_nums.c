/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int getNum(struct ListNode *l)
{
    struct ListNode *n;
    n = l;
    int num = 0;
    int x = 1;

    while (n != NULL)
    {
        printf("%d %d %d\n", num, x, n->val);
        num += x * (n->val);
        x *= 10;
        n = n->next;
        printf(">%d\n", num);
    }
    printf("<%d", num);
    return num;
}

struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2)
{
    int sum, index;
    int num1, num2;

    num1 = getNum(l1);
    num2 = getNum(l2);
    sum = num1 + num2;
    printf("\n%d %d %d\n", num1, num2, sum);

    struct ListNode *head = NULL, *p;
    int c = 0;
    if (sum == 0)
    {
        head = malloc(sizeof(struct ListNode));
        head->val = 0;
        head->next = NULL;
        return head;
    }
    for (long i = sum; i > 0; i = i / 10)
    {
        if (c >= 99)
        {
            p->next = NULL;
            return head;
        }
        if (c == 0)
        {
            head = malloc(sizeof(struct ListNode));
            p = head;
        }
        else
        {
            p->next = malloc(sizeof(struct ListNode));
            p = p->next;
        }

        index = i % 10;
        printf("Index%d", index);
        p->val = index;
        c++;
    }
    p->next = NULL;
    printf("->%d<", sum);
    return head;
}

# ~ AbelR007