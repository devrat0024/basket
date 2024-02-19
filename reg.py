def create_basket():
    basket = {}
    while True:
        item = input("Enter item (or 'done' to finish): ")
        if item.lower() == 'done':
            break
        price = float(input("Enter price for {}: $".format(item)))
        basket[item] = price
    return basket

def display_basket(basket):
    print("\nBasket Contents:")
    total_cost = 0
    for item, price in basket.items():
        print("{}: ${:.2f}".format(item, price))
        total_cost += price
    print("Total Cost: ${:.2f}".format(total_cost))

# Example usage
basket_list = create_basket()
display_basket(basket_list)