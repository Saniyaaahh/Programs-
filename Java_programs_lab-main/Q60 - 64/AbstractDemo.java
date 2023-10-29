abstract class A {
    abstract void showA();

    void showB() {
        System.out.println("non-abstract method");
    }
}

class B extends A {
    @Override
    void showA() {
        System.out.println("Inside showA() of class B");
    }
}

public class AbstractDemo {
    public static void main(String[] args) {
        B bObj = new B();
        bObj.showA();
        bObj.showB();
    }
}
