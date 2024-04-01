## Buy and sell stock problem (price at each day given, you can buy any time, then sell in future, return max profit) Follow up: return buy and sell day as well
`Educative`

You can solve the buy and sell stock problem in Python by iterating through the prices and keeping track of the minimum price seen so far and the maximum profit that can be made. Additionally, you can keep track of the buy and sell days. Here's a Python function to achieve this:

```python
def max_profit(prices):
    if len(prices) < 2:
        return 0, None, None  # If there are less than two prices, no profit can be made

    min_price = prices[0]
    max_profit = 0
    buy_day = sell_day = 0

    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
            buy_day = i
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
            sell_day = i

    return max_profit, buy_day, sell_day

# Example usage:
prices = [7, 1, 5, 3, 6, 4]
profit, buy_day, sell_day = max_profit(prices)
print("Max profit:", profit)
print("Buy on day:", buy_day)
print("Sell on day:", sell_day)
```

This function takes a list of prices as input and returns the maximum profit that can be made, along with the buy and sell days. It iterates through the prices, updating the minimum price seen so far and the maximum profit that can be made. Finally, it returns the maximum profit, buy day, and sell day.