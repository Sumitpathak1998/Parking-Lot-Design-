from managers.data_manager import DataManager;

class FloorManager : 

    floor_base_path = "floor.json";

    @classmethod
    def assignNewSpotToFloor(cls, floor_id , spot_id) :
        data = DataManager.fetchData(cls.floor_base_path);

        for floor in data :
            if( int(floor["id"]) == floor_id ) :
                floor["spot"].append(spot_id);
                break;

        res = DataManager.updateData(cls.floor_base_path,data);
        if(res["success"]) :
            return "Spot Added to Floor"; 
        else :
            return res["message"];

    @classmethod
    def assingFloorToParkingAttendent(cls , floor_id , attendent_id) : 
        data = DataManager.fetchData(cls.floor_base_path);

        for floor in data :
            if( int(floor["id"]) == floor_id ) :
                floor["parkingAttendent"] = attendent_id;
                break;

        res = DataManager.updateData(cls.floor_base_path,data);
        if(res["success"]) :
            return "Attendent Added to Floor"; 
        else :
            return res["message"];

    @classmethod
    def assignPanelToFloor(cls,floor_id,panel_id) :
        data = DataManager.fetchData(cls.floor_base_path);

        for floor in data :
            if( int(floor["id"]) == floor_id ) :
                floor["entryexitpanel"].append(panel_id);
                break;

        res = DataManager.updateData(cls.floor_base_path,data);
        if(res["success"]) :
            return "Panel Added to Floor"; 
        else :
            return res["message"];

    @classmethod
    def removeSpotToFloor(cls, floor_id , spot_id) :
        data = DataManager.fetchData(cls.floor_base_path);

        for floor in data :
            if( int(floor["id"]) == floor_id ) :
                floor["spot"].remove(spot_id);
                break;

        res = DataManager.updateData(cls.floor_base_path,data);
        if(res["success"]) :
            return "Spot Remove to Floor"; 
        else :
            return res["message"];

    @classmethod
    def removeParkingAttendentToFloor(cls, attendent_id) :
        data = DataManager.fetchData(cls.floor_base_path);

        for floor in data :
            if( int(floor["parkingAttendent"]) == attendent_id ) :
                floor["parkingAttendent"] = None;
                break;

        res = DataManager.updateData(cls.floor_base_path,data);
        if(res["success"]) :
            return "Attendent de-assigm to Floor"; 
        else :
            return res["message"];

    @classmethod
    def removePanelToFloor(cls,floor_id,panel_id) :
        data = DataManager.fetchData(cls.floor_base_path);

        for floor in data :
            if( int(floor["id"]) == floor_id ) :
                floor["entryexitpanel"].remove(panel_id);
                break;

        res = DataManager.updateData(cls.floor_base_path,data);
        if(res["success"]) :
            return "Panel Remove to Floor"; 
        else :
            return res["message"];

    @classmethod 
    def fetchEntryAndExitPanel(cls,floor_id) :
        data = DataManager.fetchData(cls.floor_base_path);

        panel_info = None;
        for floor in data :
            if( int(floor["id"]) == floor_id ) :
                panel_info = floor["entryexitpanel"];
                break;

        if (len(panel_info) > 1 ) :
            panel_details = {};
            panel_data = DataManager.fetchData("panel.json");

            for panel in panel_data : 
                if (panel["id"] in panel_info) :
                    panel_details[panel["panel_type"]] = panel["id"];
            
            return {"success" : True , "data" : panel_details };
        else :
            return {"success" : False , "message" : "Entry and Exit Panel are not Present"};

    @classmethod
    def UpdateFloorSpot(cls,spot_id,occupied_type = "assign") :
        data = DataManager.fetchData("floorSpot.json");

        check = False;
        for spot in data :
            if( int(spot["id"]) ==  spot_id) :
                check = True;
                if (occupied_type == "assign") :
                    spot["occupied"] = True;
                else : 
                    spot["occupied"] = False;
                break;

        if check :    
            res = DataManager.updateData("floorSpot.json",data);
            return {"success" : True , "message" : "Spot Updated"};
        else :
            return {"success" : False , "message" : "Spot not found"};



