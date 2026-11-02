def lowest_and_highest(prices):
    return min(prices), max(prices)


low, high = lowest_and_highest([3.99, 12.50, 7.25, 1.75])
print(f"Cheapest: ${low:.2f}, priciest: ${high:.2f}")
