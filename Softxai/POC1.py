from flask import Flask, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__)

# Mock API endpoints
create_payment_url = "https://api-mock.payments.jpmorgan.com/api/v2/payments"
# get_payment_url = "https://api-mock.payments.jpmorgan.com/api/v2/payments"
# get_payment_url = f"https://api-mock.payments.jpmorgan.com/api/v2/payments/{payment_id}"
refund_payment_url = "https://api-mock.payments.jpmorgan.com/api/v2/refunds"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_payment', methods=['POST'])
def create_payment():
    # data = request.form.to_dict()
    amount = request.form['amount']
    currency = request.form['currency']
    card_number = request.form['card_number']
    expiry_month = request.form['expiry_month']
    expiry_year = request.form['expiry_year']
    cvv = request.form['cvv']
    headers = {
        "Content-Type": "application/json",
        # "Authorization": "Bearer YOUR_API_KEY",
        "merchant-id": "991234567890",
        "request-id": "10cc0270-7bed-11e9-a188-1763956dd7f6"

    }
    data = {
        "captureMethod": "NOW",
        "amount": amount,
        "currency": currency,
        "merchant": {
            "merchantSoftware": {
                "companyName": "Payment Company",
                "productName": "Application Name",
                "version": "1.235"
            },
            "merchantCategoryCode": "4899"
        },
        "paymentMethodType": {
            "card": {
                "accountNumber": card_number,
                "expiry": {
                    "month": expiry_month,
                    "year": expiry_year
                },
                "isBillPayment": True
            }
        },
        "initiatorType": "CARDHOLDER",
        "accountOnFile": "NOT_STORED",
        "isAmountFinal": True
    }

    response = requests.post(create_payment_url, headers=headers, json=data)
    if response.status_code == 200:
        print(response.json())
        return redirect(url_for('payment_success'))
    else:
        return redirect(url_for('payment_error'))



# @app.route('/get_payment')
# def get_payment():
#     return render_template('payment_details.html')

@app.route('/get_payment', methods=['GET'])
def get_payment_details():
    payment_id = request.args.get('payment_id')
    if payment_id:
        payment_details = get_payment_details_from_api(payment_id)
        if payment_details:
            print(payment_details)
            # return render_template('payment_details.html', payment=payment_details)
            return render_template('payment_details.html', payment_id=payment_details['transactionId'],
                                   amount=payment_details['amount'], currency=payment_details['currency'],
                                   merchant=payment_details['merchant'])

    return redirect(url_for('payment_error'))

def get_payment_details_from_api(payment_id):
    url = f"https://api-mock.payments.jpmorgan.com/api/v2/captures/{payment_id}"
    headers = {"Accept": "application/json", "merchant-id": "991234567890", "minorVersion": "",'request-id': '10cc0270-7bed-11e9-a188-1763956dd7f6'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None
# @app.route('/get_payment', methods=['GET'])
# def get_payment():
#     # params = {"requestIdentifier": "14cc0270-7bed-11e9-a188-1763956dd7f6"}
#     params = {"id": request.form['id']}
#     get_payment_url = f"https://api-mock.payments.jpmorgan.com/api/v2/payments/{id}"
#     headers = {"Content-Type": "application/json","merchant-id": "991234567890",}
#     response = requests.get(get_payment_url, headers=headers, params=params)
#     if response.status_code == 200:
#         return render_template('get_payment.html', payment=response.json())
#     else:
#         return redirect(url_for('payment_error'))

@app.route('/refund_payment', methods=['POST'])
def refund_payment():
    data = request.form.to_dict()
    headers = {"Content-Type": "application/json"}
    response = requests.post(refund_payment_url, headers=headers, json=data)
    if response.status_code == 200:
        return redirect(url_for('refund_success'))
    else:
        return redirect(url_for('refund_error'))

@app.route('/payment_success')
def payment_success():
    return render_template('payment_success.html')

@app.route('/payment_error')
def payment_error():
    return render_template('payment_error.html')

@app.route('/refund_success')
def refund_success():
    return render_template('refund_success.html')

@app.route('/refund_error')
def refund_error():
    return render_template('refund_error.html')

if __name__ == '__main__':
    app.run(port=9000)
