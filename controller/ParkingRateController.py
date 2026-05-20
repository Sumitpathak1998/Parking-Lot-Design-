from models.parkingRate import ParkingRate;
from response import Response;
from services.ParkingRateServices import ParkingRateServices;
from models.user import User;

class ParkingRateController : 

    def __init__(self):
        self.parkingRate = ParkingRate();
        self.parkingRateService = ParkingRateServices();
        

    def modifyParkingRate(self, user : User) :
        # controller only take input , no business login will be implemented here like (check user is admin or not)

        self.parkingRate.first_hour = float(input("Enter the first hour rate : "));
        self.parkingRate.second_third_hour = float(input("Enter the second and third hour rate : "));
        self.parkingRate.remaining_hour = float(input("Enter the remaining hour rate : "));

        response = self.parkingRateService.modifyParkingRate(self.parkingRate,user); 
        print(response.message);

            



