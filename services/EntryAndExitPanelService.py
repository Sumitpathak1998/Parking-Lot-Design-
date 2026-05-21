from models.admin import Admin;
from models.user import User;
from models.entryAndExitPanel import EntryAndExitPanel;
from managers.data_manager import DataManager;
from response import Response;
from repositories.EntryAndExitPanelRepository import EntryAndExitPanelRepository;

class EntryAndExitPanelService :

    def __init__(self):
        self.entryAndExitPanelRepository = EntryAndExitPanelRepository();

    def addEntryAndExitPanel(self, user : User , entryexitpanel : EntryAndExitPanel) :
        if(isinstance(user,Admin)) :

            # check Panel is present or not 
            check_res = DataManager.checkDuplicateData("panel.json" , entryexitpanel.id);
            
            if(check_res) :
                return Response(409,False,f"Panel with id = {entryexitpanel.id} Already Added");
        
            # add the entry exit panel 
            response : Response = self.entryAndExitPanelRepository.addEntryAndExitPanel(entryexitpanel);
            
            # assign entry and exit panel to floor 
            floor_res = self.entryAndExitPanelRepository.assignAndRemovePanelToFloor(entryexitpanel.floor_id,entryexitpanel.id,work_type="added");
            print(floor_res.message);
        
            return response;
        else : 
            return Response(403,False,message="Only Admin has access to create Panel");

    def removePanel(self,user,id) :
        response : Response;
        if(isinstance(user, Admin)) :

            data = self.entryAndExitPanelRepository.fetchPanelData();

            check_id = False;
            remove_panel_info = None;
            for index , panel in enumerate(data,start=0) :
                if (int(panel["id"]) == id) :
                    check_id = True;
                    remove_panel_info = data.pop(index);

            if(check_id) : 
                # Just release the floor from panel
                floor_res = self.entryAndExitPanelRepository.assignAndRemovePanelToFloor(remove_panel_info["floor_id"],id,work_type="remove"); 
                print(floor_res.message);

                response : Response = self.entryAndExitPanelRepository.remove("panel.json",data);
                return response;
            else : 
                return Response(400,False,message="Please check the Id");
        else : 
            return Response(403,False,message="Only Admin has access to remove Panel");
