from managers.data_manager import DataManager;
from response import Response;

class DisplayManager :

    @classmethod 
    def updateDisplayBoardWhenSpotAdd(cls, floor_id,spot_type) :
        data = DataManager.fetchData("floorDisplay.json");
        if (len(data) == 0) :
            return "Floor Display not present";

        for display in data :
            if(int(display["floor_id"]) == floor_id) :
                display["total_spot"][spot_type] += 1;
                break;

        res = DataManager.updateData("floorDisplay.json",data);
        if(res["success"]) :
            return "Display Updated"; 
        else :
            return res["message"];

    @classmethod 
    def updateDisplayBoardWhenSpotRemove(cls, floor_id,spot_type) :
        data = DataManager.fetchData("floorDisplay.json");
        if (len(data) == 0) :
            return "Floor Display not present";

        for display in data :
            if(int(display["floor_id"]) == floor_id) :
                display["total_spot"][spot_type] -= 1;
                break;

        res = DataManager.updateData("floorDisplay.json",data);
        if(res["success"]) :
            return "Display Updated"; 
        else :
            return res["message"];

    @classmethod
    def removeDisplayBoard(cls,floor_id) :
        data = DataManager.fetchData("floorDisplay.json");
        if (len(data) == 0) :
            return "Floor Display not present";

        for index, display in enumerate(data,start=0)  :
            if(int(display["floor_id"]) == floor_id) :
                data.pop(index);
                break;

        res : Response = DataManager.updateData("floorDisplay.json",data);
        if(res.success) :
            res.message = "Display Removed";
        return res;

    @classmethod 
    def updateDisplayBoardWhenSpotOccupiedAndRelase(cls, floor_id,spot_type,work_type = "occupied") :
        data = DataManager.fetchData("floorDisplay.json");
        if (len(data) == 0) :
            return "Floor Display not present";

        for display in data :
            if(int(display["floor_id"]) == floor_id) :
                if(work_type == "occupied") :
                    display["occupied_spot"][spot_type] += 1;
                else :
                    display["occupied_spot"][spot_type] -= 1;
                break;

        res = DataManager.updateData("floorDisplay.json",data);
        if(res["success"]) :
            return {"success" : True , "message" : "Display Updated"}; 
        else :
            return {"success" : True , "message" : res["message"]} ;
