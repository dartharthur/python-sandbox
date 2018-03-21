"""
Given an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit if you were only permitted to complete
at most one transaction i.e. buy one and sell one share of stock.
"""


def max_profit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    maxPriceDay = None
    minPriceDay = None

    for i, price in enumerate(prices):
      if not minPriceDay:
        minPriceDay = i
      elif not maxPriceDay:
        maxPriceDay = i
      elif price < prices[minPriceDay]:
        minPriceDay = i
      elif price > prices[maxPriceDay]:
        maxPriceDay = i
    
    return prices[maxPriceDay] - prices[minPriceDay]
