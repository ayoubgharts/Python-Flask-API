# Import the necessary modules from the Flask library
from flask import Flask, jsonify, request, render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Sample data to simulate a database with string IDs
items = [
    {"id": "firstname",   "content": "Ayoub", "endpoint": "/api/items/{id}"},
    {"id": "familyname",  "content": "Ghiouani", "endpoint": "/api/items/{id}"},
    {"id": "age",         "content": "28 years old", "endpoint": "/api/items/{id}"},
    {"id": "nationality", "content": "Moroccan", "endpoint": "/api/items/{id}"},
    {"id": "email",       "content": "ayoubgharts@gmail.com", "endpoint": "/api/items/{id}"},
    {"id": "address",     "content": "Fez, Morocco", "endpoint": "/api/items/{id}"},
    {"id": "frontend",    "content": "HTML/CSS, Javascript, React, Git/Github, Next.js, Bootstrap", "endpoint": "/api/items/{id}"},
    {"id": "backend",     "content": "PHP, mysql, PostgreSQL, Python, Flask, NodeJS", "endpoint": "/api/items/{id}"},
]

# Update each item's 'endpoint' field dynamically
for item in items:
    item['endpoint'] = item['endpoint'].format(id=item['id'])

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

    # Update the 'endpoint' field for the new item
    new_item['endpoint'] = f"/api/items/{new_item['id']}"
    
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

# Custom error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    # Render the custom 404.html template located in the 'templates' folder
    return render_template('404.html'), 404

# Start the web server when this file is run
if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for easier error tracking
