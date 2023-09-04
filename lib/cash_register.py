#!/usr/bin/env python3



class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []

    def add_item(self, title, price, quantity=1):
        item = {"item": title, "price": price, "quantity": quantity}
        self.items.append(item)
        self.total += price * quantity

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount  # Reduce the total by the discount amount
            message = f'After the discount, the total comes to ${self.total:.2f}'  # Format the message with two decimal places
            print(message)
            return message
        else:
            message = 'There is no discount to apply.'
            print(message)
            return message

          
    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            self.total -= last_item["price"] * last_item["quantity"]

    def get_items(self):
        item_list = []
        for item in self.items:
            for _ in range(item["quantity"]):
                item_list.append({"item": item["item"], "quantity": 1})
        return item_list

  

