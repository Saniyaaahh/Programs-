// Q19) write a java program to find area of a circle using class and object method

import java.util.Scanner;

class Circle {
    double radius;

    void setRadius(double r) {
        radius = r;
    }

    double getArea() {
        double area = Math.PI * radius * radius;
        return area;
    }
}

public class CalculateArea {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Circle c = new Circle();
        System.out.print("Enter the radius of the circle: ");
        double r = input.nextDouble();
        c.setRadius(r);
        double area = c.getArea();
        System.out.println("The area of the circle is " + area);
        input.close();
    }
}
