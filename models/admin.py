from models.user import User;

class Admin(User) :

    def __init__(self,id : int , name : str , email : str ) :
        super().__init__(id,name,email);