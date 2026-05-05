from flask import Flask, render_template, request, redirect, url_for
from repository.payment_repository import process_payment

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('payment'))

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    message = ""
    if request.method == 'POST':
        user_id = int(request.form['user_id'])
        merchant_id = int(request.form['merchant_id'])
        amount = float(request.form['amount'])
        message = process_payment(user_id, merchant_id, amount)
    return render_template('payment.html', message=message)

@app.errorhandler(404)
def not_found(error):
    return '''
    <h1>404 - Page Not Found</h1>
    <p>Available routes:</p>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/payment">Payment</a></li>
    </ul>
    ''', 404

if __name__ == '__main__':
    app.run(debug=True)
