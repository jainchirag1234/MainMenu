menu = {
    'Pizza':99,
    'Pasta':89,
    'Burger':59,
    'Salad':79,
    'Coffee':98
}
# print(menu)
print("Welcome to PYTHON Restaurant")
print("Pizza: Rs99\nPasta: Rs89\nBurger: Rs59\nSalad: Rs79\nCoffee: Rs98")

order_total = 0

item_1= input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Your item{item_1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order =="Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available")

print(f"The total amount of item to pay is {order_total}")