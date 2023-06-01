# 150. Evaluate Reverse Polish Notation
# =========================================================================
from typing import List

## Solution
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluates a Reverse Polish Notation.

        Args:
            tokens: Array of strings
        
        Returns:
            Result of the expression
        """
        stack = []
        for i in tokens:
            if i == '+':
                stack.append(stack.pop() + stack.pop())
            elif i == '-':
                stack.append(-stack.pop() + stack.pop())
            elif i == '*':
                stack.append(stack.pop() * stack.pop())
            elif i == '/':
                stack.append(int(1 / stack.pop() * stack.pop()))
            else:
                stack.append(int(i))
        return stack[0]

# Explanation :-
#   You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
