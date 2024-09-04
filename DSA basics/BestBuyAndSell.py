class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        lowest = prices[0]
        for i in prices:
            if i<lowest:
                lowest = i
            diff = max(diff,i-lowest)
        return diff


