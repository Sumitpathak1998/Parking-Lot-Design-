from models.parking_lot import ParkingLot;
from response import Response;
from managers.data_manager import DataManager;

class ParkingLotRepository : 

    def __init__(self):
        pass;

    def createParkingLot(self, parkingLot : ParkingLot) -> Response : 
        pLot_dict = parkingLot.__dict__;

        response = DataManager.addData("parkingLot.json",pLot_dict);
        response.message = "Parking Lot Created";
        return response;