from models.user import User;
from models.parking_lot import ParkingLot;
from services.ParkingLotServices import ParkingLotServices;

class ParkingLotController : 

    def __init__(self):
        self.parkingLotServices = ParkingLotServices();

    def createParkingLot(self, id : int , name : str , user : User) :
        parkingLot = ParkingLot(id,name);
        return self.parkingLotServices.createParkingLot(user,parkingLot); 