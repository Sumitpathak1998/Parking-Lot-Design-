from services.PaymentService import PaymentService;
from models.paymentType import PaymentType;

class PaymentController : 

    def __init__(self):
        self.paymentService = PaymentService();

    def make_payment(self, parking_charges):
        print("Selct Payemt Option");

        payment_type = list(PaymentType);
        
        # Select Payment Type
        print("Select Payment Type from List :");
        for index , type in enumerate(payment_type,start=1) :
            print(f"{index}.{type.name}");
        selectedPaymentType = int(input("Select the Payment Type Number: "));

        paymentProcessor = self.paymentService.createPaymentProcess(payment_type[selectedPaymentType-1].value);    
        print("Please the Pay the Amount :");
        amount = float(input("Enter the Amount : "));

        return self.paymentService.make_payment(paymentProcessor,parking_charges,amount);