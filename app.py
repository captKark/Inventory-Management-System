from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

inventory = []

@app.route('/')
def index():
    return render_template('index.html', inventory=inventory)

@app.route('/add', methods=['POST'])
def add_item():
    item_name = request.form.get('name')
    quantity = request.form.get('quantity')
    price = request.form.get('price')

    inventory.append({'name': item_name, 'quantity': quantity, 'price': price})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
