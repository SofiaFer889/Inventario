from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

amount = []
products = []
price = []

@app.route('/')
def index():
    return render_template('index.html', products=products, amount=amount, price=price)

@app.route('/add', methods=['POST'])
def add_product():
    if request.method == 'POST':
        addProduct = request.form['product']
        addAmount = int(request.form['amount'])
        addPrice = int(request.form['price'])

        products.append(addProduct)
        amount.append(addAmount)
        price.append(addPrice)

    return redirect(url_for('index'))

@app.route('/modify', methods=['POST'])
def modify_product():
    if request.method == 'POST':
        modifyProduct = request.form['product']
        modifyAmount = int(request.form['amount'])
        modifyPrice = int(request.form['price'])
        index = int(request.form['index'])

        products[index] = modifyProduct
        amount[index] = modifyAmount
        price[index] = modifyPrice

    return redirect(url_for('index'))

@app.route('/search', methods=['GET'])
def search_product():
    query = request.args.get('query')
    results = []

    for i in range(len(products)):
        if query.lower() in products[i].lower():
            results.append((products[i], amount[i], price[i]))

    return render_template('search_results.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)
