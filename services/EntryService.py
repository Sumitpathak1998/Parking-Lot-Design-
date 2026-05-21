from models.ticket import Ticket;
from models.user import User;
from models.parkingAttendent import ParkingAttendent;
from repositories.EntryRepository import EntryRepository;
from response import Response;

class EntrySecvice :

    def __init__(self):
        self.entryRepository = EntryRepository();

    def generateParkingTicket(self,user : User,vehicle_num,vehicle_type,entry_time) :
        
        if(isinstance(user,ParkingAttendent)) :

            #find the spot type for vehicle
            spot_type =  self.entryRepository.findSpotTypeForVehicle(vehicle_type);

            # check Spot According to specific spot Type
            spotResposne : Response = self.entryRepository.selectSpotForVehicle(spot_type);

            if not spotResposne.success :
                return spotResposne;

            spot_info = spotResposne.data;
            floor_id = spot_info["floor_id"];
            floorSpot = spot_info["id"];

            panelResponse : Response = self.entryRepository.fetchEntryAndExitPanel(floor_id);

            if not panelResponse.success :
                return panelResponse;

            print(panelResponse.message);

            entry,exit = (panelResponse.data).values();

            # generate the ticket Id by Ticket Manager
            ticket_id = self.entryRepository.generateTicketId();

            ticket = Ticket(ticket_id,vehicle_num,vehicle_type,floor_id,floorSpot,entry,exit,entry_time,floorSpot);
            response =  self.entryRepository.createTicket(ticket);

            print(response.message);

            # Now After the Ticket generate update the floor Spot 
            spot_res = self.entryRepository.UpdateFloorSpot(floorSpot,work_type="assign");
            print(spot_res.message);

            # And also update the Display Board 
            select_spot_type = spot_info["spot_type"];  
            dispaly_res = self.entryRepository.updateDisplayBoardWhenSpotOccupiedAndRelase(floor_id,select_spot_type,"occupied");
            print(dispaly_res.message);

            return Response(200,True,data=ticket);
        else :
            return Response(403,False,message="Only Parking attendent has access to generate ticket");


