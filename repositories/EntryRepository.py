from managers.data_manager import DataManager;
from models.ticket import Ticket;
class EntryRepository : 

    def fetchSpotData(self) :
        return DataManager.fetchData("floorSpot.json");

    def fetchTicketData(self) :
        return DataManager.fetchData("ticket.json");

    def createTicket(slef,ticket : Ticket) :
        ticket_dict = ticket.__dict__;     
        
        DataManager.addData("ticket.json",ticket_dict);
        return {"success" : True , "message" : "Ticket Created"};


