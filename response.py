class Response : 

    def __init__(self,statusCode : int ,success: bool , message : str = "" , data = "" ):
        self.statusCode = statusCode;
        self.success = success;
        self.message = message;
        self.data = data;
