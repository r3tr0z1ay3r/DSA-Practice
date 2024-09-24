"""
Prblm:
Given an int arr prices, each ith value is price of crypto on that day,
Decide a day to buy and another day to sell the coin in the future to sell,
Find the maximum profit we can achieve.

We can also choose to not make any transactions

Approach:
Since the array would consits of values in sequential order (Each day's value) we have to traverse from start to end,
Let us initially take the first value as the lowest possible and traverse through the list,
for every iteration we compare the difference between the current value and the lowest value and the lowest value,
if the value exceeds the current profit, we update it

while traversing if we find a new lower value, we update the lowest value to that and continue with the traversal


"""


class Solution:
    def maxProfit(self,prices:list[int]) -> int:
        lowest = prices[0]
        res = 0
        for i in prices:
            if i < lowest:
                lowest = i
            res = max(res,i-lowest)
        print(res)
        return res
obj = Solution()
prices = [10,1,5,6,7,1]
obj.maxProfit(prices)
            