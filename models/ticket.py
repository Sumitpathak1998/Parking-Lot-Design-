class Ticket : 

    def __init__(self,id,vehicleNumber,vehicleType,floor_id,floorSpot,entryPanel,exitPanel,entryTime,spotId,exitTime = None , totalAmount = 0, paymentStatus = False , status = "active") : 
        self.id = id;
        self.vehicleNumber = vehicleNumber;
        self.vehicleType = vehicleType;
        self.floor_id = floor_id;
        self.floorSpot = floorSpot;
        self.entryPanel = entryPanel;
        self.exitPanel = exitPanel;
        self.entryTime = entryTime;
        self.spotId = spotId;
        self.exitTime = exitTime;
        self.totalAmount = totalAmount;
        self.paymentStatus = paymentStatus;
        self.status = status;

    @classmethod
    def from_dict(cls, data):
        # what this cls() method will do extract values from dict and pass them as a argument in constructor and return object 
        return cls(
            id=data["id"],
            vehicleNumber=data["vehicleNumber"],
            vehicleType=data["vehicleType"],
            floor_id=data["floor_id"],
            floorSpot=data["floorSpot"],
            entryPanel=data["entryPanel"],
            exitPanel=data["exitPanel"],
            entryTime=data["entryTime"],
            spotId = data["spotId"],
            exitTime=data["exitTime"],
            totalAmount=data["totalAmount"],
            paymentStatus=data["paymentStatus"],
            status=data["status"]
        )
