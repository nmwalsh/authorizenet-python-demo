from authorizenet import apicontractsv1
from authorizenet.apicontrollers import*
from decimal import*

import credentials # improting our credentials from credentials.py
 
# Authentication steps using Authorize.Net API credentials
merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = credentials.api_login_name
merchantAuth.transactionKey = credentials.transaction_key


def charge(card_number, expiration_date, amount, merchant_id): 
    creditCard = apicontractsv1.creditCardType()
    creditCard.cardNumber = card_number
    creditCard.expirationDate = expiration_date
     
    payment = apicontractsv1.paymentType()
    payment.creditCard = creditCard
     
    transactionrequest = apicontractsv1.transactionRequestType()
    transactionrequest.transactionType ="authCaptureTransaction"
    transactionrequest.amount = amount
    transactionrequest.payment = payment
     
     
    createtransactionrequest = apicontractsv1.createTransactionRequest()
    createtransactionrequest.merchantAuthentication = merchantAuth
    createtransactionrequest.refId = merchant_id
     
    createtransactionrequest.transactionRequest = transactionrequest
    createtransactioncontroller = createTransactionController(createtransactionrequest)
    createtransactioncontroller.execute()
     
    response = createtransactioncontroller.getresponse()

    if (response.messages.resultCode=="Ok"):
           print"Transaction ID : %s"% response.transactionResponse.transId
    else:
           print"response code: %s"% response.messages.resultCode

# Custom transaction data - feel free to define your own!           
card_number = "4111111111111111"
expiration_date = "2020-12"
amount = Decimal('13.37') 
merchant_id = "Pied-Piper" 

# Invoke the charge function to execute the transaction
charge(card_number, expiration_date, amount, merchant_id)
