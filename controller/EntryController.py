from models.vehicleType import VehicleType;
from services.EntryService import EntrySecvice;
from models.user import User;
from datetime import datetime;
from zoneinfo import ZoneInfo;
from response import Response;

class EntryController :

    def __init__(self) :
        self.entrySecvice = EntrySecvice();

    def generateParkingTicket(self,user : User) :
        vehicle_number = input("Enter the vehicle number : ");

        #select vehicle Type
        vehicle_type = list(VehicleType);
        print("Select Vehicle Type from List :");
        for index , type in enumerate(vehicle_type,start=1) :
            print(f"{index}.{type.name}");
        choice_type = int(input("Select the Vehicle Type Number: "));

        # entrytime 
        current_time = datetime.now(ZoneInfo("Asia/Kolkata"));
        #formate the time in DD-MM-YYYY HH:MM:SS
        entry_time = current_time.strftime("%d-%m-%Y %H:%M:%S");

        response : Response = self.entrySecvice.generateParkingTicket(user,vehicle_number,vehicle_type[choice_type-1].value,entry_time);

        if not response.success :
            print(response.message);
        else :
            ticket_dict = response.data.__dict__;
            print("Ticket Info : ");
            for el in ticket_dict : 
                print(f"{el} : {ticket_dict[el]}");




        