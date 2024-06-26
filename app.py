import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from pytz import timezone
from datetime import datetime

app = Flask(__name__)

def create_table():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS inventory
                  (id INTEGER PRIMARY KEY,
                   product TEXT,
                   amount INTEGER,
                   price INTEGER,
                   timestamp TIMESTAMP)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    create_table()
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM inventory')
    inventory = cursor.fetchall()
    conn.close()
    
    return render_template('index.html', inventory=inventory)

@app.route('/add', methods=['POST'])
def add_product():
    if request.method == 'POST':
        addProduct = request.form['product']
        addAmount = int(request.form['amount'])
        addPrice = int(request.form['price'])
        ar_timezone = timezone('America/Argentina/Buenos_Aires')
        ar_time = datetime.now(ar_timezone)
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO inventory (product, amount, price, timestamp) VALUES (?, ?, ?, ?)', (addProduct, addAmount, addPrice, ar_time))
        conn.commit()
        conn.close()
        
    return redirect(url_for('index'))

@app.route('/modify', methods=['POST'])
def modify_product():
    if request.method == 'POST':
        modifyProduct = request.form['product']
        modifyAmount = int(request.form['amount'])
        modifyPrice = int(request.form['price'])
        product_id = int(request.form['product_id'])
        ar_timezone = timezone('America/Argentina/Buenos_Aires')
        ar_time = datetime.now(ar_timezone)
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE inventory SET product=?, amount=?, price=?, timestamp=? WHERE id=?', (modifyProduct, modifyAmount, modifyPrice, ar_time, product_id))
        conn.commit()
        conn.close()

    return redirect(url_for('index'))

@app.route('/search', methods=['GET'])
def search_product():
    query = request.args.get('query')
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory WHERE product LIKE ?", ('%' + query + '%',))
    results = cursor.fetchall()
    conn.close()
    return render_template('search_results.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)
