import sys

"""
Given an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit if you were only permitted to complete
at most one transaction i.e. buy one and sell one share of stock.

Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
"""


def max_profit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) < 2:
        return 0
    elif prices[0] > prices[1]:
        minPriceDay = 1
        maxPriceDay = 1
    else:
        minPriceDay = 0
        maxPriceDay = 1

    maxProfitSoFar = prices[maxPriceDay] - prices[minPriceDay]

    for i, price in enumerate(prices[2:], 2):
        if price < prices[minPriceDay]:
            maxProfitSoFar = max(
                maxProfitSoFar, prices[maxPriceDay] - prices[minPriceDay])
            minPriceDay = i
            maxPriceDay = i
        elif price > prices[maxPriceDay]:
            maxPriceDay = i
            maxProfitSoFar = max(
                maxProfitSoFar, prices[maxPriceDay] - prices[minPriceDay])

    return maxProfitSoFar


"""
Below is more concise solution than that presented above.

If our goal is to just return the maxprofit, then the only variables we need
are the minprice so far and the maxprofit so far.
"""
# def max_profit(prices):
#     """
#     : type prices: List[int]
#     : rtype: int
#     """
#     minprice = sys.maxsize
#     maxprofit = 0
#     for price in prices:
#         if price < minprice:
#             minprice = price
#         elif price - minprice > maxprofit:
#             maxprofit = price - minprice
#     return maxprofit
