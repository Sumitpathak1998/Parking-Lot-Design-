from managers.data_manager import DataManager;
from managers.ticket_Manager import TicketManager;
from managers.floor_manager import FloorManager;
from managers.display_manager import DisplayManager;
from repositories.FloorSpotRepository import FloorSpotRepository;
from models.ticket import Ticket;
from response import Response;

class EntryRepository : 

    def __init__(self):
        self.floorSpotRepository = FloorSpotRepository();

    def createTicket(self,ticket : Ticket) :
        ticket_dict = ticket.__dict__;     
        
        response : Response = DataManager.addData("ticket.json",ticket_dict);
        response.message = "Ticket Created";
        return response;

    def findSpotTypeForVehicle(self,vehicle_type) :
        return TicketManager.findSpotTypeForVehicle(vehicle_type);

    def selectSpotForVehicle(self ,spot_type) :
        spot_data = self.floorSpotRepository.fetchFloorSpotData();
        return TicketManager.selectSpotForVehicle(spot_type,spot_data);

    def fetchEntryAndExitPanel(self ,floor_id):
        return FloorManager.fetchEntryAndExitPanel(floor_id);

    def generateTicketId(self) :
        ticket_data = self.fetchTicketData();
        return TicketManager.generateTicketId(ticket_data);

    def UpdateFloorSpot(self,floorSpot,work_type) : 
        return FloorManager.UpdateFloorSpot(floorSpot,work_type);

    def updateDisplayBoardWhenSpotOccupiedAndRelase(self,floor_id,select_spot_type,work_type) :
        return DisplayManager.updateDisplayBoardWhenSpotOccupiedAndRelase(floor_id,select_spot_type,work_type);

    def fetchTicketData(self) :
        return DataManager.fetchData("ticket.json");


