
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        min_price = (1 << 31) - 1
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            if price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit



if __name__ == "__main__":
    s = Solution()

    print s.maxProfit([0, 1, 4, 3, 5, 2])
