from services.ExitService import ExitService;

class ExitController : 

    def __init__(self):
        self.exitService = ExitService();

    def scanAndcalculateCharges(self) :
        ticket_id = int(input("Enter the Ticket Id : "));
        resposne = self.exitService.scanAndcalculateCharges(ticket_id);

        if not resposne["success"] :
            print(resposne["message"]);

        parking_charges = resposne["data"];
        print(f"Total Parking Charges : {parking_charges}");
        print("Please the Pay the Amount :");
        # collect the amount from user 
        amount = float(input("Enter the Amount : "));

        count = 0;
        amount_collect_confirm = False;
        while count < 2 : 
            if ( amount != parking_charges) :
                print(f"Amount not matched , Pay Again you have {2-count} chance left : ")
                amount = float(input("Enter the Amount : "));
                count += 1;
            else : 
                print(f"Amount Received");
                amount_collect_confirm = True;
                break;
            
        # check the amount 
        if not amount_collect_confirm :
            print("Exit Process Fail");
            print("Please Try Again , Thanks"); 
            return; 

        final_res = self.updateTicketRecordDisplayAndRelaseSpot(amount);
        if(final_res["success"]) :
            print("Payment Completed.");
            print("Thanks Visit Again");
    
    def updateTicketRecordDisplayAndRelaseSpot(self,amount : float) :
        return self.exitService.updateTicketRecordDisplayAndRelaseSpot(amount);
        