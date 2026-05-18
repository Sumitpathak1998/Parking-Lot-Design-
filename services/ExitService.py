from managers.ticket_Manager import TicketManager;
from managers.payment_manager import PaymentManager;
from managers.floor_manager import FloorManager;
from managers.display_manager import DisplayManager;
from models.ticket import Ticket;
from repositories.ExitRepository import ExitRepository;

class ExitService : 
    
    current_ticket : Ticket;

    def __init__(self):
        self.exitRepository = ExitRepository();

    def scanAndcalculateCharges(self,ticket_id) :

        # 1st we need to check ticket_id present and there status
        # status : active or completed
        check_res = TicketManager.checkTicketStatus(ticket_id);

        if not check_res["success"] :
            return check_res;
        
        ticket_info = check_res["data"]; 
        self.current_ticket = Ticket.from_dict(ticket_info)

        # calculate the time duration of parking 
        entry_time = ticket_info["entryTime"];
        timeDuration_res = PaymentManager.calculateTimeDurationInHour(entry_time);    
        print("total_hour :", timeDuration_res["total_hour"]);
        print("exit time : ", timeDuration_res["exit_time"]);
        
        # assign exitTime 
        self.current_ticket.exitTime = timeDuration_res['exit_time'];

        # on the basis of time calculate the parking changes 
        parking_charges = PaymentManager.calculateParkingCharges(timeDuration_res["total_hour"]);   

        return {"success" : True , "data" : parking_charges};

    def updateTicketRecordDisplayAndRelaseSpot(self,amount) :

        # update the ticket record 
        self.current_ticket.totalAmount = amount;
        self.current_ticket.paymentStatus = True;
        self.current_ticket.status = "completed";

        ticket_response = self.exitRepository.updateTicketRecord(self.current_ticket);
        print(ticket_response['message']);

        # relase spot   
        spot_response = FloorManager.UpdateFloorSpot(self.current_ticket.spotId,"un-assign");
        print(spot_response["message"]);

        # update Display Board 
        spot_details = self.exitRepository.fetchDataBasisOfId("floorSpot.json",self.current_ticket.id);

        display_res = DisplayManager.updateDisplayBoardWhenSpotOccupiedAndRelase(spot_details["floor_id"],spot_details["spot_type"],"relase");
        print(display_res["message"]);

        return {"success" : True , "message" : "Ticket,Spot and Display board Update"};



