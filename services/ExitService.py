from managers.ticket_Manager import TicketManager;
from managers.payment_manager import PaymentManager;
from managers.floor_manager import FloorManager;
from managers.display_manager import DisplayManager;
from models.ticket import Ticket;
from repositories.ExitRepository import ExitRepository;
from response import Response;
from models.user import User;
from models.parkingAttendent import ParkingAttendent;

class ExitService : 
    
    current_ticket : Ticket;

    def __init__(self):
        self.exitRepository = ExitRepository();

    def scanAndcalculateCharges(self,user,ticket_id) :
        if (isinstance(user,ParkingAttendent)) :
            # 1st we need to check ticket_id present and there status
            # status : active or completed
            checkResponse : Response = self.exitRepository.checkTicketStatus(ticket_id);

            if not checkResponse.success :
                return checkResponse;
            
            ticket_info = checkResponse.data; 
            self.current_ticket = Ticket.from_dict(ticket_info)

            # calculate the time duration of parking 
            entry_time = ticket_info["entryTime"];
            timeDuration_res = self.exitRepository.calculateTimeDurationInHour(entry_time);    
            print("total_hour :", timeDuration_res["total_hour"]);
            print("exit time : ", timeDuration_res["exit_time"]);
            
            # assign exitTime 
            self.current_ticket.exitTime = timeDuration_res['exit_time'];

            # on the basis of time calculate the parking changes 
            parking_charges = self.exitRepository.calculateParkingCharges(timeDuration_res["total_hour"]);   

            return Response(200,True,data=parking_charges);
        else :
            return Response(403,False,message="Only parking attendent has access to perform exit process");

    def updateTicketRecordDisplayAndRelaseSpot(self,amount) :

        # update the ticket record 
        self.current_ticket.totalAmount = amount;
        self.current_ticket.paymentStatus = True;
        self.current_ticket.status = "completed";

        ticket_response = self.exitRepository.updateTicketRecord(self.current_ticket);
        print(ticket_response.message);

        # relase spot   
        spot_response = self.exitRepository.UpdateFloorSpot(self.current_ticket.spotId,"un-assign");
        print(spot_response.message);

        # update Display Board 
        spot_details = self.exitRepository.fetchDataBasisOfId("floorSpot.json",self.current_ticket.id);

        display_res = DisplayManager.updateDisplayBoardWhenSpotOccupiedAndRelase(spot_details["floor_id"],spot_details["spot_type"],"relase");
        print(display_res.message);

        return Response(200,True,"Ticket,Spot and Display board Update");



