from account import Account

class CAR:
    id       = int
    license  = str
    driver   = str
    passegenger = str

    def __init__(self, license, driver):
        self.license  = license 
        self.driver   = driver  
