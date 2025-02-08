'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0

'''
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        # Bottom Up DP (Tabulation)
        # Time: O(Coins * Amount)
        # Space: O(Amount)

        # Sort coins in asc order such that we 
        # always look at the smallest coins first
        coins.sort()

        # Set a variable that houses the minimum number
        # of coins it takes to make a certain amount.  
        # Because we want to include zero as our base case
        # lets use amount + 1
        dp = [0] * (amount + 1)

        # Loop through everything that is not our base case
        # starting from 1 (inclusive) to our amount + 1
        for i in range(1, amount + 1):
            # Set a minimum tracker to a number that will never
            # be in our coins list
            minn = float('inf')

            # Loop through each coin in coins
            for coin in coins:
                # Establish a difference being where we are 
                # minus the coin that we are using
                diff = i - coin

                # If that caluculation causes our difference to
                # become negative, we know that we no longer need 
                # to move on, and we can break from this loop
                if diff < 0:
                    break

                # If we have a positive number, we can now set our
                # minimum tracker to the minimum of itself and 
                # dp at the difference position + 1 (the coin we are
                # currently using)
                minn = min(minn, dp[diff] + 1)

            # Set our i position within dp equal to our minimum tracking 
            # variable
            dp[i] = minn 

        # If the amount position within dp is less than infinity, that
        # means we have a real number and we can return it as an 
        # answer
        if dp[amount] < float('inf'):
            return dp[amount]
        # Else, we need to return -1 per the ask of the question
        else:
            return -1
