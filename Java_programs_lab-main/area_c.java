// Q20) write a java program to find area and circumference of a circle using class and object method

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

    double getCircumference() {
        double circumference = 2 * Math.PI * radius;
        return circumference;
    }
}

public class area_c {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Circle c = new Circle();
        System.out.print("Enter the radius of the circle: ");
        double r = input.nextDouble();
        c.setRadius(r);
        double area = c.getArea();
        double circumference = c.getCircumference();
        System.out.println("The area of the circle is " + area);
        System.out.println("The circumference of the circle is " + circumference);
        input.close();
    }
}

