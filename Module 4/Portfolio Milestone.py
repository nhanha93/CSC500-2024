class ItemToPurchase:
    item_name: str = "none"
    item_price: float = 0.0
    item_quantity: int = 0
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost:.2f}")

print("Item 1")
item1 = ItemToPurchase()
item1.item_name = input("Enter item name: ")
item1.item_price = float(input("Enter item price: "))
item1.item_quantity = int(input("Enter item quantity: "))

print("Item 2")
item2 = ItemToPurchase()
item2.item_name = input("Enter item name: ")
item2.item_price = float(input("Enter item price: "))
item2.item_quantity = int(input("Enter item quantity: "))

print("TOTAL COST")
item1.print_item_cost()
item2.print_item_cost()

total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
print(f"Total: ${total_cost:.2f}")




