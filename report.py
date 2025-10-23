"""
Report class file

Step-by-step Instructions:
1. Add methods:
   - order_summary(order)
   - customer_orders(customer)
   - sales_report(orders)
2. Display clean formatted output.
Hint: Use loops and f-strings to format reports.
"""

class Report:
    def order_summary(self, order):
        # TODO: Print products and total
        # Hint: loop order.products and calculate total
        print("\n" + "="*50)
        print(f"ORDER SUMMARY - Order {order.order_id}")
        print("="*50)
        print(f"Customer: {order.customer.name}")
        print(f"Status: {order.status.value}")
        print("\nProducts:")
        print("-"*50)
        
        if not order.products:
            print("No products in this order")
        else:
            for product, qty in order.products.items():
                subtotal = product.price * qty
                print(f"  {product.name} x{qty} = ${subtotal:.2f}")
        
        total = order.calculate_total()
        print("-"*50)
        print(f"TOTAL: ${total:.2f}")
        print("="*50 + "\n")

    def customer_orders(self, customer):
        # TODO: Show all orders by a customer
        # Hint: use customer.get_order_history()
        print("\n" + "="*50)
        print(f"CUSTOMER ORDERS - {customer.name}")
        print("="*50)
        print(f"Customer ID: {customer.customer_id}")
        print(f"Email: {customer.email}")
        print("\nOrder History:")
        print("-"*50)
        
        order_history = customer.get_order_history()
        
        if not order_history:
            print("No orders found for this customer")
        else:
            for indx, order_summary in enumerate(order_history, 1):
                print(f"{indx}. {order_summary}")
        
        print("="*50 + "\n")

    def sales_report(self, orders):
        # TODO: Generate total sales
        # Hint: sum(order.calculate_total() for order in orders)
        print("\n" + "="*50)
        print("SALES REPORT")
        print("="*50)
        
        if not orders:
            print("No orders to report")
            print("="*50 + "\n")
            return
        
        total_sales = 0
        print(f"\nTotal Orders: {len(orders)}")
        print("\nOrder Details:")
        print("-"*50)
        
        for order in orders:
            order_total = order.calculate_total()
            total_sales += order_total
            print(f"Order #{order.order_id} - Customer: {order.customer.name} - Total: ${order_total:.2f}")
        
        print("-"*50)
        print(f"TOTAL SALES: ${total_sales:.2f}")
        print("="*50 +"\n")