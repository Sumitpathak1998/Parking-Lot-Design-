from services.payment_processors.PaymentProcessor import PaymentProcessor;
from response import Response;

class UPIPaymentProcessor(PaymentProcessor) : 

    def __init__(self):
        pass;

    def processPayment(self,amount) : 
        return Response(200,True,f"UPI Payment of {amount} successful",amount);