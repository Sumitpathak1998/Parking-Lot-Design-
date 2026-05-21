from enum import Enum;

class PaymentType(Enum) :
    CASH = "cash";
    CARD = "card";
    UPI = "upi";