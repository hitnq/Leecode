class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_p = 99999
        max_p = 0
        for price in prices:
            min_p = min(min_p,price)
            max_p = max(max_p,price-min_p)
        return max_p     