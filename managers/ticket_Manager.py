from models.vehicleType import VehicleType;
from models.spotType import SpotType;
from repositories.EntryRepository import EntryRepository;

class TicketManager :

    entryRepository = EntryRepository();
    __vehicle_spot_mapping = {
        VehicleType.CAR : [
            SpotType.COMPACT,
            SpotType.LARGE
        ],
        VehicleType.TRUCK : [SpotType.LARGE],
        VehicleType.MOTORCYCLE : [SpotType.MOTORCYCLE],
        VehicleType.ELECTRIC_CAR : [SpotType.ELECTRIC]
    }

    @classmethod
    def findSpotTypeForVehicle(cls,vehicle_type) :
        print("vehicle_type :" , vehicle_type);
        type =  VehicleType(vehicle_type);
        spot_type = cls.__vehicle_spot_mapping[type];
        return spot_type;

    # Here in the method on the basis of SpotTYpe we check empty and what get first that spot id picked 
    @classmethod
    def selectSpotForVehicle(cls,spot_types) :
        spot_type = [spot.value for spot in spot_types];
        data = cls.entryRepository.fetchSpotData();

        if(len(data) == 0) :
            return {"success" : False , "message" : "No Spot Present"};
    
        spot = None;
        for el in data :
            print("dvbv", bool(el["occupied"]));
            if el["spot_type"] in spot_type and bool(el["occupied"]) == False : 
                print("cam to this")
                spot = el;
                break;

        print("spot",spot);
        if(spot == None) :
            return {"success" : False , "message" : "No Spot Present for this vehicle"};
        else :
            return {"success" : True , "data" : spot};

    # get the latest ticket Id number and inc. by one 
    @classmethod
    def generateTicketId(cls) :
        data = cls.entryRepository.fetchTicketData();

        ticket_id = None;
        if(len(data) == 0) : 
            return 1;
        else :
            ticket_id = int(data[-1]["id"]) + 1;
            return ticket_id;

    @classmethod
    def checkTicketStatus(cls,ticket_id) :
        data = cls.entryRepository.fetchTicketData();

        check = False;
        status = False;
        ticket_info = None;
        for ticket in data : 
            if ( ticket["id"] == ticket_id) :
                check = True;
                if (ticket["status"] == "active") :
                    status = True;
                    ticket_info = ticket;
                    break;

        if not check :
            return {"success" : False , "message" : "Please check the Id Again"};
        elif not status :
            return {"success" : False , "message" : "For this Ticket Payment completed"};
        else :
            return {"success" : True , "data" : ticket_info};



         
            
        


