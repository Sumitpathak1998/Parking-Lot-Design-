from models.user import User;
from models.admin import Admin;
from models.floor import Floor;
from response import Response;
from managers.data_manager import DataManager;
from repositories.FloorRepository import FloorRepository;
from managers.display_manager import DisplayManager;

class FloorService :

    def __init__(self):
        self.floorRepository = FloorRepository();
    
    def addFloor(self, floor : Floor,user : User) :
        if (isinstance(user , Admin)) :
            # check floor is present or not 
            check_res = DataManager.checkDuplicateData("floor.json" , floor.id);
            
            if(check_res) :
                return Response(409,False,f"Floor_id = {floor.id} Already Added");
        
            response : Response = self.floorRepository.addFloor(floor);
            
            if(response.success) : 
                # create the display of floor 
                self.CreateFloorDisplay(floor);
            
            return response;
        else : 
            return Response(403,False,message="Only Admin has access to create floor");
    
    def CreateFloorDisplay(self, floor : Floor ) : 
        self.floorRepository.createFloorDisplay(floor);
    
    def removeFloor(self,floor_id , user : User) : 

        response : Response;

        if(isinstance(user , Admin)) : 
            #check if any spot assign this floor or not
            data = self.fetchFloorData(user,"floor.json");
            
            check_id = False;
            for index, floor in enumerate(data,start=0) : 
                if(int(floor['id']) == floor_id) :
                    check_id = True;
                    check_len_spot = len(list(floor["spot"]));
                    if (check_len_spot > 0) :
                        return Response(400,False,"Floor not remove , Spot assign to this Floor");    
                    else : 
                        data.pop(index);
            if(check_id) :
                # remove the floor display as well , before removing the floor 
                display_res : Response = DisplayManager.removeDisplayBoard(floor_id);
                print(display_res.message);

                response = self.floorRepository.remove("floor.json",data);
                return response;
            else : 
                return Response(400,False,message="Please check the Id");
        else : 
            return Response(403,False,message="Only Admin has access to remove floor");

    def fetchFloorData(self,user,location = "floor.json") :
        #Only admin can able to fetch the data 
        if(isinstance(user,Admin)) :
            return self.floorRepository.fetchData(location);
        else :
            return Response(403,False,message="Only Admin has access to fetch Floor info");



        
        
        