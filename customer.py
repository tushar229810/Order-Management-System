from exceptions import CustomerNotFoundError
"""
Customer class file

Step-by-step Instructions:
1. Define attributes:
   - customer_id (int)
   - name (str)
   - email (str)
   - orders (list of Order objects)
2. Add __init__, add_order, get_order_history methods.
Hint: Use a list to store order references.
"""

class Customer:
    def __init__(self, customer_id, name, email):
        # TODO: Initialize attributes
        # Hint: self.orders = []
        self.customer_id=customer_id
        self.name=name
        self.email=email
        self.orders=[]

    def add_order(self, order):
        # TODO: Append order to list
        # Hint: self.orders.append(order)
        if order in self.orders:
            raise CustomerNotFoundError("Order already exist for this customer")
            
        self.orders.append(order)

    def get_order_history(self):
        # TODO: Return order details
        # Hint: Loop through self.orders and return summaries
        if not self.orders:
            return "Not ordered yet!",[]
            
        summaries=[]
        for order in self.orders:
            summaries.append(order.get_summary())
            
            
        return summaries
