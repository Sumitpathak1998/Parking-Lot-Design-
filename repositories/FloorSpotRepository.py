from models.floorSpot import FloorSpot;
from managers.data_manager import DataManager;
from managers.floor_manager import FloorManager;
from managers.display_manager import DisplayManager;
from response import Response;

class FloorSpotRepository : 

    def __init__(self):
        pass;

    def CreateSpot(self, floorSpot : FloorSpot) :
        spot_dict = floorSpot.__dict__;

        response : Response = DataManager.addData("floorSpot.json",spot_dict);
        response.message = "Floor spot created";
        return response;

    def removeAndAddSpotToFloor(self,floor_id,spot_id,work_type) :
        return FloorManager.removeAndAddSpotToFloor(floor_id,spot_id,work_type);

    def updateDisplayBoardWhenSpotAddAndRemove(self,floor_id,spot_type,work_type) :
        return DisplayManager.updateDisplayBoardWhenSpotAddAndRemove(floor_id,spot_type,work_type);

    def fetchFloorSpotData(self,location="floorSpot.json") :
        return DataManager.fetchData(location);

    def remove(self,location,data) : 
        response : Response = DataManager.updateData(location,data);
        if(response.success) : 
            response.message = "Floor Spot Remove from System";    
        return response;

