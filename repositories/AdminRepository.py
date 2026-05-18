from models.admin import Admin;
from models.parking_lot import ParkingLot;
from models.floor import Floor;
from models.floorSpot import FloorSpot;
from models.displayBoard import DisplayBoard;
from models.parkingAttendent import ParkingAttendent;
from models.entryAndExitPanel import EntryAndExitPanel;
from managers.data_manager import DataManager;
from models.parkingRate import ParkingRate;

class AdminRepository : 

    def createAdmin(self , id : int , name : str, email : str) -> Admin :
        a1 = Admin(id,name,email);
        admin_dict = a1.__dict__;     
        
        DataManager.addData("admin.json",admin_dict);
        return a1; 

    def createParkingLot(self, id : int , name : str) -> ParkingLot : 
        p1 = ParkingLot(id,name);
        pLot_dict = p1.__dict__;

        DataManager.addData("parkingLot.json",pLot_dict);
        return p1;

    def addFloor(self, id : int , name : str) -> Floor :
        f1 = Floor(id,name);
        floor_dict = f1.__dict__;

        DataManager.addData("floor.json",floor_dict);
        return f1;

    def createFloorDisplay( self, floor) :
        display = DisplayBoard(floor.id,floor.name);    
        dis_dict = display.__dict__;

        DataManager.addData("floorDisplay.json",dis_dict);
        return display;

    def CreateSpot(self, spot_id : int , name : str ,spot_type : str , floor_id : int) :

        sp1 = FloorSpot(spot_id,name,spot_type,floor_id);
        spot_dict = sp1.__dict__;

        DataManager.addData("floorSpot.json",spot_dict);
        return sp1;

    def addParkingAttendent(self,id : int , name : str ) : 
        pa1 = ParkingAttendent(id,name);
        pa_dict = pa1.__dict__;
    
        DataManager.addData("parkingAttendent.json",pa_dict);
        return pa1;

    def addEntryAndExitPanel(self, id : int , name : str , panel_type : str , floor_id : int) :
        panel = EntryAndExitPanel(id,name,panel_type,floor_id);
        panel_dict = panel.__dict__;
    
        DataManager.addData("panel.json", panel_dict);
        return panel;

    def modifyParkingRate(self,parkingRate : ParkingRate) :

        parking_dict = parkingRate.__dict__;
        DataManager.addData("parkingRate.json", parking_dict);
        return {"success" : True , "message" : "Parking Rate Modified"};

    def remove(self,location,data) : 
        DataManager.updateData(location,data);
        return {"success" : True};

    def fetchDataBasisOfId(self,location,id) :
        data = DataManager.fetchData(location);

        resposne = None;
        for el in data :
            if( int(el["id"]) == id ) :
                resposne = el;
                break;
        return resposne;

