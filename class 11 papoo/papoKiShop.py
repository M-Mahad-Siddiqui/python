shop = {
    "pencil": {"price": 10, "stock": 5},
    "notebook": {"price": 50, "stock": 20},
    "eraser": {"price": 5, "stock": 3},
    "pen": {"price": 20, "stock": 10},
    "sharpener": {"price": 15, "stock": 7},
    "book": {"price": 100, "stock": 1},
    "ruler": {"price": 8, "stock": 15},
    "highlighter": {"price": 25, "stock": 6},
    "calculator": {"price": 50, "stock": 2},
    "stapler": {"price": 30, "stock": 4},
    "paper": {"price": 5, "stock": 50}
}
total_amount = 0  # Total purchase amount

while True:
    item = input("Kia chaye? ").strip().lower()

    if item in shop:
        price = shop[item]["price"]
        available_stock = shop[item]["stock"]
        print(f"{item.capitalize()} costs Rs. {price} each.")

        try:
            quantity = int(input("Kitne chahye? "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        if 0 < quantity <= available_stock:
            subtotal = quantity * price
            total_amount += subtotal
            shop[item]["stock"] -= quantity

            # Discount Calculation
            if total_amount >= 300:
                discount = total_amount * 0.02  # 2% discount
            elif total_amount >= 200:
                discount = total_amount * 0.01  # 1% discount
            else:
                discount = 0

            if input("Or kuch chahye? (haan/nahi) ").strip().lower() == "nahi":
                print(f"Total for {quantity} {item}(s): Rs. {subtotal}")
                break
        else:
            print("Itne sarey nahi hen. Mazrat!")

    else:
        print("Not Available!")

# Final Bill
amount_payable = total_amount - discount
print(f"\nTotal Purchased Amount: Rs. {total_amount}")
print(f"Discount Amount: Rs. {discount}")
print(f"Final Amount Payable: Rs. {amount_payable}")

# cart = {}
# def show_cart():
#     if cart:
#         print("\nYour cart:")
#         for item, details in cart.items():
#             print(f"{item.capitalize()} - Quantity: {details['quantity']} - Price: {details['price']} each - Total: {details['quantity'] * details['price']}")
#     else:
#         print("\nYour cart is empty.")

# def update_cart(item, qty):
#     if item in cart:
#         cart[item]['quantity'] += qty
#     else:
#         cart[item] = {"quantity": qty, "price": shop[item]['price']}

# def process_purchase():
#     total_bill = 0
#     for item, details in cart.items():
#         total_bill += details['quantity'] * details['price']
#     print(f"\nTotal Bill: {total_bill}")

# def main():
#     while True:
#         select = input("\nWhat do you want to buy? ").lower()

#         if select in shop:
#             if shop[select]["stock"] > 0:
#                 print(f"Yes, we have {select} in our shop.")
#                 try:
#                     qty = int(input("Tell me how much you want? "))
#                     if qty > shop[select]["stock"]:
#                         print(f"Sorry, we only have {shop[select]['stock']} {select}(s) in stock.")
#                     else:
#                         shop[select]["stock"] -= qty
#                         update_cart(select, qty)
#                         print(f"{qty} {select}(s) added to your cart.")
#                 except ValueError:
#                     print("Invalid quantity. Please enter a valid number.")
#             else:
#                 print(f"Sorry, we are out of stock for {select}.")
#         else:
#             print(f"Item '{select}' not available in our shop.")

#         more = input("\nDo you want to buy something else? (yes/no): ").lower()
#         if more != 'yes':
#             break

#     show_cart()
#     process_purchase()

# if __name__ == "__main__":
#     main()
