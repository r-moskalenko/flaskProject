from flask import Flask, render_template
from routes import routes
import logging

app = Flask(__name__)
app.register_blueprint(routes)

# Configure Flask logging
app.logger.setLevel(logging.DEBUG)  # Set log level to DEBUG
handler = logging.FileHandler('app.log')  # Log to a file
app.logger.addHandler(handler)


@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template("market.html", items=items)


@app.route('/about/<username>')
def about_page(username):
    return f'<h1> this is the about page of {username} </h1>'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
