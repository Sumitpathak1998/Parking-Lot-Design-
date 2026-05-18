from datetime import datetime;
from zoneinfo import ZoneInfo;
from managers.data_manager import DataManager;
import math;

class PaymentManager : 

    @classmethod
    def calculateTimeDurationInHour(cls,entry_time) :

        #parse the date from string to dateTime 
        entry_datetime = datetime.strptime(entry_time,"%d-%m-%Y %H:%M:%S");
        india_tz = ZoneInfo("Asia/Kolkata");
        entry_datetime = entry_datetime.replace(tzinfo=india_tz);        
        
        current_datetime = datetime.now(ZoneInfo("Asia/Kolkata"));

        #get the time differnece
        time_difference = current_datetime - entry_datetime;
        total_hours = time_difference.total_seconds() / 3600;

        return {"total_hour" : math.ceil(total_hours) , "exit_time" : current_datetime.strftime("%d-%m-%Y %H:%M:%S") };

    @classmethod 
    def calculateParkingCharges(cls,hours) :

        # fetch the parking rate (we assume that rate is set) 
        parkingRate = DataManager.fetchData("parkingRate.json");

        total = 0;
        for hour in range(1,hours+1) :
            if hour == 1 :
                total += float(parkingRate[0]["first_hour"]);
            elif hour in [2,3] :
                total += float(parkingRate[0]["second_third_hour"]);
            else :
                total += float(parkingRate[0]["remaining_hour"]);

        return total;

