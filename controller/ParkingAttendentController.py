from models.user import User;
from models.parkingAttendent import ParkingAttendent;
from services.ParkingAttendentService import ParkingAttendentService;
from services.FloorService import FloorService;


class ParkingAttendentController :

    def __init__(self):
        self.floorService = FloorService();
        self.parkingAttendentService = ParkingAttendentService();

    def addParkingAttendent(self , user : User) :
        parkingAttendent : ParkingAttendent;

        attendent_id = int(input("Enter the Attendent Id : "));
        name = input("Enter the attendent Name : ");    
        #select Floor 
        data = self.floorService.fetchFloorData(user);
        
        if(len(data) == 0) :
            return "Please insert the Floor first";
    
        print("Select Floor from List : ");
        for floor in data :
            print(f"{floor["id"]}.{floor["name"]}");
        floor_id = int(input("Select Floor Id : "));
    

        parkingAttendent = ParkingAttendent(attendent_id,name);
        response = self.parkingAttendentService.addParkingAttendent(user,parkingAttendent,floor_id);
        print(response.message);

    def removeParkingAttendent(self,user) :
        attendent_id = int(input("Enter the Attendent Id : "));
        response = self.parkingAttendentService.removeparkingAttendent(user,attendent_id);
        print(response.message);

