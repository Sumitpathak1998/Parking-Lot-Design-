from models.spotType import SpotType;

class DisplayBoard : 

    def __init__(self, floor_id , floor_name):
        self.floor_id = floor_id;
        self.floor_name = floor_name;
        self.total_spot = {
            SpotType.COMPACT.value : 0,
            SpotType.LARGE.value : 0,
            SpotType.MOTORCYCLE.value : 0,
            SpotType.ELECTRIC.value : 0
        };
        self.occupied_spot = {
            SpotType.COMPACT.value : 0,
            SpotType.LARGE.value : 0,
            SpotType.MOTORCYCLE.value : 0,
            SpotType.ELECTRIC.value : 0
        };