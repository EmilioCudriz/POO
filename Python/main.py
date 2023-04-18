
from account import Account
from car import CAR
from Payment import Payment
from Route import Rute



if __name__ == "__main__":
    print("Hola Mundo")
    
    carro = CAR("RTG876", Account("Aleandro","123654789"))
    print(vars(carro))

    car2 = CAR("TGF789", Account("Fercho","789654321"))
    print(vars(car2))
