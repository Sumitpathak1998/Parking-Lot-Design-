from models.user import User;
from models.floor import Floor;
from services.FloorService import FloorService;

class FloorController : 

    def __init__(self):
        self.floorService = FloorService();
        pass;

    def addFloor(self,user : User) :

        floor : Floor;

        # Get Floor Info
        id = int(input("Enter the New Floor Id : "));
        name = input("Enter the New Floor Name : ");
        
        floor = Floor(id,name);
        
        response = self.floorService.addFloor(floor,user);
        print(response.message);

    def removeFloor(self, user : User) :
        floor_id = int(input("Enter the floor Id : "));
        response = self.floorService.removeFloor(floor_id,user);
        print(response.message);

