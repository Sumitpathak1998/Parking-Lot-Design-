from models.entryAndExitPanel import EntryAndExitPanel;
from managers.data_manager import DataManager;
from managers.floor_manager import FloorManager;
from response import Response;

class EntryAndExitPanelRepository :

    def __init__(self):
        pass;

    def addEntryAndExitPanel(self, entryexitpanle : EntryAndExitPanel) -> Response :
        panel_dict = entryexitpanle.__dict__;
    
        response : Response = DataManager.addData("panel.json", panel_dict);
        response.message = "Panel Added";
        return response; 

    def assignAndRemovePanelToFloor(self, floor_id , panel_id , work_type) -> Response :
        return FloorManager.assignAndRemovePanelToFloor(floor_id,panel_id,work_type);

    def fetchPanelData(self) :
        return DataManager.fetchData("panel.json");

    def remove(self,location,data) : 
        response : Response = DataManager.updateData(location,data);
        if(response.success) : 
            response.message = "EntryExit Panel Remove";    
        return response;

