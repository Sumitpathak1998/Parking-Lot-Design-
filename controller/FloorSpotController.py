from models.spotType import SpotType;
from models.floorSpot import FloorSpot;
from models.user import User;
from services.FloorService import FloorService;
from services.FloorSpotService import FloorSpotService;

class FloorSpotController : 

    def __init__(self) : 
        self.floorService = FloorService();
        self.floorSpotService = FloorSpotService();

    def createSpot(self , user : User) :
        spot_id = int(input("Enter the Spot Id : "));
        spot_name = input("Enter the Spot Name : ");
        spot_type = list(SpotType);
        
        # Select Spot Type
        print("Select Spot Type from List :");
        for index , type in enumerate(spot_type,start=1) :
            print(f"{index}.{type.name}");
        choice_type = int(input("Select the Spot Type Number: "));

        #select Floor 
        data = self.floorService.fetchFloorData(user);
        
        if(len(data) == 0) :
            return "Please insert the Floor first";

        print("Select Floor from List : ");
        for floor in data :
            print(f"{floor["id"]}.{floor["name"]}");
        floor_id = int(input("Select Floor Id : "));

        # create a floor spot object 
        floorSpot = FloorSpot(spot_id,spot_name,spot_type[choice_type-1].value,floor_id);
        response = self.floorSpotService.CreateSpot(user,floorSpot);
        print(response.message);

    def removeParkingSlot(self,user) : 
        spot_id = int(input("Enter the parking Spot Id : "));
        response = self.floorSpotService.removeParkingSpot(user,spot_id);
        print(response.message);