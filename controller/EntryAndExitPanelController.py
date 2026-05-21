from models.user import User;
from models.panelType import PanelType;
from models.entryAndExitPanel import EntryAndExitPanel;
from services.FloorService import FloorService;
from services.EntryAndExitPanelService import EntryAndExitPanelService;

class EntryAndExitController : 

    def __init__(self):
        self.floorService = FloorService();
        self.entryAndExitPanelService = EntryAndExitPanelService(); 

    def addPanel(self , user) : 
        panel_id = int(input("Enter the Panel Id : "));
        name = input("Enter the Panel Name : ");    
        
        # select Panel Type

        panel_type = list(PanelType); 
        print("Select Panel Type from List :");
        for index , type in enumerate(panel_type,start=1) :
            print(f"{index}.{type.name}");
        choice_type = int(input("Select the Panel Type Number: "));

        #select Floor 
        data = self.floorService.fetchFloorData(user);
        
        if(len(data) == 0) :
            return "Please insert the Floor first";
    
        print("Select Floor from List : ");
        for floor in data :
            print(f"{floor["id"]}.{floor["name"]}");
        floor_id = int(input("Select Floor Id : "));
    
        entryAndExitPanel = EntryAndExitPanel(panel_id,name,panel_type[choice_type - 1].value,floor_id);
        response = self.entryAndExitPanelService.addEntryAndExitPanel(user,entryAndExitPanel);
        print(response.message);

    def removePanel(self,user) :
        panel_id = int(input("Enter the Panel Id : "));
        response = self.entryAndExitPanelService.removePanel(user,panel_id);
        print(response.message);