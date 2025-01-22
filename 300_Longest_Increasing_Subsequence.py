'''
Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # NOTES:
        # Remember that a subsequence differs from a subarray.  
        # A subsequence does not have to be contiguous. 

        # First, we want to create an array the same length as 
        # nums that represents the maximum length increasing 
        # subsequence assuming that we are ending at that particular
        # position in the array nums.  At the end, we want the max
        # value from our created array. -> max(createdArr)

        # We want to use a nested for loop -> i and j
        # We want the i pointed at the second position and the 
        # j pointed at the first position.  We will simply as the 
        # question "Is nums at i bigger than nums at j?" Yes? Ok, 
        # whatever we had in the position that j is pointing to
        # is currently the beginning of our increasing subsequence
        # That j position has a value of 1 and our position at i, 
        # also having a value of 1, makes our subsequence value now
        # 2.

        # We then move our i pointer to the next position and ask if 
        # this value is bigger than the value at the j position?  Yes?
        # Ok, lets now move j down to the next position.  So on and so forth.
        # 
        # 
        # Bottom Up DP (Tablulation)
        # Time: O(n^2)
        # Space: O(n)

        n = len(nums)

        dp = [1] * n 

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
