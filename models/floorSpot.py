class FloorSpot: 

    def __init__(self,spot_id,name,spot_type,floor_id) :
        self.id = spot_id;
        self.name = name;
        self.spot_type = spot_type;
        self.occupied = False;
        self.vehicle = None;
        self.floor_id = floor_id;
