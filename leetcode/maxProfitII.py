
INT_MAX = (1 << 31) - 1
INT_MIN = -(1 << 31)

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0

        s = [0 for i in range(len(prices) + 1)]
        min_price = INT_MAX
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
            s[i] = max_profit

        e = [0 for i in range(len(prices) + 1)]
        max_price = INT_MIN
        max_profit = 0
        for i in range(len(prices) - 1, -1, -1):
            if prices[i] > max_price:
                max_price = prices[i]
            if max_price - prices[i] > max_profit:
                max_profit = max_price - prices[i]
            e[i] = max_profit

        max_profit = 0
        for i in range(1, len(prices)):
            if s[i] + e[i + 1] > max_profit:
                max_profit = s[i] + e[i + 1]
        return max_profit



if __name__ == "__main__":
    s = Solution()

    print s.maxProfit([2, 1, 2, 0, 1])
    print s.maxProfit([1,2,4,2,5,7,2,4,9,0])
    print s.maxProfit([1, 2])
    print s.maxProfit([1, 2, 4])
    print s.maxProfit([1])
    print s.maxProfit([])
