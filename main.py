"""
Main driver file

Step-by-step Instructions:
1. Import Product, Customer, Order, Report, etc.
2. Create sample customers and products.
3. Show menu:
   a. Create order
   b. Add product to order
   c. Remove product
   d. View order summary
   e. Customer order history
   f. Exit
4. Handle invalid input with try/except.
Hint: Use while True loop with input() for menu.
"""

from product import Product
from customer import Customer
from order import Order
from report import Report
from utils import generate_id
from exceptions import OutOfStockError, InvalidOrderOperationError


customers = []
products = []
orders = []
report = Report()


def initialize_sample_data():
    print("\n Initializing sample data...\n")
    
    # Create sample customers
    customer1 = Customer(generate_id(), "Rahul Kumar Nayak", "rahul@email.com")
    customer2 = Customer(generate_id(), "Tushar Naik", "tushar@email.com")
    customer3 = Customer(generate_id(), "Bitu Kumar", "bitu@email.com")
    
    customers.extend([customer1, customer2, customer3])
    
    print("Sample Customers Created:")
    for c in customers:
        print(f"   ID: {c.customer_id} - {c.name} ({c.email})")
    
    # Create sample products
    product1 = Product(generate_id(), "Gaming Laptop", 1299.99, 15)
    product2 = Product(generate_id(), "Wireless Mouse", 29.99, 50)
    product3 = Product(generate_id(), "Mechanical Keyboard", 89.99, 30)
    product4 = Product(generate_id(), "4K Monitor", 499.99, 20)
    product5 = Product(generate_id(), "Gaming Headset", 79.99, 40)
    
    products.extend([product1, product2, product3, product4, product5])
    
    print("\n Sample Products Created:")
    for p in products:
        print(f"   {p}")


def show_menu():
    """Display the main menu"""
    print("\n" + "="*60)
    print("           ORDER MANAGEMENT SYSTEM - MENU")
    print("="*60)
    print("  1. Create order")
    print("  2. Add product to order")
    print("  3. Remove product")
    print("  4. View order summary")
    print("  5. Customer order history")
    print("  6. Exit")
    print("="*60)


def find_customer_by_id(customer_id):
    """Find customer by ID"""
    for customer in customers:
        if customer.customer_id == customer_id:
            return customer
    return None


def find_product_by_id(product_id):
    """Find product by ID"""
    for product in products:
        if product.product_id == product_id:
            return product
    return None


def find_order_by_id(order_id):
    """Find order by ID"""
    for order in orders:
        if order.order_id == order_id:
            return order
    return None


def create_order():
    """Create a new order"""
    print("\n" + "-"*60)
    print("CREATE NEW ORDER")
    print("-"*60)
    
    # Show available customers
    print("\nAvailable Customers:")
    for c in customers:
        print(f"  ID: {c.customer_id} - {c.name}")
    
    try:
        customer_id = int(input("\nEnter Customer ID: "))
        customer = find_customer_by_id(customer_id)
        
        if not customer:
            print(" Customer not found!")
            return
        
        # Create order
        new_order = Order(generate_id(), customer)
        orders.append(new_order)
        customer.add_order(new_order)
        
        print(f"\n Order #{new_order.order_id} created successfully for {customer.name}!")
        
    except ValueError:
        print(" Invalid input! Please enter a valid number.")
    except InvalidOrderOperationError as e:
        print(f" Error: {e}")


def add_product_to_order():
    """Add product to an existing order"""
    print("\n" + "-"*60)
    print("ADD PRODUCT TO ORDER")
    print("-"*60)
    
    if not orders:
        print(" No orders available. Create an order first!")
        return
    
    # Show available orders
    print("\nAvailable Orders:")
    for o in orders:
        print(f"  Order ID: {o.order_id} - Customer: {o.customer.name} - Status: {o.status.value}")
    
    try:
        order_id = int(input("\nEnter Order ID: "))
        order = find_order_by_id(order_id)
        
        if not order:
            print(" Order not found!")
            return
        
        # Show available products
        print("\nAvailable Products:")
        for p in products:
            print(f"  {p}")
        
        product_id = int(input("\nEnter Product ID: "))
        product = find_product_by_id(product_id)
        
        if not product:
            print("Product not found!")
            return
        
        quantity = int(input("Enter Quantity: "))
        
        # Add product to order
        order.add_product(product, quantity)
        print(f"\n Added {quantity} x {product.name} to Order #{order.order_id}!")
        
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    except (InvalidOrderOperationError, OutOfStockError) as e:
        print(f" Error: {e}")


def remove_product_from_order():
    """Remove product from an order"""
    print("\n" + "-"*60)
    print("REMOVE PRODUCT FROM ORDER")
    print("-"*60)
    
    if not orders:
        print("No orders available!")
        return
    
    # Show available orders
    print("\nAvailable Orders:")
    for o in orders:
        print(f"  Order ID: {o.order_id} - Customer: {o.customer.name}")
    
    try:
        order_id = int(input("\nEnter Order ID: "))
        order = find_order_by_id(order_id)
        
        if not order:
            print(" Order not found!")
            return
        
        if not order.products:
            print(" No products in this order!")
            return
        
        # Show products in order
        print("\nProducts in this order:")
        for product, qty in order.products.items():
            print(f"  Product ID: {product.product_id} - {product.name} (Quantity: {qty})")
        
        product_id = int(input("\nEnter Product ID to remove: "))
        
        # Remove product
        order.remove_product(product_id)
        print(f"\n Product removed from Order #{order.order_id}!")
        
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    except InvalidOrderOperationError as e:
        print(f" Error: {e}")


def view_order_summary():
    """View summary of a specific order"""
    print("\n" + "-"*60)
    print("VIEW ORDER SUMMARY")
    print("-"*60)
    
    if not orders:
        print("No orders available!")
        return
    
    # Show available orders
    print("\nAvailable Orders:")
    for o in orders:
        print(f"  Order ID: {o.order_id} - Customer: {o.customer.name} - Status: {o.status.value}")
    
    try:
        order_id = int(input("\nEnter Order ID: "))
        order = find_order_by_id(order_id)
        
        if not order:
            print(" Order not found!")
            return
        
        # Display order summary
        report.order_summary(order)
        
    except ValueError:
        print("Invalid input! Please enter a valid number.")


def view_customer_order_history():
    """View all orders for a customer"""
    print("\n" + "-"*60)
    print("CUSTOMER ORDER HISTORY")
    print("-"*60)
    
    # Show available customers
    print("\nAvailable Customers:")
    for c in customers:
        print(f"  ID: {c.customer_id} - {c.name}")
    
    try:
        customer_id = int(input("\nEnter Customer ID: "))
        customer = find_customer_by_id(customer_id)
        
        if not customer:
            print("Customer not found!")
            return
        
        # Display customer orders
        report.customer_orders(customer)
        
    except ValueError:
        print(" Invalid input! Please enter a valid number.")


def main():
    """Main program loop"""
    print("\n" + "="*60)
    print("     WELCOME TO ORDER MANAGEMENT SYSTEM")
    print("="*60)
    
    # Initialize sample data
    initialize_sample_data()
    
    # Main menu loop
    while True:
        try:
            show_menu()
            choice = input("\nEnter your choice (1-6): ").lower().strip()
            
            if choice == '1':
                create_order()
            elif choice == '2':
                add_product_to_order()
            elif choice == '3':
                remove_product_from_order()
            elif choice == '4':
                view_order_summary()
            elif choice == '5':
                view_customer_order_history()
            elif choice == '6':
                print("\n" + "="*60)
                print("     Thank you for using Order Management System!")
                print("="*60)
                break
            else:
                print("\n Invalid choice! Please select a-f.")
        
        except KeyboardInterrupt:
            print("\n\n  Program interrupted by user.")
            break
        except Exception as e:
            print(f"\n An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()