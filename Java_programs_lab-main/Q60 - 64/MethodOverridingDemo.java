// write a java program to demonstrate METHOD overriding concept

class Vehicle {
    public void displayInfo() {
        System.out.println("This is a vehicle.");
    }
}

class Car extends Vehicle {
    @Override
    public void displayInfo() {
        System.out.println("This is a car.");
    }
}

public class MethodOverridingDemo {
    public static void main(String[] args) {
        Vehicle vehicle = new Vehicle();
        vehicle.displayInfo(); // Output: This is a vehicle.

        Car car = new Car();
        car.displayInfo(); // Output: This is a car.

        Vehicle vehicle2 = new Car();
        vehicle2.displayInfo(); // Output: This is a car.
    }
}

