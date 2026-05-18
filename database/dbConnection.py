import mysql.connector as DB;
import os;
from dotenv import load_dotenv;

class DBConnection :

    #load variable from .env
    load_dotenv();

    __dbHost = os.getenv("DB_HOST");
    __dbUSer = os.getenv("DB_USER");
    __dbPassword = os.getenv("DB_PASSWORD");
    __dbDatabase = os.getenv("DB_DATABASENAME");
    __dbPort = os.getenv("DB_PORT");

    @classmethod
    def get_connection(cls) :
        try :
            conn = DB.connect(
            host= cls.__dbHost,
            user= cls.__dbUSer,
            password= cls.__dbPassword,
            database= cls.__dbDatabase,
            port = cls.__dbPort
        )

            print("Connection is Establish :",conn);
            return conn;
        except DB.Error as e :
            print(f"Database Error Occured : {e}");
            print(f"Error Code : {e.errno}");
            return None;
        except Exception as e :
            print(f"Unexcepted Error Occured : {e}");
            return None;


DBConnection.get_connection();