from models.admin import Admin;
from repositories.AdminRepository import AdminRepository;
from managers.data_manager import DataManager;
from response import Response;

class AdminService :   

    def __init__(self) :
        self.adminRepository = AdminRepository();

    def CreateAdmin(self, admin : Admin) :
        # check Admin Id is present or not
        check_res = DataManager.checkDuplicateData("admin.json" , admin.id);
        if(check_res) :
            return Response(409,False,f"admin with id = {admin.id} Already Added");
        response : Response = self.adminRepository.createAdmin(admin);
        return response;




