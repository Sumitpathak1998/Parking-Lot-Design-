from models.admin import Admin;
from models.parking_lot import ParkingLot;
from managers.data_manager import DataManager;
from response import Response;

class AdminRepository : 

    def createAdmin(self , admin : Admin) -> Response :
        admin_dict = admin.__dict__;     
        
        response = DataManager.addData("admin.json",admin_dict);
        response.message = "Admin added";
        return response; 
