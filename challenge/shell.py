from app import app, db
from models import Product

with app.app_context():
    # Add products
    product1 = Product(name='Laptop', price=799.99, description='A high-performance laptop for professionals.', stock=10)
    product2 = Product(name='Smartphone', price=499.99, description='A smartphone with excellent battery life.', stock=20)
    product3 = Product(name='Headphones', price=149.99, description='Noise-cancelling over-ear headphones.', stock=15)
    product4 = Product(name='Smartwatch', price=199.99, description='A smartwatch with fitness tracking features.', stock=5)
    product5 = Product(name='Gaming Console', price=399.99, description='Next-gen gaming console with 4K support.', stock=8)
    
    # Add them to the session
    db.session.add(product1)
    db.session.add(product2)
    db.session.add(product3)
    db.session.add(product4)
    db.session.add(product5)
    
    # Commit the session to save the products in the database
    db.session.commit()

    print("Products added successfully!")
