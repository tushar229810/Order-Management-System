from exceptions import OutOfStockError
from utils import validate_price,validate_quantity
class Product:
    def __init__(self, product_id, name, price, stock):
        validate_price(price)
        validate_quantity(stock)
        self.product_id=product_id
        self.name=name
        self.price=max(0,price)
        self.stock=max(0,stock)
        # TODO: Initialize attributes
        # Hint: validate that price >= 0 and stock >= 0
        

    def __str__(self):
        
        return f"Product[{self.product_id}] {self.name}-${self.price},Stock: {self.stock}"
        # TODO: Return formatted string
        # Hint: f"Product[{self.product_id}] {self.name} - ${self.price}, Stock: {self.stock}"
        

    def update_stock(self, quantity): 
            if quantity>=0:
                self.stock=quantity
            else:
                raise OutOfStockError("The quantity should not be negetive")
   
         
            
            
    def add_stock (self,quantity):
            validate_quantity(quantity)
            if quantity>=0:
                self.stock+=quantity
            else:
                raise OutOfStockError("The quantity should not be in negative")
            
            
    def reduce_stock(self,quantity):
            validate_quantity(quantity)
            if quantity < 0:
                raise OutOfStockError("The quantity doesn't go below zero")
            elif quantity > self.stock:
                raise OutOfStockError(f"Insufficient stock.Available:{self.stock},Requested:{quantity}")
            self.stock-=quantity    
         
            
        # TODO: Increase or decrease stock
        # Hint: self.stock += quantity (but ensure it doesn't go below 0)
        
