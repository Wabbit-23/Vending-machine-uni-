import csv

# Declaring Constants
ACCEPTED_COIN = [200, 100, 50, 20] # Coin in pence
RECEIPT_PATH = "receipts.csv"
GBP_SYMBOL = "£"

# Pence to GBP
def gbp_format(pence):
    pounds = pence / 100
    return GBP_SYMBOL + f"{pounds:.2f}"

# Initialize - return vending items 
def vending_items():
    return {
        "A1": {"name": "Water", "price": 120, "stock": 8},
        "A2": {"name": "Soda", "price": 150, "stock": 6},
        "B1": {"name": "Chocolate", "price": 250, "stock": 5},
        "B2": {"name": "Crisps", "price": 140, "stock": 7},
        "C1": {"name": "Sandwich", "price": 380, "stock": 4},
        "C2": {"name": "Granola Bar", "price": 180, "stock": 6},

    }

# Printing the menu
def menu(items):
    print("\nItems available:")
    print("-----------------")

    for code, item in items.items():
        price_txt = gbp_format(item["price"])

        if item["stock"] > 0:
            stock_txt = f"{item['stock']} in stock"
        else:
            stock_txt = "OUT OF STOCK"

        print(f"{code}: {item['name']} - {price_txt} - {stock_txt}")
    print("-----------------")

#Displaying the current balance
def balance_show(balance):
    print(f"Current balance: {gbp_format(balance)}")

# Adding coins to the vending balance 
def insert_coins(balance):
    print("\nInsert coins (2 for \u00a32, 1 for \u00a31, 50, or 20). Type 'done' when finished.")

    while True:
        user_input = input("Enter a coin (£2, £1, 50p, 20p): ").strip().lower()

        if user_input == "done":
            break
        try:
            value = int(user_input)

        except ValueError:
            print("Please enter a number like 2, 1, 50, 20 or 'done'.")
            continue

        if value == 2:
            value = 200
        elif value == 1:
            value = 100

        if value in ACCEPTED_COIN:
            balance += value
            balance_show(balance)
        else:
            print("Coin not accepted. Use £2, £1, 50p, or 20p.")

    return balance

# User selects the item
def select_items(items, balance):
    purchased = {}
    total_spent = 0

    while True:
        menu(items)
        balance_show(balance)

        choice_raw = input("Enter item code to buy, or 'done' to finish: ").strip()

        if choice_raw.lower() == "done":
            break

        choice = choice_raw.upper()

        if choice not in items:
            print("Invalid item code.")
            continue
        if items[choice]["stock"] <= 0:
            print("Item out of stock.")
            continue

        price = items[choice]["price"]
        if balance < price:
            print("Not enough balance to buy this item.")
            continue

        balance -= price
        items[choice]["stock"] -= 1

        purchased.setdefault(choice, 0)
        purchased[choice] += 1

        total_spent += price

    return purchased, total_spent, balance

# 
def discount(total_spent, item_count):
    discount_percentage = 0

    if item_count >= 3:
        discount_percentage = 5
    if total_spent > 500:
        discount_percentage = max(discount_percentage, 10)
    if total_spent > 700:
        discount_percentage = max(discount_percentage, 15)

    discount_total = total_spent * discount_percentage // 100
    return discount_total, discount_percentage


def bonus(order_number, total_spent):
    if order_number % 2 == 1 and total_spent > 200:
        return 100  
    return 0

def change(balance):
    change = {}
    leftover = balance

    for coin in ACCEPTED_COIN:
        if leftover >= coin:
            count = leftover // coin
            change[coin] = count
            leftover -= coin * count

    return change, leftover

def change_format(change_dict):
    parts = []
    for coin, count in change_dict.items():
        if coin >= 100:
            label = f"£{coin // 100}"
        else:
            label = f"{coin}p"
        parts.append(f"{label} x{count}")
    return ", ".join(parts) if parts else "No change"


def receipt():
    try:
        with open(RECEIPT_PATH, "x", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "order_number",
                "items",
                "items_total_pence",
                "discount_pence",
                "discount_percent",
                "bonus_pence",
                "refund_pence",
                "change_given",
                "remaining_balance_pence",
            ])
    except FileExistsError:
        pass

def write_receipt(order_number, purchased, total_spent, discount_amount,
                  discount_percent, bonus_amount, refund, change_dict, leftover):
    receipt()

    items_str_parts = [f"{code} x{count}" for code, count in purchased.items()]
    items_str = "; ".join(items_str_parts)

    change_str = change_format(change_dict)

    with open(RECEIPT_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            order_number,
            items_str,
            total_spent,
            discount_amount,
            discount_percent,
            bonus_amount,
            refund,
            change_str,
            leftover,
        ])


if __name__ == "__main__":
    items = vending_items()
    order_number = 1

    while True:
        print(f"\n--- Customer {order_number} ---")
        balance = 0

        balance = insert_coins(balance)
        purchased, total_spent, balance = select_items(items, balance)

        if not purchased:
            print("No items purchased.")
        else:
            item_count = sum(purchased.values())

            discount_amount, discount_percent = discount(total_spent, item_count)
            total_after_discount = total_spent - discount_amount

            bonus_amount = bonus(order_number, total_spent)
            total_after_discount_with_bonus = total_after_discount - bonus_amount

            refund = discount_amount + bonus_amount
            balance += refund

            change_dict, leftover = change(balance)

            write_receipt(
                order_number,
                purchased,
                total_spent,
                discount_amount,
                discount_percent,
                bonus_amount,
                refund,
                change_dict,
                leftover,
            )

            print("\nSUMMARY")
            print("You bought:", purchased)
            print("Items total:", gbp_format(total_spent))
            print(f"Discount applied: {discount_percent}% -> -{gbp_format(discount_amount)}")
            print("Bonus applied:", gbp_format(bonus_amount))
            print("Refund from discount+bonus:", gbp_format(refund))
            print("Change returned:", change_format(change_dict))
            print("Amount kept by machine:", gbp_format(leftover))

        again = input("\nNext customer? (y/n): ").strip().lower()
        if again != "y":
            break

        order_number += 1