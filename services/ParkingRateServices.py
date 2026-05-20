from models.parkingRate import ParkingRate;
from models.user import User;
from models.admin import Admin;
from response import Response;
from repositories.ParkingRateRepository import ParkingRateRepository;

class ParkingRateServices : 

    def __init__(self):
        self.parkingRateRepository = ParkingRateRepository();

    def modifyParkingRate(self, rates : ParkingRate , user : User) :
        if( isinstance(user , Admin)) :
            return self.parkingRateRepository.modifyParkingRate(rates); 
        else : 
            return Response(403,False,message="Only Admin has access to modify rate");