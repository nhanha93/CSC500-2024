class ItemToPurchase:
    def __init__(self, item_name="none", item_description = "none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        item_name = item_name.strip().lower()
        for item in self.cart_items:
            if item.item_name.strip().lower() == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        item_name = item_to_purchase.item_name.strip().lower()
        for item in self.cart_items:
            if item.item_name.strip().lower() == item_name:
                if item_to_purchase.item_price != 0.0:
                    item.item_price = item_to_purchase.item_price
                if item_to_purchase.item_quantity > 0:
                    item.item_quantity = item_to_purchase.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0.0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_total(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print("Number of Items:", self.get_num_items_in_cart())
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total Cost: ${self.get_cost_of_cart():.2f}")

    def print_description(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print("\nItem Descriptions:")
            for item in self.cart_items:
                print(f"{item.item_name}: {item.item_description}")


def print_menu(shopping_cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option: ")

        if choice == 'a':
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            shopping_cart.add_item(item)

        elif choice == 'r':
            item_name = input("Enter the item name to remove: ")
            shopping_cart.remove_item(item_name)
            print("Item removed from cart")

        elif choice == 'c':
            item_name = input("Enter the item name to modify: ")
            item_price = float(input("Enter the item price(0 if no change): "))
            item_quantity = int(input("Enter the new item quantity: "))
            item = ItemToPurchase(item_name, "",item_price, item_quantity)
            shopping_cart.modify_item(item)

        elif choice == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            shopping_cart.print_description()

        elif choice == 'o':
            print("OUTPUT SHOPPING CART")
            shopping_cart.print_total()

        elif choice == 'q':
            break

        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    customer = input("Enter customer's name: ")
    date = input("Enter today's date: ")
    cart = ShoppingCart(customer, date)

    print(f"\nCustomer name: {customer}")
    print(f"Today's date: {date}")

    print_menu(cart)
