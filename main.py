from controller.AdminController import AdminController;
from controller.EntryController import EntryController;
from controller.ExitController import ExitController;
from controller.ParkingRateController import ParkingRateController;
from controller.FloorController import FloorController;
from models.admin import Admin;

class Main : 

    def __init__(self) :
        self.admin = AdminController();
        self.entry = EntryController();
        self.exit = ExitController();
        self.floor = FloorController();
        self.parkingRate = ParkingRateController();
        self.initlizeAdmin();
        self.initlizeParkingLot();
        self.operation();
    
    #initlize Parking lot
    def initlizeParkingLot(self) :
        p_lot = self.admin.createParkingLot(1,"P&M Mall Parking");
        print(p_lot);
    
    #initlize Admin 
    def initlizeAdmin(self) :
        response = self.admin.createAdmin(1,"Sumit","sumitpath901@gmail.com");
        print(f"{response}");

    def operation(self) :
        
        while True : 
            print(""" Select Operation
              1. Work as Admin 
              2. Work as Parking Attendent.
              3. Exit""");
            select = int(input("Select the number : "));
            match select :
                case 1: 
                    self.adminOperation();
                case 2:
                    self.parkingAttendentOpeartion();
                case 3: 
                    print("Application Closed");
                    break;
                case _:
                    print("Invalid Selection");

    # Perform admin operation
    def adminOperation(self) :

        while True : 
            print("""Start the Operation of Admin
            1. Add Parking Floor
            2. Add Parking Spot
            3. Remove Parking Floor
            4. Remove Parking Spot
            5. Add Parking Attendent
            6. Remove Parking Attendent
            7. Add Floor Panel
            8. Remove Floor Panel
            9. Modify Parking Rate      
            10. Back to Main Menu """);
            admin_user = Admin(1,"Sumit","sumitpathak");
            select = int(input("Select the Number for Perform Operation : "));
            match select : 
                case 1 : 
                    self.floor.addFloor(admin_user);
                case 2 :
                    self.admin.createSpot();
                case 3 : 
                    self.floor.removeFloor(admin_user);
                case 4 : 
                    self.admin.removeParkingSlot();
                case 5 : 
                    self.admin.addParkingAttendent();
                case 6 :
                    self.admin.removeParkingAttendent();
                case 7 : 
                    self.admin.addPanel();
                case 8 : 
                    self.admin.removePanel();
                case 9 : 
                    self.parkingRate.modifyParkingRate(admin_user);
                case 10:
                    print("Returning to Main Menu...");
                    break;
                case _:
                    print("Invalid Selection")
    
    #perform parkingAttendent Opration
    def parkingAttendentOpeartion(self) :
        
        while True : 
            print(""" Start the Opearion of Parking Attendant
              1. Want to Entry the vechicle.
              2. Want to Exit the Vehicle.
              3. Return to Main Menu""");
            
            select = int(input("Enter the Number for Perform Operation : "));
            match select : 
                case 1 : 
                    self.entry.generateParkingTicket();
                case 2 : 
                    self.exit.scanAndcalculateCharges();
                case 3:
                    print("Returning to Main Menu...");
                    break;
                case _:
                    print("Invalid Selection");

m1 = Main();


