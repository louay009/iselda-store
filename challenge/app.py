from flask import Flask, render_template
from models import db
from config import Config
from flask import Response, request, session
from lxml import etree as ET
from models import Product
from flask_migrate import Migrate
from io import BytesIO

app = Flask(__name__)

# Load configuration settings from Config class
app.config.from_object(Config)
app.secret_key = 'theabyss'
migrate = Migrate(app, db)
# Initialize the database with the Flask app
db.init_app(app)

@app.route('/products.xml')
def products_xml():
    # Create the root element
    root = ET.Element('store')

    # Query the products from the database
    products = Product.query.all()
    
    # Loop through products and add them to the XML
    for product in products:
        product_element = ET.SubElement(root, 'product')
        
        name = ET.SubElement(product_element, 'name')
        name.text = product.name
        
        price = ET.SubElement(product_element, 'price')
        price.text = str(product.price)
        
        description = ET.SubElement(product_element, 'description')
        description.text = product.description
        
        stock = ET.SubElement(product_element, 'stock')
        stock.text = str(product.stock)
        
    # Convert the XML tree to a string
    xml_data = ET.tostring(root, encoding='utf-8', method='xml')

    # Return the XML as a response
    return Response(xml_data, mimetype='application/xml')


@app.route('/')
def home():

    if 'bearer' not in session:
        session['bearer'] = "hollowknight"
    # Dynamically generate the XML
    tree = ET.ElementTree(ET.fromstring(products_xml().data))  # Fetch the XML dynamically
    root = tree.getroot()

    # Extract products from the XML
    products = []
    products = Product.query.all()
    return render_template('home.html', products=products)

#product_info route
@app.route('/product_info', methods=['GET'])
def product_info():
    product_id = request.args.get('id')  # Get the product ID from the query string

    if product_id:
        product = Product.query.filter_by(id=product_id).first()
        if product:
            return render_template('product_info.html', product=product)
        else:
            return "Product not found", 404
    else:
        return "No product ID provided", 400
     



@app.route('/check_stock', methods=['POST'])
def check_stock():
    # Check the session token
    if 'bearer' not in session or session['bearer'] != 'paleking':
        return "welcome my knight :) but only the paleking is allowed to check the stock", 403
    # Get the XML request data
    xml_data = request.data.decode('utf-8')
    
    try:
  # Enable XInclude in the parser
                # Create an XML parser with XInclude support
        parser = ET.XMLParser(load_dtd=True, resolve_entities=True)
        
        # Parse the XML data and load it into an ElementTree
        tree = ET.parse(BytesIO(xml_data.encode('utf-8')), parser=parser)
        
        # Process XInclude elements
        tree.xinclude()
        
        # Get the root element and find the product_id
        root = tree.getroot()
        product_id = root.find('product_id').text
        product = Product.query.get(product_id)

        if product:
            stock_info = f"Stock for Product {product.name} : {product.stock} units left."
        else:
            stock_info = f"Product with ID {product_id} not found."

        return stock_info, 200

    except ET.XMLSyntaxError as e:
        print("Parse Error:", e)
        return "Error parsing XML", 400

if __name__ == '__main__':
    app.run(debug=True)