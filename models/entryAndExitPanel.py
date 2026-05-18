from models.user import User;

class EntryAndExitPanel(User): 

    def __init__(self,id,name,panel_type,floor_id):
        super().__init__(id,name);
        self.panel_type = panel_type;
        self.floor_id = floor_id;