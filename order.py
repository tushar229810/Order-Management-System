from exceptions import InvalidOrderOperationError
from order_status import OrderStatus
from utils import validate_quantity


class Order:
    def __init__(self, order_id, customer):
        self.order_id=order_id
        self.customer=customer
        self.products={}
        self.status= OrderStatus.PENDING
        # TODO: Initialize with empty products dict
        # Hint: self.products = {}
    

    def add_product(self, product, qty):
        # TODO: Add product to dict
        # Hint: self.products[product] = self.products.get(product, 0) + qty
        validate_quantity(qty)
        self.products[product]=self.products.get(product,0)+qty
        print(f"Added{qty} of {product.name}")

    def remove_product(self, product_id):
        # TODO: Remove product from dict
        # Hint: loop through keys and match product.product_id
        for  product in self.products.keys():
            if product.product_id==product_id:
                del self.products[product]
                print(f"removed product: {product.name}")
                return
            else:
                raise InvalidOrderOperationError(f"Product ID {product_id} not found for order {self.order_id}...")

    def calculate_total(self):
        # TODO: Return total amount
        # Hint: Use sum(p.price * qty for p, qty in self.products.items())
        total=sum(p.price*qty for p,qty in self.products.items())
        return total

    def update_status(self, new_status):
        # TODO: Update order status
        if not isinstance(new_status,OrderStatus):
            raise InvalidOrderOperationError("Invalid Status Provided")
        else:
            self.status=new_status
    def get_summary(self):
        products_list=",".join([f"{p.name} (x{qty})" for p, qty in self.products.items()])
        total = self.calculate_total()
        return f"Order {self.order_id} - Status: {self.status.value} - Products: {products_list} - Total: ${total:.2f}"
    
    def __str__(self):
        
        return self.get_summary()


        
        
        
        
        
        
        
        
        
        
        
    