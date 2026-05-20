from managers.data_manager import DataManager;
from models.admin import Admin;
from models.floorSpot import FloorSpot;
from models.user import User;
from response import Response;
from repositories.FloorSpotRepository import FloorSpotRepository;

class FloorSpotService : 

    def __init__(self):
        self.floorSpotRepository = FloorSpotRepository();

    def CreateSpot(self, user : User , floorSpot : FloorSpot) :

        if (isinstance(user,Admin)) :
            # check spot is present or not 
            check_res = DataManager.checkDuplicateData("floorSpot.json" , floorSpot.id);
            
            if(check_res) :
                return Response(409,False,f"Floor Spot = {floorSpot.id} Already Added"); return "Floor Spot Already Added with same ID";

            response : Response = self.floorSpotRepository.CreateSpot(floorSpot);

            #Update floor with the Spot by Spot Manager like Assign spot to floor 
            spotAddedRes = self.floorSpotRepository.removeAndAddSpotToFloor(floorSpot.floor_id,floorSpot.id,work_type="add");
            print(spotAddedRes.message);

            #Update disply of floor by display manager
            disUpdateRes = self.floorSpotRepository.updateDisplayBoardWhenSpotAddAndRemove(floorSpot.floor_id,floorSpot.spot_type,work_type="add");
            print(disUpdateRes.message);

            return response;
        else : 
            return Response(403,False,message="Only Admin has access to create Spot");

    
    def removeParkingSpot(self,user,spot_id) :
        if(isinstance(user,Admin)) :
            #before going to remove the spot check it occupied or not
            data = self.floorSpotRepository.fetchFloorSpotData();

            check_id = False;
            remove_spot_info = None;
            for index , spot in enumerate(data,start=0) :
                if (int(spot["id"]) == spot_id) :
                    check_id = True;
                    if(bool(spot['occupied'])) :
                        return Response(400,False,"Spot not remove , Vehicle assign to this Spot");
                    else : 
                        remove_spot_info = data.pop(index);
            
            if(check_id) : 
                # Now if the spot id is correct and not occupied now go for
                # 1. Update the display board by display manager

                display_res = self.floorSpotRepository.updateDisplayBoardWhenSpotAddAndRemove(remove_spot_info["floor_id"],remove_spot_info["spot_type"],work_type="remove");
                print(display_res.message);

                # 2. Un-assign spot from the floor by floor Manager
                floor_res = self.floorSpotRepository.removeAndAddSpotToFloor(remove_spot_info["floor_id"],remove_spot_info["id"],work_type="remove");
                print(floor_res.message);
                
                response = self.floorSpotRepository.remove("floorSpot.json",data);
                return response;
            else : 
                return Response(400,False,message="Please check the Id");
        else : 
            return Response(403,False,message="Only Admin has access to remove floor Spot");
