from services.ExitService import ExitService;
from controller.PaymentController import PaymentController;
from response import Response;
from models.user import User;

class ExitController : 

    def __init__(self):
        self.exitService = ExitService();
        self.paymentController = PaymentController();

    def scanAndcalculateCharges(self,user : User) :
        ticket_id = int(input("Enter the Ticket Id : "));
        resposne : Response = self.exitService.scanAndcalculateCharges(user,ticket_id);

        if not resposne.success :
            print(resposne.message);
            return;

        parking_charges = resposne.data;
        print(f"Total Parking Charges : {parking_charges}");

        # collect the amount from user
        payment_res = self.paymentController.make_payment(parking_charges);
            
        # check the amount 
        if not payment_res.success :
            print("Exit Process Fail");
            print("Please Try Again , Thanks"); 
            return; 
        else : 
            print(payment_res.message);

        final_res = self.updateTicketRecordDisplayAndRelaseSpot(payment_res.data);
        if(final_res.message) :
            print("Payment Completed.");
            print("Thanks Visit Again");
    
    def updateTicketRecordDisplayAndRelaseSpot(self,amount : float) :
        return self.exitService.updateTicketRecordDisplayAndRelaseSpot(amount);
        