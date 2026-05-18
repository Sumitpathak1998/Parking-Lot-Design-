from services.AdminService import AdminService;
from managers.data_manager import DataManager;
from models.spotType import SpotType;
from models.panelType import PanelType;

class AdminController : 

    adminService = AdminService();

    def createAdmin(self, id : int , name : str , email : str) :
        return self.adminService.CreateAdmin(id,name,email);

    def createParkingLot(self, id : int , name : str) : 
        return self.adminService.createParkingLot(id,name); 

    def addFloor(self) :

        # Get Floor Info
        id = int(input("Enter the New Floor Id : "));
        name = input("Enter the New Floor Name : ");
        
        response = self.adminService.addFloor(id,name);
        print(response);

    def createSpot(self) :
        spot_id = int(input("Enter the Spot Id : "));
        spot_name = input("Enter the Spot Name : ");
        spot_type = list(SpotType);
        
        # Select Spot Type
        print("Select Spot Type from List :");
        for index , type in enumerate(spot_type,start=1) :
            print(f"{index}.{type.name}");
        choice_type = int(input("Select the Spot Type Number: "));

        #select Floor 
        data = DataManager.fetchData("floor.json");
        
        if(len(data) == 0) :
            return "Please insert the Floor first";

        print("Select Floor from List : ");
        for floor in data :
            print(f"{floor["id"]}.{floor["name"]}");
        floor_id = int(input("Select Floor Id : "));

        response = self.adminService.CreateSpot(spot_id,spot_name,spot_type[choice_type - 1].value,floor_id);
        print(response);

    def addParkingAttendent(self) :
        attendent_id = int(input("Enter the Attendent Id : "));
        name = input("Enter the attendent Name : ");    
        #select Floor 
        data = DataManager.fetchData("floor.json");
        
        if(len(data) == 0) :
            return "Please insert the Floor first";
    
        print("Select Floor from List : ");
        for floor in data :
            print(f"{floor["id"]}.{floor["name"]}");
        floor_id = int(input("Select Floor Id : "));
    
        response = self.adminService.addParkingAttendent(attendent_id,name,floor_id);
        print(response);

    def addPanel(self) : 
        panel_id = int(input("Enter the Panel Id : "));
        name = input("Enter the Panel Name : ");    
        
        # select Panel Type

        panel_type = list(PanelType); 
        print("Select Panel Type from List :");
        for index , type in enumerate(panel_type,start=1) :
            print(f"{index}.{type.name}");
        choice_type = int(input("Select the Panel Type Number: "));

        #select Floor 
        data = DataManager.fetchData("floor.json");
        
        if(len(data) == 0) :
            return "Please insert the Floor first";
    
        print("Select Floor from List : ");
        for floor in data :
            print(f"{floor["id"]}.{floor["name"]}");
        floor_id = int(input("Select Floor Id : "));
    
        response = self.adminService.addEntryAndExitPanel(panel_id,name,panel_type[choice_type - 1].value,floor_id);
        print(response);
    
    def removeFloor(self) :
        floor_id = int(input("Enter the floor Id : "));
        response = self.adminService.removeFloor(floor_id);
        print(response["message"]);

    def removeParkingSlot(self) : 
        spot_id = int(input("Enter the parking Spot Id : "));
        response = self.adminService.removeParkingSpot(spot_id);
        print(response["message"]);

    def removeParkingAttendent(self) :
        attendent_id = int(input("Enter the Attendent Id : "));
        response = self.adminService.removePanel(attendent_id);
        print(response["message"]);

    def removePanel(self) :
        panel_id = int(input("Enter the Panel Id : "));
        response = self.adminService.removePanel(panel_id);
        print(response["message"]);

    def modifyParkingRate(self) :
        first_hour = float(input("Enter the first hour rate : "));
        second_third_hour = float(input("Enter the second and third hour rate : "));
        remaining_hour = float(input("Enter the remaining hour rate : "));

        response = self.adminService.modifyParkingRate(first_hour,second_third_hour,remaining_hour);
        print(response["message"]);

