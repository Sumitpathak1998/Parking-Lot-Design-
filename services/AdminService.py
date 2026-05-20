from models.admin import Admin as admin;
from repositories.AdminRepository import AdminRepository;
from managers.data_manager import DataManager;
from managers.floor_manager import FloorManager;
from managers.display_manager import DisplayManager;
from models.floor import Floor;
from models.parkingRate import ParkingRate;

class AdminService :   

    adminRepository = AdminRepository();

    def CreateAdmin(self, id : int , name : str , email : str) :
        # check Admin Id is present or not
        check_res = DataManager.checkDuplicateData("admin.json" , id);

        if(check_res) :
            return "Admin Already Added with same ID";
    
        new_admin = self.adminRepository.createAdmin(id,name,email);

        return f"Admin is Created : {new_admin.name}";

    def createParkingLot(self, id : int , name : str) :
        #check Parking lot id is present or not 
        check_res = DataManager.checkDuplicateData("parkingLot.json" , id);
        
        if(check_res) :
            return "Parking Lot Already Added with same ID";
        
        new_parkinglot = self.adminRepository.createParkingLot(id,name); 
        return f"Parking lot Created : {new_parkinglot.name}";

    def addFloor(self, id : int , name : str) :
        # check floor is present or not 
        check_res = DataManager.checkDuplicateData("floor.json" , id);
        
        if(check_res) :
            return "Floor Already Added with same ID";
    
        floor =  self.adminRepository.addFloor(id,name);
        
        # create the display of floor 
        self.CreateFloorDisplay(floor);

        return "Floor & Display board is created";

    def CreateFloorDisplay(self, floor : Floor ) : 
        self.adminRepository.createFloorDisplay(floor);

    def CreateSpot(self, spot_id : int ,  name : str , spot_type : str , floor_id : int) :
        # check spot is present or not 
        check_res = DataManager.checkDuplicateData("floorSpot.json" , spot_id);
        
        if(check_res) :
            return "Floor Spot Already Added with same ID";


        spot = self.adminRepository.CreateSpot(spot_id,name,spot_type,floor_id);

        #Update floor with the Spot by Spot Manager like Assign spot to floor 
        spotAddedRes = FloorManager.assignNewSpotToFloor(floor_id,spot_id);
        print(spotAddedRes);

        #Update disply of floor by display manager
        disUpdateRes = DisplayManager.updateDisplayBoardWhenSpotAdd(floor_id,spot_type);
        print(disUpdateRes);

        return "Spot is created"; 


    def addParkingAttendent(self, id: int , name : str , floor_id : int) :
        # check Attendent is present or not 
        check_res = DataManager.checkDuplicateData("parkingAttendent.json" , id);
        
        if(check_res) :
            return "Floor Attendent Already Added with same ID";

        # add the parking attwndent
        parkingAtt = self.adminRepository.addParkingAttendent(id,name);

        # Assign the floor to Parking Attendent by floor manager
        res = FloorManager.assingFloorToParkingAttendent(floor_id,id);
    
        return "Parking attendent created and assign to Floor";
    
    def addEntryAndExitPanel(self, id : int , name : str , panel_type : str , floor_id : int) :
        # check Panel is present or not 
        check_res = DataManager.checkDuplicateData("panel.json" , id);
        
        if(check_res) :
            return "Panel Already Added with same ID";

        # add the entry exit panel 
        parkingAtt = self.adminRepository.addEntryAndExitPanel(id,name,panel_type,floor_id);
        
        # assign entry and exit panel to floor 
        floor_res = FloorManager.assignPanelToFloor(floor_id,id);
    
        return "Panel added and assign to Floor";


    def removeFloor(self,floor_id) : 

        #check if any spot assign this floor or not 
        data = DataManager.fetchData("floor.json");

        response = None;
        check_id = False;
        for index, floor in enumerate(data,start=0) : 
            if(int(floor['id']) == floor_id) :
                check_id = True;
                check_len_spot = len(list(floor["spot"]));
                if (check_len_spot > 0) :
                    response = {"success" : False , "message" : "Floor not remove , Spot assign to this Floor"};
                    return response;    
                else : 
                    data.pop(index);
        if(check_id) :
            # remove the floor display as well , before removing the floor 
            display_res = DisplayManager.removeDisplayBoard(floor_id);
            print(display_res);

            res = self.adminRepository.remove("floor.json",data);
            if (res["success"]) :
                response = {"success" : True , "message" : "Floor Removed"};
            else : 
                response = {"success" : False , "message" : "Somthing went wrong"};
        else : 
            response = {"success" : False , "message" : "Please check the Id"};

        return response;

    def removeParkingSpot(self,spot_id) :
        #before going to remove the spot check it occupied or not
        data = DataManager.fetchData("floorSpot.json");

        response = None;
        check_id = False;
        remove_spot_info = None;
        for index , spot in enumerate(data,start=0) :
            if (int(spot["id"]) == spot_id) :
                check_id = True;
                if(bool(spot['occupied'])) :
                    response = {"success" : False , "message" : "Spot not remove , Vehicle assign to this Spot"};
                    return response;
                else : 
                    remove_spot_info = data.pop(index);
        
        if(check_id) : 
            # Now if the spot id is correct and not occupied now go for
            # 1. Update the display board by display manager

            display_res = DisplayManager.updateDisplayBoardWhenSpotAddAndRemove(remove_spot_info["floor_id"],remove_spot_info["spot_type"],work_type="remove");
            print(display_res);

            # 2. Un-assign spot from the floor by floor Manager
            floor_res = FloorManager.removeSpotToFloor(remove_spot_info["floor_id"],remove_spot_info["id"]);
            print(floor_res);

            spot_remove_res = self.adminRepository.remove("floorSpot.json",data);
            if (spot_remove_res["success"]) :
                response = {"success" : True , "message" : "Spot Removed"};
            else : 
                response = {"success" : False , "message" : "Somthing went wrong"};
        else : 
            response = {"success" : False , "message" : "Please check the Id"};
        return response;

    def removeparkingAttendent(self,id) : 

        data = DataManager.fetchData("parkingAttendent.json");

        check_id = False;
        for index, attendent in enumerate(data,start=0) :
            if(int(attendent["id"]) == id) :
                check_id = True;
                data.pop(index);

        if(check_id) : 
            # Just release the floor from parking attendent
            floor_res = FloorManager.removeParkingAttendentToFloor(id); 
            print(floor_res);

            res = self.adminRepository.remove("parkingAttendent.json",data);
            if (res["success"]) :
                response = {"success" : True , "message" : "Arrendent Removed"};
            else : 
                response = {"success" : False , "message" : "Somthing went wrong"};
        else : 
            response = {"success" : False , "message" : "Please check the Id"};

        return response;

    def removePanel(self,id) :
        data = DataManager.fetchData("panel.json");

        response = None;
        check_id = False;
        remove_panel_info = None;
        for index , panel in enumerate(data,start=0) :
            if (int(panel["id"]) == id) :
                check_id = True;
                remove_panel_info = data.pop(index);

        if(check_id) : 
            # Just release the floor from panel
            floor_res = FloorManager.removePanelToFloor(remove_panel_info["floor_id"],id); 

            res = self.adminRepository.remove("panel.json",data);
            if (res["success"]) :
                response = {"success" : True , "message" : "Panel Removed"};
            else : 
                response = {"success" : False , "message" : "Somthing went wrong"};
        else : 
            response = {"success" : False , "message" : "Please check the Id"};

        return response;

    def modifyParkingRate(self,first_hour,second_hour,remaining_hour) :
        parking = ParkingRate(first_hour,second_hour,remaining_hour);
        response = self.adminRepository.modifyParkingRate(parking);
        if(response["success"]) :
            return response;
        else :
            return {"success" : False , "message" : "Somthing went wrong"};



