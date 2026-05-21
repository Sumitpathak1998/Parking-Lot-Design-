from managers.data_manager import DataManager;
from response import Response;

class FloorManager : 

    floor_base_path = "floor.json";

    @classmethod
    def assingFloorToParkingAttendent(cls , floor_id , attendent_id) : 
        data = DataManager.fetchData(cls.floor_base_path);

        for floor in data :
            if( int(floor["id"]) == floor_id ) :
                floor["parkingAttendent"] = attendent_id;
                break;

        response : Response = DataManager.updateData(cls.floor_base_path,data);
        if(response.success) :
            response.message = "Attendent Added to Floor"; 

        return response;

    @classmethod
    def assignAndRemovePanelToFloor(cls,floor_id,panel_id,work_type) :
        data = DataManager.fetchData(cls.floor_base_path);

        for floor in data :
            if( int(floor["id"]) == floor_id ) :
                if( work_type == "added") :   
                    floor["entryexitpanel"].append(panel_id);
                else :
                    floor["entryexitpanel"].remove(panel_id);
                break;
        
        response : Response = DataManager.updateData(cls.floor_base_path,data);
        if(response.success) :
            response.message = f"Panel {work_type} to Floor"; 

        return response;

    @classmethod
    def removePanelToFloor(cls,floor_id,panel_id) :
        data = DataManager.fetchData(cls.floor_base_path);

        for floor in data :
            if( int(floor["id"]) == floor_id ) :
                floor["entryexitpanel"].remove(panel_id);
                break;

        response : Response = DataManager.updateData(cls.floor_base_path,data);
        if(response.success) :
            response.message = "Panel Remove to Floor"; 

        return response;

    @classmethod
    def removeAndAddSpotToFloor(cls,floor_id,spot_id,work_type) :
        data = DataManager.fetchData(cls.floor_base_path);

        for floor in data :
            if( int(floor["id"]) == floor_id ) :
                if(work_type == "add") :
                    floor["spot"].append(spot_id);
                else :
                    floor["spot"].remove(spot_id);
                break;

        response : Response = DataManager.updateData(cls.floor_base_path,data);
        if(response.success) :
            response.message = f"Spot {work_type} to Floor"; 

        return response;
        

    @classmethod
    def removeParkingAttendentToFloor(cls, attendent_id) :
        data = DataManager.fetchData(cls.floor_base_path);

        for floor in data :
            if( int(floor["parkingAttendent"]) == attendent_id ) :
                floor["parkingAttendent"] = None;
                break;

        response : Response = DataManager.updateData(cls.floor_base_path,data);
        if(response.success) :
            response.message = "Attendent de-assigm to Floor"; 

        return response;

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
            
            return Response(200,True,data=panel_details);
        else :
            return Response(500,False,"Entry and Exit Panel are not Present");

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
            resposne : Response = DataManager.updateData("floorSpot.json",data);
            resposne.message = "Spot Updated";
            return resposne;
        else :
            return Response(500,False,"Spot Not Found");



