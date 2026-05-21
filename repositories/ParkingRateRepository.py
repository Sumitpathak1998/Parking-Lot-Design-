from models.parkingRate import ParkingRate;
from response import Response;
from managers.data_manager import DataManager;

class ParkingRateRepository :

    def modifyParkingRate(self,parkingRate : ParkingRate) :

        parking_dict = [];
        parking_dict[0] = parkingRate.__dict__;
        res = DataManager.updateData("parkingRate.json", parking_dict);
        res.message = "Parking Rate Modified";
        return res;