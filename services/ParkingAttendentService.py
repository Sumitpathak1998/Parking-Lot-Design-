from models.user import User;
from models.admin import Admin;
from models.parkingAttendent import ParkingAttendent;
from response import Response;
from managers.data_manager import DataManager;
from repositories.ParkingAttendentRepository import ParkingAttendentRepository;


class ParkingAttendentService : 

    def __init__(self):
        self.parkingAttendentRepository = ParkingAttendentRepository(); 

    def addParkingAttendent(self, user : User , parkingAttendent : ParkingAttendent,  floor_id : int) :
        
        if( isinstance(user , Admin)) :
            # check Attendent is present or not 
            check_res = DataManager.checkDuplicateData("parkingAttendent.json" , id);
            
            if(check_res) :
                return Response(409,False,f"Parking Attendent = {parkingAttendent.id} Already Added");

            # add the parking attwndent
            response : Response = self.parkingAttendentRepository.addParkingAttendent(parkingAttendent);

            # Assign the floor to Parking Attendent by floor manager
            self.parkingAttendentRepository.assingFloorToParkingAttendent(floor_id,parkingAttendent.id);
        
            return response;
        else : 
            return Response(403,False,message="Only Admin has access to add Parking Attendent");

    def removeparkingAttendent(self,user : User , id : int) : 

        if (isinstance(user,Admin)) :
            data = DataManager.fetchData("parkingAttendent.json");

            check_id = False;
            for index, attendent in enumerate(data,start=0) :
                if(int(attendent["id"]) == id) :
                    check_id = True;
                    data.pop(index);

            if(check_id) : 
                # Just release the floor from parking attendent
                floor_res = self.parkingAttendentRepository.removeParkingAttendentToFloor(id); 
                print(floor_res.message);

                response : Response = self.parkingAttendentRepository.remove("parkingAttendent.json",data);
                return response;
            else : 
                return Response(400,False,message="Please check the Id");
        else : 
            return Response(403,False,message="Only Admin has access to remove Parking Attendent");
