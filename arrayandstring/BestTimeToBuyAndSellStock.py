from typing import List


class BestTimeToBuyAndSellStock:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        profit = 0

        for p in prices[1:]:
            if (buyPrice > p):
                buyPrice = p

            profit = max(profit, p - buyPrice)

        return profit
