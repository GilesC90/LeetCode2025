'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Constraints:

0 <= n <= 30
'''

class Solution:
    def fib(self, n: int) -> int:
        # Establish a base case of 
        # n == 0
        if n <= 1:
            return n
        # Use variables to keep track
        # of last two nums in sequence
        a = 0
        b = 1

        # Create a for loop, starting at 2
        # that covers from 2 through n
        for _ in range (2, n):
            # Instantiate our variable that holds
            # the value of a + b
            c = a + b
            # Update a and b values 
            a = b
            b = c

        # Return our answer
        return a + b


'''
Why this works

Given that this is usually the intro to Dynamic Programming for most users, understand that we want to utilize memoization to 
prevent ourselves from repetative calculations.  This can be done a number of ways but the simplest for me to understand is 
using two variables to keep track of our footsteps behind us as we look for or final value at 'n'.  

Our base case

We understand that if n == 0 or n == 1, we need to return n so, we call that out immediately

Moving onward

We instantiate two separate variables that hold onto our prior steps through the sequence.  We then want to loop through each position,
starting at 2, and work our way down to n.  As we move to n, we create a third variable that adds our two prior footsteps together and 
acknowledge our traversal to the next step through the sequence by updating our initial variables.

Our return statement

When we finally reach n, we know that the answer to F(n) is F(n - 1) + F(n - 2).  Our 'a' variable is our F(n - 1) and 'b' is F(n - 2).
All we would need to do is add our a and b together to get our correct return statement

Time Complexity is O(n) and beats 95.82% on LC
Memory beats 36.24%
'''
