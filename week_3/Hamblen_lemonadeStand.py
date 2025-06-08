"""
Author: Noah Hamblen
Date: 6/7/25
File Name: Hamblen_lemonadeStand.py
Description: This program uses functions to calculate the cost of making lemonade and the profit from selling it.
"""

def main():
    # Variables for each dollar amount
    lemons_cost = 5
    sugar_cost = 3
    selling_price = 12

    # Function that takes 2 parameters and calculates the cost
    def calculate_cost(lemons_cost, sugar_cost):
        total_cost = lemons_cost + sugar_cost # Calculating the total cost
        return total_cost # Return the total cost

    # Function that takes 3 parameters and calculates the profit
    def calculate_profit(lemons_cost, sugar_cost, selling_price):
        total_cost = calculate_cost(lemons_cost, sugar_cost)# Get the total cost from calculate_cost function

        total_profit = selling_price - total_cost # Calculating the total profit
        return total_profit # Return the total profit

    print(f"It costs ${calculate_cost(lemons_cost, sugar_cost)} to purchase lemons and sugar.") # Printing the total cost
    print (f"You sold lemonade for ${selling_price}.") # Printing sell price
    print(f"You make ${calculate_profit(lemons_cost, sugar_cost, selling_price)} in profit! 🎇") # Printing the total profit

    input ("Press any button to close") # Put in to avoid shell closing (assignment still made in VScode)

# This ensures that the main() function runs only when the script is executed directly, and not when it is imported as a module in another script.
if __name__ == "__main__":
    main()




# Same output as before, but using string concatenation to satisfy the assignment instructions

"""

cost_string = "It costs $" + str(calculate_cost(lemons_cost, sugar_cost)) + " to purchase lemons and sugar."

selling_string = "You sold lemonade for $" + str(selling_price) + "."

profit_string = "You make $" + str(calculate_profit(lemons_cost, sugar_cost, selling_price)) + " in profit! 🎇"

print(cost_string)
print(selling_string)
print(profit_string)

"""
#