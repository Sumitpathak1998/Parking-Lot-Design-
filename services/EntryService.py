from managers.ticket_Manager import TicketManager;
from managers.floor_manager import FloorManager;
from managers.display_manager import DisplayManager;
from models.ticket import Ticket;
from repositories.EntryRepository import EntryRepository;

class EntrySecvice :

    entryRepository = EntryRepository();

    def generateParkingTicket(self,vehicle_num,vehicle_type,entry_time) :

        #find the spot type for vehicle
        spot_type = TicketManager.findSpotTypeForVehicle(vehicle_type);

        # check Spot According to specific spot Type
        spot_res = TicketManager.selectSpotForVehicle(spot_type);


        if not spot_res["success"] :
            return spot_res["message"];

        spot_info = spot_res["data"];
        floor_id = spot_info["floor_id"];
        floorSpot = spot_info["id"];

        panel_res = FloorManager.fetchEntryAndExitPanel(floor_id);

        if not panel_res["success"] :
            return panel_res;

        print(panel_res);
        entry,exit = panel_res["data"].values();

        # generate the ticket Id by Ticket Manager
        ticket_id = TicketManager.generateTicketId();

        ticket = Ticket(ticket_id,vehicle_num,vehicle_type,floor_id,floorSpot,entry,exit,entry_time,floorSpot);
        response =  self.entryRepository.createTicket(ticket);

        print(response["message"]);

        # Now After the Ticket generate update the floor Spot 
        spot_res = FloorManager.UpdateFloorSpot(floorSpot);
        print(spot_res["message"]);

        # And also update the Display Board 
        select_spot_type = spot_info["spot_type"];  
        dispaly_res = DisplayManager.updateDisplayBoardWhenSpotOccupiedAndRelase(floor_id,select_spot_type,"occupied");
        print(dispaly_res['message']);

        return {"success" : True , "data" : ticket};



