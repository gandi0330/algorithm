# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sub_list = []
        min_price = prices[0]
        max_profit = []
        for i in range(len(prices)):
            if min_price > prices[i]  :
                min_price = prices[i]
                max_profit.append(max(sub_list) - min(sub_list))
                sub_list = [prices[i]]
            
            elif i == len(prices) - 1:
                sub_list.append(prices[i])
                max_profit.append(max(sub_list) - min(sub_list))
            else: 
                sub_list.append(prices[i])
            
        return max(max_profit) if len(max_profit) != 0  else 0