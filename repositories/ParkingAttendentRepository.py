from models.parkingAttendent import ParkingAttendent;
from managers.data_manager import DataManager;
from managers.floor_manager import FloorManager;
from response import Response;

class ParkingAttendentRepository : 

    def addParkingAttendent(self, parkingAttendent : ParkingAttendent) : 
        
        pa_dict = parkingAttendent.__dict__;
        response : Response = DataManager.addData("parkingAttendent.json",pa_dict);
        response.message = "Parking Attendent Added";
        return response;

    def assingFloorToParkingAttendent(self,floor_id,parkingAttendent_id) :
        return FloorManager.assingFloorToParkingAttendent(floor_id,parkingAttendent_id);

    def remove(self,location,data) : 
        response : Response = DataManager.updateData(location,data);
        if(response.success) : 
            response.message = "Parking Attendent Remove";    
        return response;

    def removeParkingAttendentToFloor(self,id) :
        return FloorManager.removeParkingAttendentToFloor(id);