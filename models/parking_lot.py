from models.user import User;

class ParkingLot(User) : 

    def __init__(self,id,name):
        super().__init__(id,name);