
def calculate_subtotal(products):
    """Calculate the total price of all products."""
    subtotal = 0

    for product in products:
        subtotal += product["quantity"] * product["price"]

    return subtotal


def calculate_discount(subtotal, discount_rate):
    """Calculate the discount amount."""
    return subtotal * discount_rate / 100


def calculate_tax(amount, tax_rate):
    """Calculate tax on the amount after discount."""
    return amount * tax_rate / 100


def display_bill(products, subtotal, discount, tax, final_amount):
    """Display the formatted shopping bill."""
    print("\n" + "=" * 55)
    print("                 SHOPPING BILL")
    print("=" * 55)
    print(f"{'Product':<18}{'Qty':>5}{'Price':>12}{'Total':>12}")
    print("-" * 55)

    for product in products:
        total = product["quantity"] * product["price"]
        print(
            f"{product['name']:<18}"
            f"{product['quantity']:>5}"
            f"{product['price']:>12.2f}"
            f"{total:>12.2f}"
        )

    print("-" * 55)
    print(f"{'Subtotal:':>39} Rs. {subtotal:>10.2f}")
    print(f"{'Discount:':>39} Rs. {discount:>10.2f}")
    print(f"{'Tax:':>39} Rs. {tax:>10.2f}")
    print("=" * 55)
    print(f"{'Final Amount:':>39} Rs. {final_amount:>10.2f}")
    print("=" * 55)
    print("          Thank you for shopping!")


def main():
    products = []

    print("===== Shopping Bill Generator =====")

    while True:
        name = input("\nEnter product name (or 'done' to finish): ")
        name = name.strip()

        if name.lower() == "done":
            break

        if not name:
            print("Product name cannot be empty.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per item (Rs.): "))

            if quantity <= 0 or price < 0:
                print("Quantity must be positive and price cannot be negative.")
                continue

        except ValueError:
            print("Please enter a valid quantity and price.")
            continue

        product = {
            "name": name,
            "quantity": quantity,
            "price": price
        }

        products.append(product)
        print("Product added successfully!")

    if not products:
        print("\nNo products added. Bill cannot be generated.")
        return

    subtotal = calculate_subtotal(products)

    try:
        discount_rate = float(input("\nEnter discount percentage (0-100): "))
        tax_rate = float(input("Enter tax percentage (0-100): "))

        if not (0 <= discount_rate <= 100 and 0 <= tax_rate <= 100):
            print("Discount and tax must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter valid discount and tax percentages.")
        return

    discount = calculate_discount(subtotal, discount_rate)
    amount_after_discount = subtotal - discount
    tax = calculate_tax(amount_after_discount, tax_rate)
    final_amount = amount_after_discount + tax

    display_bill(products, subtotal, discount, tax, final_amount)


if __name__ == "__main__":
    main()
