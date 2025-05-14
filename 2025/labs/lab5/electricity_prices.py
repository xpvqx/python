def cheapest_3h(prices):
    min_avg_price = float('inf')
    best_index = 0
    
    for i in range(len(prices) - 2):
        avg_price = sum(prices[i:i+3]) / 3
        
        if avg_price < min_avg_price:
            min_avg_price = avg_price
            best_index = i
    
    return best_index
