'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      # Create a hash map to keep track of the indicies and numbers we've seen
        hm = {}
      # Because we need to see both the index and the number itself, we use enumerate
        for i, num in enumerate(nums):
          # Create a variable that keeps track of the target number minus the number
          # that we are currently viewing in the array 
            tracker = target - num
          # Does the tracker exist inside of our hash map?
            if tracker in hm:
              # If so, lets return the index we are currently at in the array and 
              # the index of the tracker inside of our hash map
                return [i, hm[tracker]]
            else:
              # If not, lets add our number and its index to the hash map
                hm[num] = i
