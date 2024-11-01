from app import app, db
from models import Product

with app.app_context():
    # Add products
    product1 = Product(name='Wayward Compass', price=50, description='Whispers its location to the bearer whenever a map is open, allowing wanderers to pinpoint their current location.', stock=10)
    product2 = Product(name='Longnail', price=150, description='Increases the range of the bearer\'s nail, allowing them to strike foes from further away.', stock=20)
    product3 = Product(name='Heavy Blow', price=100, description='Increases the force of the bearer\'s nail, causing enemies to recoil further when hit', stock=15)
    product4 = Product(name='Quick Slash', price=200, description='Allows the bearer to slash much more rapidly with their nail.', stock=5)
    product5 = Product(name='Steady Body', price=50, description='Allows one to stay steady and keep attacking.', stock=8)
    
    # Add them to the session
    db.session.add(product1)
    db.session.add(product2)
    db.session.add(product3)
    db.session.add(product4)
    db.session.add(product5)
    
    # Commit the session to save the products in the database
    db.session.commit()

    print("Products added successfully!")