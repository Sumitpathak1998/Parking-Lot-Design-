import json;

class DataManager : 

    __base_location = "storage/";

    @classmethod
    def addData(cls,location,new_data) :

        try : 
            with open(cls.__base_location+location, "r") as file : 
                data = json.load(file);
        except (FileNotFoundError , json.JSONDecodeError) : 
                data = [];
                
        data.append(new_data);
        with open(cls.__base_location+location, "w") as file : 
            json.dump(data,file);

        return {"success" : True};

    @classmethod
    def fetchData(cls,location) -> list :
        try : 
            with open(cls.__base_location+location , "r") as file : 
                data = json.load(file); 
        except (FileNotFoundError , json.JSONDecodeError) : 
                data = [];
        return data;

    @classmethod
    def checkDuplicateData(cls,location,check_id) -> bool :
        id_present = False;
        try : 
            with open(cls.__base_location+location , "r") as file : 
                data = json.load(file);
                for item in data:
                    if( int(item["id"]) == check_id) :
                        id_present = True;
                        break;
            return id_present; 
        # why Json Decoded error is importan  becz it handle the empty case as well
        except (FileNotFoundError , json.JSONDecodeError) : 
            return id_present;

    @classmethod
    def updateData(cls,location,data) :
        try : 
            with open(cls.__base_location+location, "w") as file : 
                json.dump(data,file);
                return {"success" : True};
        except (FileNotFoundError , json.JSONDecodeError) as e : 
                return {"success" : False , "message" : "Data not Updated" }; 
        