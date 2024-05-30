#----------------- Create Tokan-------------------

import requests

url = "https://id.payments.jpmorgan.com/am/oauth2/alpha/access_token"

client_id = "d310e129-34c5-4237-a20d-d98e6ad7c51f"
client_secret = "jKkyC3rkUb7Pg_HKcr4nRxUF1foxxU8giBABDADNmNmg5p1GCn7N7rEKxeAMNDfJGF-A91ASD4I0U1oTaJaoyA"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "client_credentials",
    "scope": "jpm:payments:sandbox"
}

response = requests.post(url, headers=headers, data=data, auth=(client_id, client_secret))


if response.status_code == 200:
    print("Access token Create successful.")
    print(response.json())
else:
    print("Access token request failed.")
    print(f"Status code: {response.status_code}")
    print(response.text)


#---------------- Create Payment


import requests


# url = "https://api.payments.jpmorgan.com/api/v2/payments"
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
      "accountNumber": "4012000033330026",
      "expiry": {
        "month": 5,
        "year": 2027
      },
      "isBillPayment": True
    }
  },
  "initiatorType": "CARDHOLDER",
  "accountOnFile": "NOT_STORED",
  "isAmountFinal": True
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Payment successful.")
    print(response.json())
else:
    print("Payment failed.")


#----- ---- Get Payment-----------

import requests

url = "https://api-mock.payments.jpmorgan.com/api/v2/payments"

params = {
    "requestIdentifier": "14cc0270-7bed-11e9-a188-1763956dd7f6"
}

headers = {
    "Content-Type": "application/json",
    # "Authorization": "Bearer YOUR_API_KEY",
    "merchant-id": "991234567890",
    "request-id":"10cc0270-7bed-11e9-a188-1763956dd7f6"

}

response = requests.get(url, headers=headers, params=params)


if response.status_code == 200:
    print("Request successful.")
    print(response.json())
else:
    print("Request failed.")
    print(f"Status code: {response.status_code}")
    print(response.text)
#---------------Update Payment
import requests

url = "https://api-mock.payments.jpmorgan.com/api/v2/payments/{id}"

params = {
    "id": "22222222-7bea-11e9-a188-1763956dd7f6"
}

headers = {
    "Content-Type": "application/json",
    # "Authorization": "Bearer YOUR_API_KEY",
    "merchant-id": "991234567890",
    "request-id":"10cc0270-7bed-11e9-a188-1763956dd7f6"

}
data={
  "captureMethod": "NOW"
}

response = requests.patch(url, headers=headers, json=data)


if response.status_code == 200:
    print("Payment update successful.")
    print(response.json())
else:
    print("Payment update failed.")
    print(f"Status code: {response.status_code}")
    print(response.text)




import requests
import json

# URL for the JPMorgan Chase API
url = "https://api-mock.payments.jpmorgan.com/api/v2/payments"

# Headers for the request
# Note: You need to include your actual Authorization header here
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJraWQiOiJJR05rNSthbHVNdy9FeHQ4ejc5Wmg5ZVpZL0U9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJkMzEwZTEyOS0zNGM1LTQyMzctYTIwZC1kOThlNmFkN2M1MWYiLCJjdHMiOiJPQVVUSDJfU1RBVEVMRVNTX0dSQU5UIiwiYXVkaXRUcmFja2luZ0lkIjoiYTU3YzM5YjMtNzJlMC00OTYxLTgwOGUtMzg2YjM1MWJlODFiLTkyNjIxODQiLCJzdWJuYW1lIjoiZDMxMGUxMjktMzRjNS00MjM3LWEyMGQtZDk4ZTZhZDdjNTFmIiwiaXNzIjoiaHR0cHM6Ly9pZC5wYXltZW50cy5qcG1vcmdhbi5jb206NDQzL2FtL29hdXRoMiIsInRva2VuTmFtZSI6ImFjY2Vzc190b2tlbiIsInRva2VuX3R5cGUiOiJCZWFyZXIiLCJhdXRoR3JhbnRJZCI6Il8tSVBaLTFJT1lUaWRtMnp4enQ5ZS1sbTdFVSIsImF1ZCI6ImQzMTBlMTI5LTM0YzUtNDIzNy1hMjBkLWQ5OGU2YWQ3YzUxZiIsIm5iZiI6MTcxNDAyNzcwOCwiZ3JhbnRfdHlwZSI6ImNsaWVudF9jcmVkZW50aWFscyIsInNjb3BlIjpbImpwbTpwYXltZW50czpzYW5kYm94Il0sImF1dGhfdGltZSI6MTcxNDAyNzcwOCwicmVhbG0iOiIvYWxwaGEiLCJleHAiOjE3MTQwMzEzMDgsImlhdCI6MTcxNDAyNzcwOCwiZXhwaXJlc19pbiI6MzYwMCwianRpIjoiMnhzUjZleTd6S3BqRG5jaXBwNFd2NHRSX3VjIn0.IiOG3YWHMxHcvGSl7-_byWXHrju95geqkp5ggpaSlKorsy2VbA8aQs7xcb3UgpUTmGVBdNYDnhQ0KtSW3MEqf2MqMzRfuj7b6rrBsS0daLmalTy5lAsRe4YZsAtJKEDmOspG_L4ATGk_0TedpYs1K1WRXzMM0qV5UOG636uRmHD77yff44iIi76jPo0epC3yrdEW3uq6d5VQlndpngqQpE8h8dEP3mTwA1ykDgafr31ZLM2R2pReJ22j0IHXgnfeb0PJxf3AD_7cDSt8iACuJfDb1TnMqrMMwwITeMFVvqDEQm4is26e2jPkxn_KdEhaVPj3vGNpp3Qwpw0t_8Zbkw"
}

# JSON payload for the request
data = {
    "version": "4.3",
    "transType": "AC",
    "merchant": {
        "bin": "000001",
        "terminalID": "001"
    },
    "order": {
        "orderID": "akbk26",
        "comments": "Website payments2",
        "industryType": "EC",
        "amount": "1000"
    },
    "paymentInstrument": {
        "card": {
            "cardBrand": "MC",
            "ccAccountNum": "5454545454545454",
            "ccExp": "222506"
        }
    },
    "profile": {
        "addProfileFromOrder": "S",
        "customerRefNum": "myprofile01",
        "profileOrderOverideInd": "NO"
    }
}

# Perform the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Handle the response
if response.status_code == 200:
    print("Payment request successful.")
    print(response.json())
else:
    print("Payment request failed.")
    print(f"Status code: {response.status_code}")
    print(response.text)



import requests
import json

# URL for the JPMorgan Chase API
url = "https://api-mock.payments.jpmorgan.com/api/v2/profile/"

# Headers for the request
# Note: You need to include your actual Authorization header here
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN_HERE"
}

# JSON payload for the request
data = {
    "version": "4.3",
    "merchant": {
        "bin": "000001",
        "terminalID": "001"
    },
    "order": {
        "customerProfileFromOrderInd": "S",
        "customerProfileOrderOverideInd": "NO",
        "orderDefaultAmount": "500"
    },
    "paymentInstrument": {
        "customerAccountType": "CC",
        "card": {
            "ccAccountNum": "5454545454545454",
            "ccExp": "202506"
        }
    },
    "profile": {
        "customerName": "John Smith",
        "customerAddress1": "123 Main St",
        "customerCity": "Tampa",
        "customerState": "FL",
        "customerZIP": "33601",
        "customerEmail": "email@email.com",
        "customerPhone": "1234561234",
        "customerCountryCode": "US",
        "customerRefNum": "myprofile10"
    }
}

# Perform the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Handle the response
if response.status_code == 200:
    print("Profile creation/update successful.")
    print(response.json())
else:
    print("Profile creation/update failed.")
    print(f"Status code: {response.status_code}")
    print(response.text)


import requests

# URL for the JPMorgan Chase API
url = "https://api-mock.payments.jpmorgan.com/v1/checkout/notifications"

# Query parameters
params = {
    "periodStart": "2023-04-05T00:00:00.000Z",
    "periodEnd": "2023-04-06T00:00:00.000Z"
}

# Headers for the request
headers = {
    "Accept": "application/json",
    "MERCHANTID": "991234567890"
}

# Perform the GET request
response = requests.get(url, params=params, headers=headers)

# Handle the response
if response.status_code == 200:
    print("Request successful.")
    print(response.json())
else:
    print("Request failed.")
    print(f"Status code: {response.status_code}")
    print(response.text)


import requests

# URL for the JPMorgan Chase API
url = "https://api-mock.payments.jpmorgan.com/v1/checkout/notifications/receive"

# Query parameters
params = {
    "maxNumberMessages": 10,
    "timeoutMs": 300
}

# Headers for the request
headers = {
    "Accept": "application/json",
    "MERCHANTID": "998482157632"
}

# Perform the GET request
response = requests.get(url, params=params, headers=headers)

# Handle the response
if response.status_code == 200:
    print("Request successful.")
    print(response.json())
else:
    print("Request failed.")
    print(f"Status code: {response.status_code}")
    print(response.text)




import requests
import json

# URL for the JPMorgan Chase API
url = "https://api-mock.payments.jpmorgan.com/api/v2/refunds"

# Headers for the request
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "merchant-id": "991234567890",
    "minorVersion": "", # Ensure this is set to the correct minor version if required
    "request-id": "10cc0270-7bed-11e9-a188-1763956dd7f6"
}

# JSON payload for the request
data = {
    "merchant": {
        "merchantSoftware": {
            "companyName": "Payment Company",
            "productName": "Application Name",
            "version": "1.235"
        }
    },
    "amount": 1234,
    "currency": "USD",
    "initiatorType": "CARDHOLDER",
    "accountOnFile": "NOT_STORED",
    "paymentMethodType": {
        "card": {
            "accountNumber": "4012000033330026",
            "expiry": {
                "month": 4,
                "year": 2025
            }
        }
    }
}

# Perform the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Handle the response
if response.status_code == 200:
    print("Refund request successful.")
    print(response.json())
else:
    print("Refund request failed.")
    print(f"Status code: {response.status_code}")
    print(response.text)

import requests, base64

url = "https://orbitalvar1.chasepaymentech.com/gwapi/v4/gateway/profile"
response = requests.post(url)

print("[", response.status_code, "] -", response.text)

#
# import requests, base64
#
# url = "https://orbitalvar1.chasepaymentech.com/gwapi/v4/gateway/profile"
# payload = {  "version": "5.2",  "merchant": {    "bin": "000001"  },  "order": {    "customerProfileOrderOverideInd": "NO",    "customerProfileFromOrderInd": "A",    "orderDefaultAmount": "1050"  },  "paymentInstrument": {    "customerAccountType": "CC",    "card": {      "ccAccountNum": "5454545454545454",      "ccExp": "202206"    }  },  "profile": {    "customerName": "Customer Name",    "customerAddress1": "123 Main St",    "customerCity": "Tampa",    "customerState": "FL",    "customerZIP": "123456",    "customerEmail": "email@email.com",    "customerPhone": "1234561234",    "customerCountryCode": "US"  }}
# headers = {"orbitalConnectionUsername":"d310e129-34c5-4237-a20d-d98e6ad7c51f","orbitalConnectionPassword":"jKkyC3rkUb7Pg_HKcr4nRxUF1foxxU8giBABDADNmNmg5p1GCn7N7rEKxeAMNDfJGF-A91ASD4I0U1oTaJaoyA","merchantID":"991234567890"}
# response = requests.post(url, json=payload, headers=headers, cert=("certificate.cer","keyfile.key"))
#
# print("[", response.status_code, "] -", response.text)

# #---------------Create Profile
# import requests, base64
#
# url = "https://orbitalvar1.chasepaymentech.com/gwapi/v4/gateway/profile"
# payload = {
#   "version": "5.2",
#   "merchant": {
#     "bin": "000001"
#   },
#   "order": {
#     "customerProfileOrderOverideInd": "NO",
#     "customerProfileFromOrderInd": "A",
#     "orderDefaultAmount": "1050"
#   },
#   "paymentInstrument": {
#     "customerAccountType": "CC",
#     "card": {
#       "ccAccountNum": "5454545454545454",
#       "ccExp": "202206"
#     }
#   },
#   "profile": {
#     "customerName": "Customer Name",
#     "customerAddress1": "123 Main St",
#     "customerCity": "Tampa",
#     "customerState": "FL",
#     "customerZIP": "123456",
#     "customerEmail": "email@email.com",
#     "customerPhone": "1234561234",
#     "customerCountryCode": "US"
#   }
# }
# headers = {"orbitalConnectionUsername":"d310e129-34c5-4237-a20d-d98e6ad7c51f","orbitalConnectionPassword":"jKkyC3rkUb7Pg_HKcr4nRxUF1foxxU8giBABDADNmNmg5p1GCn7N7rEKxeAMNDfJGF-A91ASD4I0U1oTaJaoyA","merchantID":"991234567890"}
# response = requests.post(url, json=payload, headers=headers,cert=("certificate.cer","keyfile.key"))
#
# print("[", response.status_code, "] -", response.text)
#
# #----------------------Update PRofile
# import requests, base64
#
# url = "https://orbitalvar1.chasepaymentech.com/gwapi/v4/gateway/profile"
# payload = {
#   "version": "5.2",
#   "merchant": {
#     "bin": "000001"
#   },
#   "paymentInstrument": {
#     "card": {
#       "ccAccountNum": "5454545454545454",
#       "ccExp": "202206"
#     }
#   },
#   "profile": {
#     "customerRefNum": "12345678",
#     "customerName": "Customer Name",
#     "customerAddress1": "123 Main St",
#     "status": "I"
#   }
# }
# headers = {"orbitalConnectionUsername":"d310e129-34c5-4237-a20d-d98e6ad7c51f","orbitalConnectionPassword":"jKkyC3rkUb7Pg_HKcr4nRxUF1foxxU8giBABDADNmNmg5p1GCn7N7rEKxeAMNDfJGF-A91ASD4I0U1oTaJaoyA","merchantID":"991234567890"}
# response = requests.post(url, json=payload, headers=headers)
#
# print("[", response.status_code, "] -", response.text)
#
#



import requests
import json

# URL for the JPMorgan Chase API
url = "https://api-mock.payments.jpmorgan.com/v1/checkout/intent"

# Headers for the request
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "merchantId": "998482157630",
    "requestId": "993264242060"
}

# JSON payload for the request
data = {
    "currencyCode": "USD",
    "merchantOrderNumber": "X1G5VZMxplIm1tRRcrC85o",
    "checkoutOptions": {
        "authorization": {
            "authorizationType": "AUTH_METHOD_CART_AMOUNT"
        },
        "capture": {
            "captureMethod": "CAPTURE_METHOD_MANUAL"
        }
    },
    "cart": {
        "totalTransactionAmount": 1000
    }
}

# Perform the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Handle the response
if response.status_code == 200:
    print("Request successful.")
    print(response.json())
else:
    print("Request failed.")
    print(f"Status code: {response.status_code}")
    print(response.text)


import requests

# URL for the JPMorgan Chase API
url = "https://api-mock.payments.jpmorgan.com/api/v2/payments/66666666-7bea-11e9-a188-1763956dd7f6"

# Headers for the request
headers = {
    "Accept": "application/json",
    "merchant-id": "998482157632",
    "minorVersion": "" # Ensure this is set to the correct minor version if required
}

# Perform the GET request
response = requests.get(url, headers=headers)

# Handle the response
if response.status_code == 200:
    print("Request successful.")
    print(response.json())
else:
    print("Request failed.")
    print(f"Status code: {response.status_code}")
    print(response.text)


import requests
import json

# Define the endpoint URL
ENDPOINT = "https://api-mock.payments.jpmorgan.com/v1/checkout/intent"

# Define the access token
accessToken = "eyJ0eXAiOiJKV1QiLCJraWQiOiJJR05rNSthbHVNdy9FeHQ4ejc5Wmg5ZVpZL0U9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJkMzEwZTEyOS0zNGM1LTQyMzctYTIwZC1kOThlNmFkN2M1MWYiLCJjdHMiOiJPQVVUSDJfU1RBVEVMRVNTX0dSQU5UIiwiYXVkaXRUcmFja2luZ0lkIjoiYTU3YzM5YjMtNzJlMC00OTYxLTgwOGUtMzg2YjM1MWJlODFiLTkyNjIxODQiLCJzdWJuYW1lIjoiZDMxMGUxMjktMzRjNS00MjM3LWEyMGQtZDk4ZTZhZDdjNTFmIiwiaXNzIjoiaHR0cHM6Ly9pZC5wYXltZW50cy5qcG1vcmdhbi5jb206NDQzL2FtL29hdXRoMiIsInRva2VuTmFtZSI6ImFjY2Vzc190b2tlbiIsInRva2VuX3R5cGUiOiJCZWFyZXIiLCJhdXRoR3JhbnRJZCI6Il8tSVBaLTFJT1lUaWRtMnp4enQ5ZS1sbTdFVSIsImF1ZCI6ImQzMTBlMTI5LTM0YzUtNDIzNy1hMjBkLWQ5OGU2YWQ3YzUxZiIsIm5iZiI6MTcxNDAyNzcwOCwiZ3JhbnRfdHlwZSI6ImNsaWVudF9jcmVkZW50aWFscyIsInNjb3BlIjpbImpwbTpwYXltZW50czpzYW5kYm94Il0sImF1dGhfdGltZSI6MTcxNDAyNzcwOCwicmVhbG0iOiIvYWxwaGEiLCJleHAiOjE3MTQwMzEzMDgsImlhdCI6MTcxNDAyNzcwOCwiZXhwaXJlc19pbiI6MzYwMCwianRpIjoiMnhzUjZleTd6S3BqRG5jaXBwNFd2NHRSX3VjIn0.IiOG3YWHMxHcvGSl7-_byWXHrju95geqkp5ggpaSlKorsy2VbA8aQs7xcb3UgpUTmGVBdNYDnhQ0KtSW3MEqf2MqMzRfuj7b6rrBsS0daLmalTy5lAsRe4YZsAtJKEDmOspG_L4ATGk_0TedpYs1K1WRXzMM0qV5UOG636uRmHD77yff44iIi76jPo0epC3yrdEW3uq6d5VQlndpngqQpE8h8dEP3mTwA1ykDgafr31ZLM2R2pReJ22j0IHXgnfeb0PJxf3AD_7cDSt8iACuJfDb1TnMqrMMwwITeMFVvqDEQm4is26e2jPkxn_KdEhaVPj3vGNpp3Qwpw0t_8Zbkw"

# Define the request ID and merchant ID
# requestId = "merchantOrderReference"
# merchantId = "merchantId"
merchantId = "998482157630",
requestId = "993264242060"

# Define the session request payload
sessionRequestPayload = {
        "currencyCode": "USD",
        "merchantOrderNumber": "X1G5VZMxplIm1tRRcrC85o",
        "checkoutOptions": {
            "authorization": {
                "authorizationType": "AUTH_METHOD_CART_AMOUNT"
            },
            "capture": {
                "captureMethod": "CAPTURE_METHOD_NOW"
            }
        },
        "cart": {
            "totalTransactionAmount": 1000
        }
}

# Prepare the headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {accessToken}",
    "requestId": "993264242060",
    "merchantId": "998482157630"
}

# Prepare the body
body = json.dumps(sessionRequestPayload)

# Make the POST request
response = requests.post(ENDPOINT, headers=headers, data=body)

# Print the response
print(response.json())


import requests

url = "https://idag2.jpmorganchase.com/adfs/oauth2/token/"

# Body parameters
body_params = {
    "grant_type": "client_credentials",
    "client_id": "CC-105239-B041999-261550-PROD",
    "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
    "client_assertion": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVENDE5RTY4OUNGMzhBOTRGQjdFODU2M0QyODQwNkNGQTdCQ0IyNDgifQ.eyJqdGkiOiIxMjM0NSIsImlhdCI6MTcwODQwMzY2NSwiZXhwIjoxOTk2NDAzNjY1LCJhdWQiOiJodHRwczovL2lkYWcyLmpwbW9yZ2FuY2hhc2UuY29tL2FkZnMvb2F1dGgyL3Rva2VuIiwiaXNzIjoiQ0MtMTA1MjM5LUIwNDE5OTktMjYxNTUwLVBST0QiLCJzdWIiOiJDQy0xMDUyMzktQjA0MTk5OS0yNjE1NTAtUFJPRCJ9.eox6RboxPcIN_ISkOB3b3oxFYf8mz3K-QzF_YS7A4azlpnJ4ovoDc7SY3AHQXNNMeYZD-NpHjH-rDOicWmZQiX8gQzWaWHfcXrvXO9YUjFLn9fAaDNl3pVSDn8Q2gw83zxfpdbnhkBqGczaUNgCciwgTKgRy4u4DhJAmgFrVXCjtwvCWsAZ2F2wQ2jCP33O6PG6TSu4nXsksfHIqANBkXPLUPks_oJoairuOBBFSqAfI4p2nQztvnGXHMP1h8-jfOZbS8ZWVUiUFdcF8KkdzUlVveeYgkIj8XfSFy0hYnSlYBjc2FkXjTV2UjKFggkLDZhIsCdCe_mOME6GF6j0qZA",
    "resource": "JPMC:URI:RS-105239-85484-HelixAPIEntitlementsCAT-PROD"
}

# Sending POST request
response = requests.post(url, data=body_params)

# Print response
print(response.json())


#"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlCY3doSUVhaml0bWZQUERlY3E0UGdFVUo0OCIsImtpZCI6IjlCY3doSUVhaml0bWZQUERlY3E0UGdFVUo0OCJ9"


# import requests
#
# url = "https://merchant-api.checkout-cat.merchant.jpmorgan.com/v1/checkout/intent"
#
# # Headers
# headers = {
#     "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjVENDE5RTY4OUNGMzhBOTRGQjdFODU2M0QyODQwNkNGQTdCQ0IyNDgifQ.eyJqdGkiOiIxMjM0NSIsImlhdCI6MTcwODQwMzY2NSwiZXhwIjoxOTk2NDAzNjY1LCJhdWQiOiJodHRwczovL2lkYWcyLmpwbW9yZ2FuY2hhc2UuY29tL2FkZnMvb2F1dGgyL3Rva2VuIiwiaXNzIjoiQ0MtMTA1MjM5LUIwNDE5OTktMjYxNTUwLVBST0QiLCJzdWIiOiJDQy0xMDUyMzktQjA0MTk5OS0yNjE1NTAtUFJPRCJ9.eox6RboxPcIN_ISkOB3b3oxFYf8mz3K-QzF_YS7A4azlpnJ4ovoDc7SY3AHQXNNMeYZD-NpHjH-rDOicWmZQiX8gQzWaWHfcXrvXO9YUjFLn9fAaDNl3pVSDn8Q2gw83zxfpdbnhkBqGczaUNgCciwgTKgRy4u4DhJAmgFrVXCjtwvCWsAZ2F2wQ2jCP33O6PG6TSu4nXsksfHIqANBkXPLUPks_oJoairuOBBFSqAfI4p2nQztvnGXHMP1h8-jfOZbS8ZWVUiUFdcF8KkdzUlVveeYgkIj8XfSFy0hYnSlYBjc2FkXjTV2UjKFggkLDZhIsCdCe_mOME6GF6j0qZA",
#     "requestId": "14488937",
#     "merchantId": "996353459981",
#     "Content-Type": "application/json"
# }
#
# # Body parameters
# body_params = {
#     "currencyCode": "USD",
#     "merchantOrderNumber": "20-1155905",
#     "checkoutOptions": {
#         "authorization": {
#             "authorizationType": "AUTH_METHOD_CART_AMOUNT"
#         },
#         "capture": {
#             "captureMethod": "CAPTURE_METHOD_NOW"
#         },
#         "consumerProfileOptions": {
#             "isSaveConsumerProfile": False
#         }
#     },
#     "cart": {
#         "totalTransactionAmount": 21213,
#         "totalTaxAmount": "1313",
#         "lineItems": [
#             {
#                 "id": "1",
#                 "quantity": 1,
#                 "unitPrice": 19900,
#                 "name": "",
#                 "description": "",
#                 "imageUrl": ""
#             }
#         ]
#     },
#     "consumer": {
#         "phone": "",
#         "email": "",
#         "billingAddress": {
#             "recipientFullName": "",
#             "line1": "",
#             "line2": "",
#             "line3": "",
#             "city": "",
#             "state": "",
#             "country": "",
#             "postalCode": ""
#         }
#     }
# }
#
# # Sending POST request
# response = requests.post(url, headers=headers, json=body_params)
#
# # Print response
# print(response.json())

import requests

url = "https://merchant-api.checkout-cat.merchant.jpmorgan.com/v1/checkout/intent"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlCY3doSUVhaml0bWZQUERlY3E0UGdFVUo0OCIsImtpZCI6IjlCY3doSUVhaml0bWZQUERlY3E0UGdFVUo0OCJ9.eyJhdWQiOiJKUE1DOlVSSTpSUy0xMDUyMzktODU0ODQtSGVsaXhBUElFbnRpdGxlbWVudHNDQVQtUFJPRCIsImlzcyI6Imh0dHA6Ly9pZGEuanBtb3JnYW5jaGFzZS5jb20vYWRmcy9zZXJ2aWNlcy90cnVzdCIsImlhdCI6MTcxNDYyOTY3NiwibmJmIjoxNzE0NjI5Njc2LCJleHAiOjE3MTQ2NzI4NzYsIkpQTUNJZGVudGlmaWVyIjoiQjA0MTk5OSIsIlJvbGUiOlsiMTEwNDI5X0NIRUNLT1VUX01FUkNIX0FDQ0VTUy04NTQ4NC0xMDUyMzktUFJPRCIsIjEwMzI1N19QQVlNRU5UU19NRVJDSF9BQ0NFU1MtODU0ODQtMTA1MjM5LVBST0QiLCJIZWxpeEFQSUVudGl0bGVtZW50c0NBVC04NTQ4NC0xMDUyMzktUFJPRCIsIjEwMzAzMl9SRVBPUlRTX01FUkNIX0FDQ0VTUy04NTQ4NC0xMDUyMzktUFJPRCJdLCJDbGllbnRJUEFkZHJlc3MiOlsiMTY5LjIxLjQyLjg3IiwiMjcuNTguMTA1LjQ4IiwiMTY5LjIxLjc0LjIzMCJdLCJ1cG4iOiJCMDQxOTk5QEFELkpQTU9SR0FOQ0hBU0UuQ09NIiwiYXV0aG1ldGhvZCI6WyJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvYXV0aGVudGljYXRpb25tZXRob2QvdGxzY2xpZW50IiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2F1dGhlbnRpY2F0aW9ubWV0aG9kL3g1MDkiXSwiYXBwdHlwZSI6IkNvbmZpZGVudGlhbCIsImFwcGlkIjoiQ0MtMTA1MjM5LUIwNDE5OTktMjYxNTUwLVBST0QiLCJhdXRoX3RpbWUiOiIyMDI0LTA1LTAyVDA2OjAyOjE2Ljg2OVoiLCJ2ZXIiOiIxLjAifQ.JcvLjfNxQVLs5aTZs8Kj8sKdjKB7Q7JXV5q5mTO6RfAWwbo4q9W-I11RVuRgbWBcoVpm1ImEMTt_5FN4rVcMmzncBjazsk5A5p_wdw_TalEiV4u0TpBfDyq1r2sCYA90dyMKuYYRSgHpyNjOjaDPvBcyEuD6S3d38AMjmoPkjBSj0YHsohz8rGNYhFKEqgaaUHCBLn9cL0DzMYzHrCDNi-EbnXvBbUEQFtjUqpbsaSQHNqvEmYhLB2lFRhUuwPAn26YovsvGiPkZ4w8c6dvHIUNqcy9uNAtCptsrxROfqAwRxNPZjBgL9ktC8qmYy3zVzB2JL2nv6ty81J-BJ1EVcA"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "requestId": "1448888811", # random digit
    "merchantId": "996353459981"
}

data = {
    "currencyCode": "USD",
    "merchantOrderNumber": "20-1155909",
    "checkoutOptions": {
        "authorization": {
            "authorizationType": "AUTH_METHOD_CART_AMOUNT"
        },
        "capture": {
            "captureMethod": "CAPTURE_METHOD_NOW"
        },
        "consumerProfileOptions": {
            "isSaveConsumerProfile": False
        }
    },
    "cart": {
        "totalTransactionAmount": 21213,
        "totalTaxAmount": "1313",
        "lineItems": [
            {
                "id": "1",
                "quantity": 1,
                "unitPrice": 19900,
                "name": "dummy",
                "description": " ",
                "imageUrl": "/Users/arpitamundra/PycharmProjects/Softxai/WhatsApp Image 2024-04-26 at 16.14.20.jpeg"
            }
        ]
    },
    "consumer": {
        "phone": "",
        "email": "",
        "billingAddress": {
            "recipientFullName": "",
            "line1": "",
            "line2": "",
            "line3": "",
            "city": "",
            "state": "",
            "country": "",
            "postalCode": ""
        }
    }
}

response = requests.post(url, json=data, headers=headers)
print("1")
print(response.json())


import requests

def get_checkout_notifications(token):
    url = "https://merchant-api.checkout-cat.merchant.jpmorgan.com/v1/checkout/notifications"
    headers = {
        "Authorization": "Bearer " + token,
        "MERCHANTID": "996353459981"
    }
    query_params = {
        "periodStart": "2024-04-16T00:00:00.000Z",
        "periodEnd": "2024-04-19T00:00:00.000Z",
        "merchantOrderNumber": "23-1155938"
    }

    try:
        response = requests.get(url, headers=headers, params=query_params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error:", e)

# Replace 'your_token_here' with the actual token obtained from the Create Access API
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlCY3doSUVhaml0bWZQUERlY3E0UGdFVUo0OCIsImtpZCI6IjlCY3doSUVhaml0bWZQUERlY3E0UGdFVUo0OCJ9.eyJhdWQiOiJKUE1DOlVSSTpSUy0xMDUyMzktODU0ODQtSGVsaXhBUElFbnRpdGxlbWVudHNDQVQtUFJPRCIsImlzcyI6Imh0dHA6Ly9pZGEuanBtb3JnYW5jaGFzZS5jb20vYWRmcy9zZXJ2aWNlcy90cnVzdCIsImlhdCI6MTcxNDYyOTY3NiwibmJmIjoxNzE0NjI5Njc2LCJleHAiOjE3MTQ2NzI4NzYsIkpQTUNJZGVudGlmaWVyIjoiQjA0MTk5OSIsIlJvbGUiOlsiMTEwNDI5X0NIRUNLT1VUX01FUkNIX0FDQ0VTUy04NTQ4NC0xMDUyMzktUFJPRCIsIjEwMzI1N19QQVlNRU5UU19NRVJDSF9BQ0NFU1MtODU0ODQtMTA1MjM5LVBST0QiLCJIZWxpeEFQSUVudGl0bGVtZW50c0NBVC04NTQ4NC0xMDUyMzktUFJPRCIsIjEwMzAzMl9SRVBPUlRTX01FUkNIX0FDQ0VTUy04NTQ4NC0xMDUyMzktUFJPRCJdLCJDbGllbnRJUEFkZHJlc3MiOlsiMTY5LjIxLjQyLjg3IiwiMjcuNTguMTA1LjQ4IiwiMTY5LjIxLjc0LjIzMCJdLCJ1cG4iOiJCMDQxOTk5QEFELkpQTU9SR0FOQ0hBU0UuQ09NIiwiYXV0aG1ldGhvZCI6WyJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvYXV0aGVudGljYXRpb25tZXRob2QvdGxzY2xpZW50IiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2F1dGhlbnRpY2F0aW9ubWV0aG9kL3g1MDkiXSwiYXBwdHlwZSI6IkNvbmZpZGVudGlhbCIsImFwcGlkIjoiQ0MtMTA1MjM5LUIwNDE5OTktMjYxNTUwLVBST0QiLCJhdXRoX3RpbWUiOiIyMDI0LTA1LTAyVDA2OjAyOjE2Ljg2OVoiLCJ2ZXIiOiIxLjAifQ.JcvLjfNxQVLs5aTZs8Kj8sKdjKB7Q7JXV5q5mTO6RfAWwbo4q9W-I11RVuRgbWBcoVpm1ImEMTt_5FN4rVcMmzncBjazsk5A5p_wdw_TalEiV4u0TpBfDyq1r2sCYA90dyMKuYYRSgHpyNjOjaDPvBcyEuD6S3d38AMjmoPkjBSj0YHsohz8rGNYhFKEqgaaUHCBLn9cL0DzMYzHrCDNi-EbnXvBbUEQFtjUqpbsaSQHNqvEmYhLB2lFRhUuwPAn26YovsvGiPkZ4w8c6dvHIUNqcy9uNAtCptsrxROfqAwRxNPZjBgL9ktC8qmYy3zVzB2JL2nv6ty81J-BJ1EVcA"
notifications = get_checkout_notifications(token)
print(notifications)
print("2")



import requests

url = "https://merchant-api.checkout-cat.merchant.jpmorgan.com/v1/checkout/notifications/receive"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlCY3doSUVhaml0bWZQUERlY3E0UGdFVUo0OCIsImtpZCI6IjlCY3doSUVhaml0bWZQUERlY3E0UGdFVUo0OCJ9.eyJhdWQiOiJKUE1DOlVSSTpSUy0xMDUyMzktODU0ODQtSGVsaXhBUElFbnRpdGxlbWVudHNDQVQtUFJPRCIsImlzcyI6Imh0dHA6Ly9pZGEuanBtb3JnYW5jaGFzZS5jb20vYWRmcy9zZXJ2aWNlcy90cnVzdCIsImlhdCI6MTcxNDYyOTY3NiwibmJmIjoxNzE0NjI5Njc2LCJleHAiOjE3MTQ2NzI4NzYsIkpQTUNJZGVudGlmaWVyIjoiQjA0MTk5OSIsIlJvbGUiOlsiMTEwNDI5X0NIRUNLT1VUX01FUkNIX0FDQ0VTUy04NTQ4NC0xMDUyMzktUFJPRCIsIjEwMzI1N19QQVlNRU5UU19NRVJDSF9BQ0NFU1MtODU0ODQtMTA1MjM5LVBST0QiLCJIZWxpeEFQSUVudGl0bGVtZW50c0NBVC04NTQ4NC0xMDUyMzktUFJPRCIsIjEwMzAzMl9SRVBPUlRTX01FUkNIX0FDQ0VTUy04NTQ4NC0xMDUyMzktUFJPRCJdLCJDbGllbnRJUEFkZHJlc3MiOlsiMTY5LjIxLjQyLjg3IiwiMjcuNTguMTA1LjQ4IiwiMTY5LjIxLjc0LjIzMCJdLCJ1cG4iOiJCMDQxOTk5QEFELkpQTU9SR0FOQ0hBU0UuQ09NIiwiYXV0aG1ldGhvZCI6WyJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvYXV0aGVudGljYXRpb25tZXRob2QvdGxzY2xpZW50IiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2F1dGhlbnRpY2F0aW9ubWV0aG9kL3g1MDkiXSwiYXBwdHlwZSI6IkNvbmZpZGVudGlhbCIsImFwcGlkIjoiQ0MtMTA1MjM5LUIwNDE5OTktMjYxNTUwLVBST0QiLCJhdXRoX3RpbWUiOiIyMDI0LTA1LTAyVDA2OjAyOjE2Ljg2OVoiLCJ2ZXIiOiIxLjAifQ.JcvLjfNxQVLs5aTZs8Kj8sKdjKB7Q7JXV5q5mTO6RfAWwbo4q9W-I11RVuRgbWBcoVpm1ImEMTt_5FN4rVcMmzncBjazsk5A5p_wdw_TalEiV4u0TpBfDyq1r2sCYA90dyMKuYYRSgHpyNjOjaDPvBcyEuD6S3d38AMjmoPkjBSj0YHsohz8rGNYhFKEqgaaUHCBLn9cL0DzMYzHrCDNi-EbnXvBbUEQFtjUqpbsaSQHNqvEmYhLB2lFRhUuwPAn26YovsvGiPkZ4w8c6dvHIUNqcy9uNAtCptsrxROfqAwRxNPZjBgL9ktC8qmYy3zVzB2JL2nv6ty81J-BJ1EVcA"
merchant_id = "996353459981"
max_number_messages = 10
timeout_ms = 300
auto_ack = True

headers = {
    "Authorization": f"Bearer {token}",
    "merchantId": merchant_id
}

query_params = {
    "maxNumberMessages": max_number_messages,
    "timeoutMs": timeout_ms,
    "autoAck": auto_ack
}

try:
    response = requests.get(url, headers=headers, params=query_params)
    if response.status_code == 200:
        print("Request successful")
        print(response.json())  # Display the response data
    else:
        print(f"Request failed with status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")

import requests

def refund_transaction(token):
    url = "https://cat-api.merchant.jpmorgan.com/api/v2/refunds"
    headers = {
        "Authorization": "Bearer " + token,
        "request-id": "88844792889",
        "merchant-id": "996353459981",
        "Content-Type": "application/json"
    }
    body = {
        "merchant": {
            "merchantSoftware": {
                "companyName": "DOT Compliance Group",
                "productName": "RefundTransaction",
                "version": "1.235"
            }
        },
        "merchantOrderNumber": "20-1155907",
        "paymentMethodType": {
            "transactionReference": {
                "transactionReferenceId": "c884a588-bbb8-4ca4-b910-55443f3d6f3a"
            }
        }
    }

    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error:", e)

# Replace 'your_token_here' with the actual token obtained from the Create Access API
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlCY3doSUVhaml0bWZQUERlY3E0UGdFVUo0OCIsImtpZCI6IjlCY3doSUVhaml0bWZQUERlY3E0UGdFVUo0OCJ9.eyJhdWQiOiJKUE1DOlVSSTpSUy0xMDUyMzktODU0ODQtSGVsaXhBUElFbnRpdGxlbWVudHNDQVQtUFJPRCIsImlzcyI6Imh0dHA6Ly9pZGEuanBtb3JnYW5jaGFzZS5jb20vYWRmcy9zZXJ2aWNlcy90cnVzdCIsImlhdCI6MTcxNDYyOTY3NiwibmJmIjoxNzE0NjI5Njc2LCJleHAiOjE3MTQ2NzI4NzYsIkpQTUNJZGVudGlmaWVyIjoiQjA0MTk5OSIsIlJvbGUiOlsiMTEwNDI5X0NIRUNLT1VUX01FUkNIX0FDQ0VTUy04NTQ4NC0xMDUyMzktUFJPRCIsIjEwMzI1N19QQVlNRU5UU19NRVJDSF9BQ0NFU1MtODU0ODQtMTA1MjM5LVBST0QiLCJIZWxpeEFQSUVudGl0bGVtZW50c0NBVC04NTQ4NC0xMDUyMzktUFJPRCIsIjEwMzAzMl9SRVBPUlRTX01FUkNIX0FDQ0VTUy04NTQ4NC0xMDUyMzktUFJPRCJdLCJDbGllbnRJUEFkZHJlc3MiOlsiMTY5LjIxLjQyLjg3IiwiMjcuNTguMTA1LjQ4IiwiMTY5LjIxLjc0LjIzMCJdLCJ1cG4iOiJCMDQxOTk5QEFELkpQTU9SR0FOQ0hBU0UuQ09NIiwiYXV0aG1ldGhvZCI6WyJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvYXV0aGVudGljYXRpb25tZXRob2QvdGxzY2xpZW50IiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2F1dGhlbnRpY2F0aW9ubWV0aG9kL3g1MDkiXSwiYXBwdHlwZSI6IkNvbmZpZGVudGlhbCIsImFwcGlkIjoiQ0MtMTA1MjM5LUIwNDE5OTktMjYxNTUwLVBST0QiLCJhdXRoX3RpbWUiOiIyMDI0LTA1LTAyVDA2OjAyOjE2Ljg2OVoiLCJ2ZXIiOiIxLjAifQ.JcvLjfNxQVLs5aTZs8Kj8sKdjKB7Q7JXV5q5mTO6RfAWwbo4q9W-I11RVuRgbWBcoVpm1ImEMTt_5FN4rVcMmzncBjazsk5A5p_wdw_TalEiV4u0TpBfDyq1r2sCYA90dyMKuYYRSgHpyNjOjaDPvBcyEuD6S3d38AMjmoPkjBSj0YHsohz8rGNYhFKEqgaaUHCBLn9cL0DzMYzHrCDNi-EbnXvBbUEQFtjUqpbsaSQHNqvEmYhLB2lFRhUuwPAn26YovsvGiPkZ4w8c6dvHIUNqcy9uNAtCptsrxROfqAwRxNPZjBgL9ktC8qmYy3zVzB2JL2nv6ty81J-BJ1EVcA"
refund_response = refund_transaction(token)
print(refund_response)
# {'access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlCY3doSUVhaml0bWZQUERlY3E0UGdFVUo0OCIsImtpZCI6IjlCY3doSUVhaml0bWZQUERlY3E0UGdFVUo0OCJ9.eyJhdWQiOiJKUE1DOlVSSTpSUy0xMDUyMzktODU0ODQtSGVsaXhBUElFbnRpdGxlbWVudHNDQVQtUFJPRCIsImlzcyI6Imh0dHA6Ly9pZGEuanBtb3JnYW5jaGFzZS5jb20vYWRmcy9zZXJ2aWNlcy90cnVzdCIsImlhdCI6MTcxNDYyOTMzNiwibmJmIjoxNzE0NjI5MzM2LCJleHAiOjE3MTQ2NzI1MzYsIkpQTUNJZGVudGlmaWVyIjoiQjA0MTk5OSIsIlJvbGUiOlsiMTEwNDI5X0NIRUNLT1VUX01FUkNIX0FDQ0VTUy04NTQ4NC0xMDUyMzktUFJPRCIsIjEwMzI1N19QQVlNRU5UU19NRVJDSF9BQ0NFU1MtODU0ODQtMTA1MjM5LVBST0QiLCJIZWxpeEFQSUVudGl0bGVtZW50c0NBVC04NTQ4NC0xMDUyMzktUFJPRCIsIjEwMzAzMl9SRVBPUlRTX01FUkNIX0FDQ0VTUy04NTQ4NC0xMDUyMzktUFJPRCJdLCJDbGllbnRJUEFkZHJlc3MiOlsiMTY5LjIxLjQyLjg3IiwiMjcuNTguMTA1LjQ4IiwiMTY5LjIxLjc0LjIzMCJdLCJ1cG4iOiJCMDQxOTk5QEFELkpQTU9SR0FOQ0hBU0UuQ09NIiwiYXV0aG1ldGhvZCI6WyJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvYXV0aGVudGljYXRpb25tZXRob2QvdGxzY2xpZW50IiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2F1dGhlbnRpY2F0aW9ubWV0aG9kL3g1MDkiXSwiYXBwdHlwZSI6IkNvbmZpZGVudGlhbCIsImFwcGlkIjoiQ0MtMTA1MjM5LUIwNDE5OTktMjYxNTUwLVBST0QiLCJhdXRoX3RpbWUiOiIyMDI0LTA1LTAyVDA1OjU2OjM2LjAzNVoiLCJ2ZXIiOiIxLjAifQ.KP3l1AaNmgyT1gpwMtDMFAQnhrCePFL7OUH0SCFhbUNriAS10iohrPLsehGo_XlxUjkRhNtJoWeAgVpQ8b51oedTiCwaPaYo0og6yyy8YojOC0SyFKBwXnvkSm4hnMMTUhBC4WAwR4uFrINob8rZn_1mMkQ1RUmCXTXeXLgJt0ZQT7eUmMRKJD-NySRlgeSdaC5o-yq-C2zSXfqgsSpaKA5wja8Ugs-8Rad1GmCyqWRE-3B3Z_NutnGSNuf5P4MwsYqVCLNGZYtdT4DNYC-5zb4iEKBZGGzFNHZJXaPuy9Q47wDMbGk7gRDHTNqUtx7ZWEeQ4mjBZaBlCDGwZnjUPg', 'token_type': 'bearer', 'expires_in': 43200}
print("3")

import requests

def refund_transaction(token):
    url = "https://cat-api.merchant.jpmorgan.com/api/v2/refunds"
    headers = {
        "Authorization": "Bearer " + token,
        "request-id": "88864792889",
        "merchant-id": "996353459981",
        "Content-Type": "application/json"
    }
    body = {

        "merchant": {

            "merchantSoftware": {

                "companyName": "DOT Compliance Group",

                "productName": "RefundTransaction",

                "version": "1.235"

            }

        },

        "amount": 5000,

        "currency": "USD",

        "merchantOrderNumber": "21-1155906",

        "paymentMethodType": {

            "transactionReference": {

                "transactionReferenceId": "a42f01d3-bdc8-4518-8a68-ff26f271ce10"

            }

        }

    }
    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error:", e)

# Replace 'your_token_here' with the actual token obtained from the Create Access API
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlCY3doSUVhaml0bWZQUERlY3E0UGdFVUo0OCIsImtpZCI6IjlCY3doSUVhaml0bWZQUERlY3E0UGdFVUo0OCJ9.eyJhdWQiOiJKUE1DOlVSSTpSUy0xMDUyMzktODU0ODQtSGVsaXhBUElFbnRpdGxlbWVudHNDQVQtUFJPRCIsImlzcyI6Imh0dHA6Ly9pZGEuanBtb3JnYW5jaGFzZS5jb20vYWRmcy9zZXJ2aWNlcy90cnVzdCIsImlhdCI6MTcxNDYyOTY3NiwibmJmIjoxNzE0NjI5Njc2LCJleHAiOjE3MTQ2NzI4NzYsIkpQTUNJZGVudGlmaWVyIjoiQjA0MTk5OSIsIlJvbGUiOlsiMTEwNDI5X0NIRUNLT1VUX01FUkNIX0FDQ0VTUy04NTQ4NC0xMDUyMzktUFJPRCIsIjEwMzI1N19QQVlNRU5UU19NRVJDSF9BQ0NFU1MtODU0ODQtMTA1MjM5LVBST0QiLCJIZWxpeEFQSUVudGl0bGVtZW50c0NBVC04NTQ4NC0xMDUyMzktUFJPRCIsIjEwMzAzMl9SRVBPUlRTX01FUkNIX0FDQ0VTUy04NTQ4NC0xMDUyMzktUFJPRCJdLCJDbGllbnRJUEFkZHJlc3MiOlsiMTY5LjIxLjQyLjg3IiwiMjcuNTguMTA1LjQ4IiwiMTY5LjIxLjc0LjIzMCJdLCJ1cG4iOiJCMDQxOTk5QEFELkpQTU9SR0FOQ0hBU0UuQ09NIiwiYXV0aG1ldGhvZCI6WyJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvYXV0aGVudGljYXRpb25tZXRob2QvdGxzY2xpZW50IiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2F1dGhlbnRpY2F0aW9ubWV0aG9kL3g1MDkiXSwiYXBwdHlwZSI6IkNvbmZpZGVudGlhbCIsImFwcGlkIjoiQ0MtMTA1MjM5LUIwNDE5OTktMjYxNTUwLVBST0QiLCJhdXRoX3RpbWUiOiIyMDI0LTA1LTAyVDA2OjAyOjE2Ljg2OVoiLCJ2ZXIiOiIxLjAifQ.JcvLjfNxQVLs5aTZs8Kj8sKdjKB7Q7JXV5q5mTO6RfAWwbo4q9W-I11RVuRgbWBcoVpm1ImEMTt_5FN4rVcMmzncBjazsk5A5p_wdw_TalEiV4u0TpBfDyq1r2sCYA90dyMKuYYRSgHpyNjOjaDPvBcyEuD6S3d38AMjmoPkjBSj0YHsohz8rGNYhFKEqgaaUHCBLn9cL0DzMYzHrCDNi-EbnXvBbUEQFtjUqpbsaSQHNqvEmYhLB2lFRhUuwPAn26YovsvGiPkZ4w8c6dvHIUNqcy9uNAtCptsrxROfqAwRxNPZjBgL9ktC8qmYy3zVzB2JL2nv6ty81J-BJ1EVcA"
refund_response = refund_transaction(token)
print(refund_response)
# {'access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlCY3doSUVhaml0bWZQUERlY3E0UGdFVUo0OCIsImtpZCI6IjlCY3doSUVhaml0bWZQUERlY3E0UGdFVUo0OCJ9.eyJhdWQiOiJKUE1DOlVSSTpSUy0xMDUyMzktODU0ODQtSGVsaXhBUElFbnRpdGxlbWVudHNDQVQtUFJPRCIsImlzcyI6Imh0dHA6Ly9pZGEuanBtb3JnYW5jaGFzZS5jb20vYWRmcy9zZXJ2aWNlcy90cnVzdCIsImlhdCI6MTcxNDYyOTMzNiwibmJmIjoxNzE0NjI5MzM2LCJleHAiOjE3MTQ2NzI1MzYsIkpQTUNJZGVudGlmaWVyIjoiQjA0MTk5OSIsIlJvbGUiOlsiMTEwNDI5X0NIRUNLT1VUX01FUkNIX0FDQ0VTUy04NTQ4NC0xMDUyMzktUFJPRCIsIjEwMzI1N19QQVlNRU5UU19NRVJDSF9BQ0NFU1MtODU0ODQtMTA1MjM5LVBST0QiLCJIZWxpeEFQSUVudGl0bGVtZW50c0NBVC04NTQ4NC0xMDUyMzktUFJPRCIsIjEwMzAzMl9SRVBPUlRTX01FUkNIX0FDQ0VTUy04NTQ4NC0xMDUyMzktUFJPRCJdLCJDbGllbnRJUEFkZHJlc3MiOlsiMTY5LjIxLjQyLjg3IiwiMjcuNTguMTA1LjQ4IiwiMTY5LjIxLjc0LjIzMCJdLCJ1cG4iOiJCMDQxOTk5QEFELkpQTU9SR0FOQ0hBU0UuQ09NIiwiYXV0aG1ldGhvZCI6WyJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvYXV0aGVudGljYXRpb25tZXRob2QvdGxzY2xpZW50IiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2F1dGhlbnRpY2F0aW9ubWV0aG9kL3g1MDkiXSwiYXBwdHlwZSI6IkNvbmZpZGVudGlhbCIsImFwcGlkIjoiQ0MtMTA1MjM5LUIwNDE5OTktMjYxNTUwLVBST0QiLCJhdXRoX3RpbWUiOiIyMDI0LTA1LTAyVDA1OjU2OjM2LjAzNVoiLCJ2ZXIiOiIxLjAifQ.KP3l1AaNmgyT1gpwMtDMFAQnhrCePFL7OUH0SCFhbUNriAS10iohrPLsehGo_XlxUjkRhNtJoWeAgVpQ8b51oedTiCwaPaYo0og6yyy8YojOC0SyFKBwXnvkSm4hnMMTUhBC4WAwR4uFrINob8rZn_1mMkQ1RUmCXTXeXLgJt0ZQT7eUmMRKJD-NySRlgeSdaC5o-yq-C2zSXfqgsSpaKA5wja8Ugs-8Rad1GmCyqWRE-3B3Z_NutnGSNuf5P4MwsYqVCLNGZYtdT4DNYC-5zb4iEKBZGGzFNHZJXaPuy9Q47wDMbGk7gRDHTNqUtx7ZWEeQ4mjBZaBlCDGwZnjUPg', 'token_type': 'bearer', 'expires_in': 43200}
print("4")



import requests
import json
import uuid

url = "https://merchant-api.checkout-cat.merchant.jpmorgan.com/v1/checkout/intent"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlCY3doSUVhaml0bWZQUERlY3E0UGdFVUo0OCIsImtpZCI6IjlCY3doSUVhaml0bWZQUERlY3E0UGdFVUo0OCJ9.eyJhdWQiOiJKUE1DOlVSSTpSUy0xMDUyMzktODU0ODQtSGVsaXhBUElFbnRpdGxlbWVudHNDQVQtUFJPRCIsImlzcyI6Imh0dHA6Ly9pZGEuanBtb3JnYW5jaGFzZS5jb20vYWRmcy9zZXJ2aWNlcy90cnVzdCIsImlhdCI6MTcxNDYyOTY3NiwibmJmIjoxNzE0NjI5Njc2LCJleHAiOjE3MTQ2NzI4NzYsIkpQTUNJZGVudGlmaWVyIjoiQjA0MTk5OSIsIlJvbGUiOlsiMTEwNDI5X0NIRUNLT1VUX01FUkNIX0FDQ0VTUy04NTQ4NC0xMDUyMzktUFJPRCIsIjEwMzI1N19QQVlNRU5UU19NRVJDSF9BQ0NFU1MtODU0ODQtMTA1MjM5LVBST0QiLCJIZWxpeEFQSUVudGl0bGVtZW50c0NBVC04NTQ4NC0xMDUyMzktUFJPRCIsIjEwMzAzMl9SRVBPUlRTX01FUkNIX0FDQ0VTUy04NTQ4NC0xMDUyMzktUFJPRCJdLCJDbGllbnRJUEFkZHJlc3MiOlsiMTY5LjIxLjQyLjg3IiwiMjcuNTguMTA1LjQ4IiwiMTY5LjIxLjc0LjIzMCJdLCJ1cG4iOiJCMDQxOTk5QEFELkpQTU9SR0FOQ0hBU0UuQ09NIiwiYXV0aG1ldGhvZCI6WyJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvYXV0aGVudGljYXRpb25tZXRob2QvdGxzY2xpZW50IiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2F1dGhlbnRpY2F0aW9ubWV0aG9kL3g1MDkiXSwiYXBwdHlwZSI6IkNvbmZpZGVudGlhbCIsImFwcGlkIjoiQ0MtMTA1MjM5LUIwNDE5OTktMjYxNTUwLVBST0QiLCJhdXRoX3RpbWUiOiIyMDI0LTA1LTAyVDA2OjAyOjE2Ljg2OVoiLCJ2ZXIiOiIxLjAifQ.JcvLjfNxQVLs5aTZs8Kj8sKdjKB7Q7JXV5q5mTO6RfAWwbo4q9W-I11RVuRgbWBcoVpm1ImEMTt_5FN4rVcMmzncBjazsk5A5p_wdw_TalEiV4u0TpBfDyq1r2sCYA90dyMKuYYRSgHpyNjOjaDPvBcyEuD6S3d38AMjmoPkjBSj0YHsohz8rGNYhFKEqgaaUHCBLn9cL0DzMYzHrCDNi-EbnXvBbUEQFtjUqpbsaSQHNqvEmYhLB2lFRhUuwPAn26YovsvGiPkZ4w8c6dvHIUNqcy9uNAtCptsrxROfqAwRxNPZjBgL9ktC8qmYy3zVzB2JL2nv6ty81J-BJ1EVcA"
merchant_id = "996353459981"
request_id = "2282829292"  # Generate a random unique string for requestId

headers = {
    "Authorization": f"Bearer {token}",
    "requestId": request_id,
    "merchantId": merchant_id,
    "Content-Type": "application/json"
}

body = {
    "currencyCode": "USD",
    "merchantOrderNumber": "09042024",
    "checkoutOptions": {
        "authorization": {
            "authorizationType": "AUTH_METHOD_VERIFY_ONLY"
        },
        "capture": {
            "captureMethod": "CAPTURE_METHOD_MANUAL"
        }
    },
    "cart": {
        "totalTransactionAmount": 0
    }
}

try:
    response = requests.post(url, headers=headers, json=body)
    if response.status_code == 200:
        print("Request successful")
        print(response.json())  # Display the response data
    else:
        print(f"Request failed with status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")


import requests
import json
import uuid

url = "https://cat-api.merchant.jpmorgan.com/api/v2/payments"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlCY3doSUVhaml0bWZQUERlY3E0UGdFVUo0OCIsImtpZCI6IjlCY3doSUVhaml0bWZQUERlY3E0UGdFVUo0OCJ9.eyJhdWQiOiJKUE1DOlVSSTpSUy0xMDUyMzktODU0ODQtSGVsaXhBUElFbnRpdGxlbWVudHNDQVQtUFJPRCIsImlzcyI6Imh0dHA6Ly9pZGEuanBtb3JnYW5jaGFzZS5jb20vYWRmcy9zZXJ2aWNlcy90cnVzdCIsImlhdCI6MTcxNDYyOTY3NiwibmJmIjoxNzE0NjI5Njc2LCJleHAiOjE3MTQ2NzI4NzYsIkpQTUNJZGVudGlmaWVyIjoiQjA0MTk5OSIsIlJvbGUiOlsiMTEwNDI5X0NIRUNLT1VUX01FUkNIX0FDQ0VTUy04NTQ4NC0xMDUyMzktUFJPRCIsIjEwMzI1N19QQVlNRU5UU19NRVJDSF9BQ0NFU1MtODU0ODQtMTA1MjM5LVBST0QiLCJIZWxpeEFQSUVudGl0bGVtZW50c0NBVC04NTQ4NC0xMDUyMzktUFJPRCIsIjEwMzAzMl9SRVBPUlRTX01FUkNIX0FDQ0VTUy04NTQ4NC0xMDUyMzktUFJPRCJdLCJDbGllbnRJUEFkZHJlc3MiOlsiMTY5LjIxLjQyLjg3IiwiMjcuNTguMTA1LjQ4IiwiMTY5LjIxLjc0LjIzMCJdLCJ1cG4iOiJCMDQxOTk5QEFELkpQTU9SR0FOQ0hBU0UuQ09NIiwiYXV0aG1ldGhvZCI6WyJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvYXV0aGVudGljYXRpb25tZXRob2QvdGxzY2xpZW50IiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2F1dGhlbnRpY2F0aW9ubWV0aG9kL3g1MDkiXSwiYXBwdHlwZSI6IkNvbmZpZGVudGlhbCIsImFwcGlkIjoiQ0MtMTA1MjM5LUIwNDE5OTktMjYxNTUwLVBST0QiLCJhdXRoX3RpbWUiOiIyMDI0LTA1LTAyVDA2OjAyOjE2Ljg2OVoiLCJ2ZXIiOiIxLjAifQ.JcvLjfNxQVLs5aTZs8Kj8sKdjKB7Q7JXV5q5mTO6RfAWwbo4q9W-I11RVuRgbWBcoVpm1ImEMTt_5FN4rVcMmzncBjazsk5A5p_wdw_TalEiV4u0TpBfDyq1r2sCYA90dyMKuYYRSgHpyNjOjaDPvBcyEuD6S3d38AMjmoPkjBSj0YHsohz8rGNYhFKEqgaaUHCBLn9cL0DzMYzHrCDNi-EbnXvBbUEQFtjUqpbsaSQHNqvEmYhLB2lFRhUuwPAn26YovsvGiPkZ4w8c6dvHIUNqcy9uNAtCptsrxROfqAwRxNPZjBgL9ktC8qmYy3zVzB2JL2nv6ty81J-BJ1EVcA"
merchant_id = "996353459981"
request_id = "234234234"  # Generate a random unique string for requestId

headers = {
    "Authorization": f"Bearer {token}",
    "request-id": request_id,
    "merchant-id": merchant_id,
    "Content-Type": "application/json"
}

body = {
    "merchant": {
        "merchantSoftware": {
            "companyName": "DOT Compliance Group",
            "productName": "CapturePayment"
        }
    },
    "amount": 597,
    "currency": "USD",
    "paymentMethodType": {
        "card": {
            "accountNumber": "4111116395011111",
            "accountNumberType": "SAFETECH_TOKEN"
        }
    }
}

try:
    response = requests.post(url, headers=headers, json=body)
    if response.status_code == 200:
        print("Request successful")
        print(response.json())  # Display the response data
    else:
        print(f"Request failed with status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")


import requests

url = "https://cat-api.merchant.jpmorgan.com/api/v2/payments/a4d3a18e-e69d-4c3a-ba07-dd581ec16544"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlCY3doSUVhaml0bWZQUERlY3E0UGdFVUo0OCIsImtpZCI6IjlCY3doSUVhaml0bWZQUERlY3E0UGdFVUo0OCJ9.eyJhdWQiOiJKUE1DOlVSSTpSUy0xMDUyMzktODU0ODQtSGVsaXhBUElFbnRpdGxlbWVudHNDQVQtUFJPRCIsImlzcyI6Imh0dHA6Ly9pZGEuanBtb3JnYW5jaGFzZS5jb20vYWRmcy9zZXJ2aWNlcy90cnVzdCIsImlhdCI6MTcxNDYyOTY3NiwibmJmIjoxNzE0NjI5Njc2LCJleHAiOjE3MTQ2NzI4NzYsIkpQTUNJZGVudGlmaWVyIjoiQjA0MTk5OSIsIlJvbGUiOlsiMTEwNDI5X0NIRUNLT1VUX01FUkNIX0FDQ0VTUy04NTQ4NC0xMDUyMzktUFJPRCIsIjEwMzI1N19QQVlNRU5UU19NRVJDSF9BQ0NFU1MtODU0ODQtMTA1MjM5LVBST0QiLCJIZWxpeEFQSUVudGl0bGVtZW50c0NBVC04NTQ4NC0xMDUyMzktUFJPRCIsIjEwMzAzMl9SRVBPUlRTX01FUkNIX0FDQ0VTUy04NTQ4NC0xMDUyMzktUFJPRCJdLCJDbGllbnRJUEFkZHJlc3MiOlsiMTY5LjIxLjQyLjg3IiwiMjcuNTguMTA1LjQ4IiwiMTY5LjIxLjc0LjIzMCJdLCJ1cG4iOiJCMDQxOTk5QEFELkpQTU9SR0FOQ0hBU0UuQ09NIiwiYXV0aG1ldGhvZCI6WyJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvYXV0aGVudGljYXRpb25tZXRob2QvdGxzY2xpZW50IiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2F1dGhlbnRpY2F0aW9ubWV0aG9kL3g1MDkiXSwiYXBwdHlwZSI6IkNvbmZpZGVudGlhbCIsImFwcGlkIjoiQ0MtMTA1MjM5LUIwNDE5OTktMjYxNTUwLVBST0QiLCJhdXRoX3RpbWUiOiIyMDI0LTA1LTAyVDA2OjAyOjE2Ljg2OVoiLCJ2ZXIiOiIxLjAifQ.JcvLjfNxQVLs5aTZs8Kj8sKdjKB7Q7JXV5q5mTO6RfAWwbo4q9W-I11RVuRgbWBcoVpm1ImEMTt_5FN4rVcMmzncBjazsk5A5p_wdw_TalEiV4u0TpBfDyq1r2sCYA90dyMKuYYRSgHpyNjOjaDPvBcyEuD6S3d38AMjmoPkjBSj0YHsohz8rGNYhFKEqgaaUHCBLn9cL0DzMYzHrCDNi-EbnXvBbUEQFtjUqpbsaSQHNqvEmYhLB2lFRhUuwPAn26YovsvGiPkZ4w8c6dvHIUNqcy9uNAtCptsrxROfqAwRxNPZjBgL9ktC8qmYy3zVzB2JL2nv6ty81J-BJ1EVcA"
merchant_id = "996353459981"

headers = {
    "Authorization": f"Bearer {token}",
    "merchant-id": merchant_id,
}

try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Request successful")
        print(response.json())  # Display the response data
    else:
        print(f"Request failed with status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")
