// Q37) Wajp to find area off a triangle and area of a circle using interface and 2 different classes

interface Shape {
    float area();
}

class Triangle implements Shape {
    float height;
    float base;

    Triangle(float height, float base) {
        this.base = base;
        this.height = height;
    }

    public float area() {
        return 0.5f * base * height;
    }
}

class Circle implements Shape {
    float radius;

    Circle(float radius) {
        this.radius = radius;
    }

    public float area() {
        return 3.14f * radius * radius;
    }
}

public class _37area_ {
    public static void main(String[] args) {
        Triangle triangle = new Triangle(10, 14);
        Circle circle = new Circle(3);
        System.out.println("The area of triangle = " + triangle.area());
        System.out.println("The area of circle = " + circle.area());
    }
}
