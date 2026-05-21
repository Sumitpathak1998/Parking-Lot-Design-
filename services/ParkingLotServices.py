from models.parking_lot import ParkingLot; 
from managers.data_manager import DataManager;
from models.user import User;
from models.admin import Admin;
from response import Response;
from repositories.ParkingLotRepository import ParkingLotRepository;

class ParkingLotServices : 

    def __init__(self):
        self.parkingLotRepository = ParkingLotRepository();

    def createParkingLot(self, user : User , parkingLot : ParkingLot) :
        if (isinstance(user ,Admin)) :
            #check Parking lot id is present or not 
            check_res = DataManager.checkDuplicateData("parkingLot.json" , parkingLot.id);
            
            if(check_res) :
                return Response(409,False,f"Parking lot with = {parkingLot.id} Already Added");
            
            response : Response = self.parkingLotRepository.createParkingLot(parkingLot); 
            return response;
        else :
            return Response(403,False,message="Only Admin has access to create Parking Lot");