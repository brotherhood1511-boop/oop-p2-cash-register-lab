#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount  # goes through the setter below
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        # Only accept a whole-number percentage between 0 and 100.
        if isinstance(discount, int) and 0 <= discount <= 100:
            self._discount = discount
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        # Add to the running total.
        self.total += price * quantity
        # Record the item name once per unit purchased.
        for _ in range(quantity):
            self.items.append(item)
        # Keep a record of this transaction so it can be voided later.
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        # A discount of 0 means none was set, so there's nothing to apply.
        if self.discount:
            self.total -= self.total * (self.discount / 100)
            # Print whole dollar amounts without a trailing ".0"
            total_display = int(self.total) if self.total == int(self.total) else self.total
            print(f"After the discount, the total comes to ${total_display}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return
        # Undo the most recent transaction: remove it from history,
        # subtract its cost, and drop its items from the items list.
        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction["price"] * last_transaction["quantity"]
        for _ in range(last_transaction["quantity"]):
            self.items.remove(last_transaction["item"])
