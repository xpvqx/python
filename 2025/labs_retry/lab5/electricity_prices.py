# bästa tillfället är att köra tvättmaskin under tre sammanhängande
# timmar då medelpriset är som lägst
# vi är ej intresserade av vad priset blir 
# vi är ute efter vilken tid vi ska sätta igång maskinen

# definition som tar en lista med priser per timme
def cheapest_3h(prices):
    # hitta index för position då den billigaste tre timmar 
    # då medelpriset är som lägst

    best_index = float('inf')
    min_avg_price = 0

    for i in range(len(prices) - 2):
        avg_price = sum(prices[i:i+3]) / 3

        if avg_price < min_avg_price:
            min_avg_price = avg_price
            best_index = i

    return best_index
