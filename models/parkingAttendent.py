from models.user import User;

class ParkingAttendent(User) : 

    def __init__(self,id,name) :
        super().__init__(id,name);
        self.floorAssign = True;