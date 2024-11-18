def reduce_price(prices):
    max_price = max(prices)
    discount = max_price * 0.1
    new_price = max_price - discount
    return new_price

prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] # example prices
result = reduce_price(prices)
print("The new price after reducing by 10% is: ", result)
