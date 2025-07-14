#Define the menu

Menu={'Pizza':80,
      'Pasta':100,
      'Burger':69,
      'Salad':70,
      'Fries':50
      }

#greet
print("Welcome to Loki Den")
print("\nMenu:\n")
print('Pizza : rs80\nPasta: rs100\nBurger: rs69\nSalad: rs70\nFries: rs50')    #\n = new line


order_total=0    #sum of 2 or 3 or no of orders

item_1=input("Enter the name of item=")
if item_1 in Menu:
    order_total +=Menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f'Order item {item_1} is not available yet!')

another_order=input('Do you want another item? (Y/N)')
if another_order=="Y":
    item_2=input("Enter the second item=")
    if item_2 in Menu:
        order_total +=Menu[item_2]
        print(f"item{item_2} has been added to order")
else:
    print(f"Ordered item{item_2} is not available")

print(f"The total amount of your purchase is {order_total}")