class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")

class ShoppingCart:
    customer_name: str = "none"
    current_date: str = "January 1, 2020"
    cart_items: list = []

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, ItemToPurchase):
        for item in self.cart_items:
            if item.item_name == ItemToPurchase.item_name:
                if ItemToPurchase.item_price != 0.0:
                    item.item_price = ItemToPurchase.item_price
                if ItemToPurchase.item_quantity != 0:
                    item.item_quantity = ItemToPurchase.item_quantity
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
                print(f"{item.item_name}: {item.item_quantity} @ ${item.item_price:.2f}")

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
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item = ItemToPurchase(item_name, item_price, item_quantity)
            shopping_cart.add_item(item)

        elif choice == 'r':
            item_name = input("Enter the item name to remove: ")
            shopping_cart.remove_item(item_name)

        elif choice == 'c':
            item_name = input("Enter the item name to modify: ")
            item_price = float(input("Enter the new item price: "))
            item_quantity = int(input("Enter the new item quantity: "))
            item = ItemToPurchase(item_name, item_price, item_quantity)
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
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    cart = ShoppingCart()

    cart.customer_name = customer_name
    cart.current_date = current_date

    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")

    print_menu(cart)
