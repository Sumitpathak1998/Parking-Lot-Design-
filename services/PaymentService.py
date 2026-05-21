from services.payment_processors.PaymentProcessor import PaymentProcessor;
from services.payment_processors.CashPaymentProcessor import CashPaymentProcessor;
from services.payment_processors.CardPaymentProcessor import CreditCardPaymentProcessor;
from services.payment_processors.UPIPaymentProcessor import UPIPaymentProcessor;
from response import Response;

class PaymentService :

    def __init__(self):
        pass;

    def make_payment(self, paymentProcessor : PaymentProcessor , parking_charges , amount) :
        if ( amount != parking_charges) :
            return Response(400,False,"Amount not matched");
        else :
            return paymentProcessor.processPayment(amount);

    def createPaymentProcess(self,payment_type) :
        paymentProcess : PaymentProcessor;
        match payment_type :
            case "cash" :
                paymentProcess = CashPaymentProcessor();
            case "card" :
                paymentProcess = CreditCardPaymentProcessor();
            case "upi" : 
                paymentProcess = UPIPaymentProcessor();

        return paymentProcess;
