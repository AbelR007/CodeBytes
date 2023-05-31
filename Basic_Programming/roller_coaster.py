# 285. Roller Coaster

# Problem
""" Chef's son wants to go on a roller coaster ride. The height of Chef's son is 
X inches while the minimum height required to go on the ride is 
H inches. Determine whether he can go on the ride or not.
"""

# Solution
t = int(input())
for i in range(t):
    X, H = map(int,input().split())
    print('YES') if H <= X else print('NO')

# Time Complexity: O(n)
# Space Complexity: O(1)
