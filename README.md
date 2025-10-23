# ORDER Management SYSTEM
## Overview
This project is an Order Management System that allows you to manage customers, products, and orders.
The system lets you create orders, add products to an order, remove products from an order, and view order summaries and customer order history.

## Features
- **Customer Management**: Create and manage customer records.
- **Order Creation**: Create orders and assign them to customers.
- **Add/Remove Products**: Add and remove products from orders.
- **View Order Summary**: View detailed summaries of orders.
- **Customer Order History**: View all orders placed by a specific customer.
- **Generate Unique IDs**: Automatically generate unique IDs for orders.

## Requirements
- Python 3.x
- OOPS,Exception,Error Handling,File Import and Export,

## Files
- **product.py**: Defines the `Product` class for product details.
- **order.py**: Defines the `Order` class for handling orders and their statuses.
- **customer.py**: Defines the `Customer` class for managing customer information.
- **order_status.py**: Contains the `OrderStatus` Enum for order statuses (e.g., Pending, Shipped, Delivered, Cancelled).
- **utils.py**: Contains utility functions like ID generation and validation functions.
- **exceptions.py**: Contains custom exceptions for error handling (e.g., `OutOfStockError`, `InvalidOrderOperationError`).
- **main.py**: The main driver file that runs the program and provides the menu-based interface for managing orders.

 
