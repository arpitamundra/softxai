from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/payment', methods=['POST'])
def payment():
    # Get form inputs
    cc_number = request.form['cc_number']
    cc_exp = request.form['cc_exp']
    cc_cvv = request.form['cc_cvv']

    # URL for the JPMorgan Chase API
    # url = "https://api-mock.payments.jpmorgan.com/v1/checkout/intent"
    #
    # # Headers for the request
    # headers = {
    #     "Accept": "application/json",
    #     "Content-Type": "application/json",
    #     "merchantId": "998482157630",
    #     "requestId": "993264242060"
    # }
    #
    # # JSON payload for the request
    # data = {
    #     "currencyCode": "USD",
    #     "merchantOrderNumber": "X1G5VZMxplIm1tRRcrC85o",
    #     "checkoutOptions": {
    #         "authorization": {
    #             "authorizationType": "AUTH_METHOD_CART_AMOUNT"
    #         },
    #         "capture": {
    #             "captureMethod": "CAPTURE_METHOD_MANUAL"
    #         }
    #     },
    #     "cart": {
    #         "totalTransactionAmount": 1000
    #     }
    # }
    #
    # # Perform the POST request
    # response = requests.post(url, headers=headers, data=json.dumps(data))
    #
    # # Handle the API response
    # if response.status_code == 200:
    #     return "Payment successful"
    # else:
    #     return "Payment failed"

    url = "https://api-mock.payments.jpmorgan.com/api/v2/payments"


    # headers = {
    #     "Content-Type": "application/json",
    #     "Authorization": "Bearer YOUR_API_KEY"
    # }
    headers = {
        "Content-Type": "application/json",
        # "Authorization": "Bearer YOUR_API_KEY",
        "merchant-id":"991234567890",
        "request-id":"10cc0270-7bed-11e9-a188-1763956dd7f6"

    }

    data = {
      "captureMethod": "NOW",
      "amount": 1234,
      "currency": "USD",
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
          "accountNumber": cc_number,
          "expiry": {
            "month": cc_exp.split("/")[0],
            "year": cc_exp.split("/")[-1]
          },
          "isBillPayment": True
        }
      },
      "initiatorType": "CARDHOLDER",
      "accountOnFile": "NOT_STORED",
      "isAmountFinal": True
    }
    # if data["paymentMethodType"]["card"]["expiry"]["year"] < 2018:
    #     return "Card expiry year must be greater than or equal to 2018."

    # response = requests.post(url, headers=headers, json=data)
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print("Payment successful.")
        # return response.json()
        return "Payment successful."
    else:
        print("Payment failed.")
        return "Payment failed."



if __name__ == '__main__':
    app.run(port=7000)

