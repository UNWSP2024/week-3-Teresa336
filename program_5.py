#Programmer: Teresa Fischer
#Date: 9/19/2024
#Title: Program #5: Hot Dog

# There are two kinds of hot dogs sold:
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost.

#Type of Hot Dog
hot_dog_type = input('Choose a type of hot dog: (Type A for Hot Dog, Type B for Chili Dog)')
cheese = input('Do you want cheese?: (yes or no)')
peppers = input('Do you want peppers?: (yes or no)')
grilled_onions = input('Do you want grilled onions?: (yes or no)')

#Calculate cost
def calculate_price(hot_dog_type):
    cost = 0.0
    if hot_dog_type == 'A':
        cost += 3.50
    elif hot_dog_type =='B':
        cost += 4.50
    if cheese == 'yes':
        cost += .50
    if peppers == 'yes':
        cost += .75
    if grilled_onions == 'yes':
        cost += 1.00

    return cost

#Calculate tax
def calculate_tax():
    tax = cost * .07

    return tax

#Calculate total
def calculate_total():
    total = cost + tax

    return total

cost = calculate_price(hot_dog_type)
print('Hot Dog Cost: $', format(cost, '.2f'))

tax = calculate_tax()
print('Tax: $', format(tax, '.2f'))

total = calculate_total()
print('Total: $', format(total, '.2f'))
