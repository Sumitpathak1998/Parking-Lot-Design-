from models.ticket import Ticket;
from managers.data_manager import DataManager;
from managers.ticket_Manager import TicketManager;
from managers.payment_manager import PaymentManager;
from managers.display_manager import DisplayManager;
from managers.floor_manager import FloorManager;
from response import Response;

class ExitRepository : 

    def checkTicketStatus(self,ticket_id) :
        data = self.fetchTicketData();
        return TicketManager.checkTicketStatus(ticket_id,data);

    def calculateTimeDurationInHour(self,entry_time) :
        return PaymentManager.calculateTimeDurationInHour(entry_time);
    
    def calculateParkingCharges(self,total_hour) :
        return PaymentManager.calculateParkingCharges(total_hour);

    def UpdateFloorSpot(self,spotId,work_type) :
        return FloorManager.UpdateFloorSpot(spotId,work_type);

    def updateDisplayBoardWhenSpotOccupiedAndRelase(self,floor_id,spot_type,work_type) : 
        return DisplayManager.updateDisplayBoardWhenSpotOccupiedAndRelase(self,floor_id,spot_type,work_type)

    def updateTicketRecord(self,ticket : Ticket) :
        data = DataManager.fetchData("ticket.json");

        for index , ticket_dict in enumerate(data,start=0) : 
            if int(ticket_dict["id"]) == int(ticket.id) :
                data[index] = ticket.__dict__;
                break;

        response : Response = DataManager.updateData("ticket.json",data);
        if(response.success) :
            response.message = "Ticket Updated";
        return response;

    def fetchDataBasisOfId(self,location,id) :
        data = DataManager.fetchData(location);

        resposne = None;
        for el in data :
            if( int(el["id"]) == id ) :
                resposne = el;
                break;
        return resposne;

    def fetchTicketData(self) :
        return DataManager.fetchData("ticket.json");


