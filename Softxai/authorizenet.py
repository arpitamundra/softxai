from datetime import datetime, timedelta
from decimal import Decimal
import os

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *

# Initialize the Authorize.Net gateway
authorize_gateway = AuthorizePaymentGateway()

# 1. Setup
# Set the required environment variables
os.environ["AUTHORIZE_LOGIN_ID"] = "your_authorize_login_id"
os.environ["AUTHORIZE_TRANSACTION_ID"] = "your_authorize_transaction_id"

# 2. Create a Customer Profile
customer_type = "individual"  # or "organisation"
customer_id = "1234"  # Replace with your customer ID
status, message, response = authorize_gateway.create_customer_profile(
    customer_type=customer_type, customer_id=customer_id
)
if status:
    customer_profile_id = response["customer_profile_id"]
    print(f"Customer Profile ID: {customer_profile_id}")
else:
    print(f"Error: {message}")

# 3. Create a Payment Profile
card_number = "4111111111111111"
card_exp_date = "2025-12"
status, message, response = authorize_gateway.create_customer_payment_profile(
    customer_profile_id=customer_profile_id,
    card_number=card_number,
    card_exp_date=card_exp_date,
)
if status:
    customer_payment_profile_id = response["customer_payment_profile_id"]
    print(f"Customer Payment Profile ID: {customer_payment_profile_id}")
else:
    print(f"Error: {message}")

# 4. Charge a Card
card_code = "123"
invoice_number = "INV-1234"
amount = Decimal("10.99")
status, message, response = authorize_gateway.charge_card(
    card_number=card_number,
    card_exp_date=card_exp_date,
    card_code=card_code,
    invoice_number=invoice_number,
    amount=amount,
    customer_profile_id=customer_profile_id,
)
if status:
    trans_id = response["transId"]
    print(f"Transaction ID: {trans_id}")
else:
    print(f"Error: {message}")

# 5. Charge a Customer Payment Profile
status, message, response = authorize_gateway.charge_customer_payment_profile(
    payment_profile_id=customer_payment_profile_id,
    invoice_number=invoice_number,
    amount=amount,
    customer_profile_id=customer_profile_id,
)
if status:
    trans_id = response["transId"]
    print(f"Transaction ID: {trans_id}")
else:
    print(f"Error: {message}")

# 6. Refund a Transaction
merchant_customer_id = "CUST-1234"
status, message, response = authorize_gateway.refund_transaction(
    trans_id=trans_id,
    merchant_customer_id=merchant_customer_id,
    card_exp_date=card_exp_date,
    card_number=card_number,
    amount=amount,
)
if status:
    refund_trans_id = response["trans_id"]
    print(f"Refund Transaction ID: {refund_trans_id}")
else:
    print(f"Error: {message}")

# 7. Get Transaction Details
status, message, response = authorize_gateway.get_transaction_details(transId=trans_id)
if status:
    print("Transaction Details:")
    print(response)
else:
    print(f"Error: {message}")

# 8. Get Subscription Details
subscription_id = "12345678"  # Replace with your subscription ID
status, message, response = authorize_gateway.get_subscription(subscriptionId=subscription_id)
if status:
    print("Subscription Details:")
    print(response)
else:
    print(f"Error: {message}")

# 9. Delete a Payment Profile
status, message, response = authorize_gateway.delete_customer_payment_profile(
    customer_profile_id=customer_profile_id,
    customer_payment_profile_id=customer_payment_profile_id,
)
if status:
    print(f"Payment Profile Deleted: {message}")
else:
    print(f"Error: {message}")

# 10. Update a Payment Profile
new_card_number = "4007000000027"
new_card_exp_date = "2026-01"
status, message, response = authorize_gateway.update_customer_payment_profile(
    customer_profile_id=customer_profile_id,
    customer_payment_profile_id=customer_payment_profile_id,
    card_exp_date=new_card_exp_date,
    card_number=new_card_number,
)
if status:
    print(f"Payment Profile Updated: {message}")
else:
    print(f"Error: {message}")

# 11. Create a Shipping Address
shipping_address = {
    "firstName": "John",
    "lastName": "Doe",
    "address": "123 Main St",
    "city": "Anytown",
    "state": "CA",
    "zip": "12345",
    "country": "USA",
    "phoneNumber": "555-1234",
}
status, message, response = authorize_gateway.create_customer_shipping_address(
    customer_profile_id=customer_profile_id, address=shipping_address
)
if status:
    customer_address_id = response["customer_address_id"]
    print(f"Customer Address ID: {customer_address_id}")
else:
    print(f"Error: {message}")

# 12. Get a Shipping Address
status, message, response = authorize_gateway.get_customer_shipping_address(
    customer_profile_id=customer_profile_id, customer_address_id=customer_address_id
)
if status:
    print("Shipping Address:")
    print(response)
else:
    print(f"Error: {message}")

# 13. Get a Hosted Profile Page
return_url = "https://www.example.com/return"
status, message, response = authorize_gateway.get_hosted_profile_page(
    customer_profile_id=customer_profile_id, return_url=return_url
)
if status:
    token = response["token"]
    print(f"Hosted Profile Page Token: {token}")
else:
    print(f"Error: {message}")

# 14. Get Customer Profile IDs
status, message, response = authorize_gateway.get_customer_profile_ids()
if status:
    print(f"Customer Profile IDs synced: {message}")
else:
    print(f"Error: {message}")

# 15. Void a Transaction
status, message, response = authorize_gateway.void_transaction(transId=trans_id)
if status:
    print(f"Transaction Voided: {message}")
    print(response)
else:
    print(f"Error: {message}")