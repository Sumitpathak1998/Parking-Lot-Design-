from services.AdminService import AdminService;
from models.admin import Admin;

class AdminController : 

    def __init__(self):
        self.adminService = AdminService();    
    
    def createAdmin(self, id : int , name : str , email : str) :
        admin = Admin(id,name,email);
        return self.adminService.CreateAdmin(admin);


