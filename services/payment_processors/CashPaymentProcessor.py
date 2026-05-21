from services.payment_processors.PaymentProcessor import PaymentProcessor;
from response import Response;

class CashPaymentProcessor(PaymentProcessor) : 

    def __init__(self):
        pass;

    def processPayment(self,amount) : 
        return Response(200,True,f"Cash Payment of {amount} successful",amount);