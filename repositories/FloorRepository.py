from models.floor import Floor;
from managers.data_manager import DataManager;
from models.displayBoard import DisplayBoard;
from response import Response;

class FloorRepository : 

    def __init__(self):
        pass;

    def addFloor(self, floor : Floor) -> Floor :
        floor_dict = floor.__dict__;
        res = DataManager.addData("floor.json",floor_dict);
        res.message = "New Floor Added";            
        return res;

    def createFloorDisplay(self, floor) :
        display = DisplayBoard(floor.id,floor.name);    
        dis_dict = display.__dict__;

        res : Response = DataManager.addData("floorDisplay.json",dis_dict);
        if(res.success) :
            res.message = "Display Board Created"
            return res;
        else : 
            return res;

    def remove(self,location,data) : 
        response : Response = DataManager.updateData(location,data);
        if(response.success) : 
            response.message = "Floor Remove from System";    
        return response;