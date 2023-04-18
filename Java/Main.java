package Java;


class Main {

    public static void main(String[] args) {
        System.out.println("Hola mundo");
        Car car = new Car("AMS123", new Account("Carlos", "123456789"));
    
        car.passegenger = 4;
        car.printDataCar();

        Car car2 = new Car("ADT852",new Account("Andres", "987654321"));
    
        car2.passegenger = 3;

        car2.printDataCar();



    }
}
