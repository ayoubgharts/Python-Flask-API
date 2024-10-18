# Import the necessary modules from the Flask library
from flask import Flask, jsonify, request, render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Sample data to simulate a database with string IDs
items = [
    {"id": "firstname", "First Name": "Ayoub"},
    {"id": "familyname", "Family Name": "Ghiouani"},
    {"id": "age", "Age": "28 years old"},
    {"id": "ntl", "Nationality": "Moroccan"},
    {"id": "email", "Adrress Email": "ayoubgharts@gmail.com"},
]

# Define a route for the docs
@app.route('/docs')
def docs():
    # Render the docs.html template located in the 'templates' folder
    return render_template('docs.html')

# Define a route to get all items and render them in an HTML template
@app.route('/api/items', methods=['GET'])
def get_items():
    # Render the items.html template and pass the items list to it
    return render_template('items.html', items=items)

# Define a route to get a specific item by its string ID
@app.route('/api/items/<string:item_id>', methods=['GET'])
def get_item(item_id):
    # Find the item with the matching string ID
    item = next((item for item in items if item["id"] == item_id), None)
    
    # If the item exists, render the item.html template; otherwise, render the 404.html template
    if item:
        return render_template('item.html', item=item)
    return render_template('404.html'), 404

# Define a route to add a new item
@app.route('/api/items', methods=['POST'])
def add_item():
    # Get the new item data from the request body
    new_item = request.json
    
    # Ensure the new item's ID is a string
    if not isinstance(new_item["id"], str):
        return jsonify({"error": "ID must be a string"}), 400

    # Append the new item to the items list
    items.append(new_item)
    
    # Return the newly added item with a 201 Created status code
    return jsonify(new_item), 201

# Define a route for the homepage
@app.route('/')
def home():
    # Render the index.html template located in the 'templates' folder
    # and pass the items list to show available IDs
    return render_template('index.html', items=items)

# Start the web server when this file is run
if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for easier error tracking
