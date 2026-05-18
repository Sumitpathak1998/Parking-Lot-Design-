from models.ticket import Ticket;
from managers.data_manager import DataManager;

class ExitRepository : 

    def updateTicketRecord(self,ticket : Ticket) :
        data = DataManager.fetchData("ticket.json");

        for index , ticket_dict in enumerate(data,start=0) : 
            if int(ticket_dict["id"]) == int(ticket.id) :
                data[index] = ticket.__dict__;
                break;

        response = DataManager.updateData("ticket.json",data);
        if(response["success"]) :
            return {"success" : True , "message" : "Ticket Updated"};
        else : 
            return response;

    def fetchDataBasisOfId(self,location,id) :
        data = DataManager.fetchData(location);

        resposne = None;
        for el in data :
            if( int(el["id"]) == id ) :
                resposne = el;
                break;
        return resposne;


