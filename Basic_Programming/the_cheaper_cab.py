# 399. The Cheaper Cab

# Problem
"""Chef has to travel to another place. For this, he can avail any one of two cab services.
The first cab service charges X rupees.
The second cab service charges Y rupees.
Chef wants to spend the minimum amount of money. Which cab service should Chef take?
"""


# Solution
t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    if x < y:
        print('FIRST')
    elif x == y:
        print('ANY')
    else:
        print('SECOND')

# Time Complexity: O(n)
# Space Complexity: O(1)
