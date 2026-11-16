# Import libraries
from flask import Flask, redirect, request, render_template, url_for

# Instantiate Flask functionality
app = Flask("CRUD operation")

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions=transactions)

# Create operation
@app.route("/add", methods = ["GET", "POST"])
def add_transaction():
    if request.method == "POST":
        transaction = {
            'id': len(transactions) + 1,
            'date': request.form['date'],
            'amount': int(request.form['amount'])
        }
            
        transactions.append(transaction)
        return redirect(url_for("get_transactions"))

    return render_template("form.html")

# Update operation
@app.route("/edit/<int:transaction_id>", methods = ["POST", "GET"])
def edit_transaction(transaction_id):

    transaction = next(
        t for t in transactions if t['id'] == transaction_id
    )
    if request.method == "POST":
            transaction['date'] =  request.form['date']
            transaction['amount'] = int(request.form['amount'])

            return redirect(url_for("get_transactions"))
    
    return render_template("edit.html", transaction=transaction)

# Delete operation
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    transaction = next(
        t for t in transactions if t['id'] == transaction_id
    )

    transactions.remove(transaction)
    return redirect(url_for("get_transactions"))

# Search operation
@app.route("/search", methods=["GET"])
def search_transaction():
    min_amount = request.args.get('min_amount', type=int)
    max_amount = request.args.get('max_amount', type=int)

    filtered_transactions = []

    if min_amount is not None and max_amount is not None:

        for t in transactions:
            if min_amount <= t['amount'] <= max_amount:
                filtered_transactions.append(t)


    return render_template("search.html", transactions=filtered_transactions)     