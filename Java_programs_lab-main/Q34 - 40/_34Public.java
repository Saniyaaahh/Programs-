// Q34) wajp TO Demonstare static and public method

class Sample {
    static void staticMethod() {
        System.out.println("Static Method");
    }

    public void publicMethod() {
        System.out.println("Public Method");
    }
}

public class _34Public {
    public static void main(String[] args) {
        Sample.staticMethod();
        Sample s = new Sample();
        s.publicMethod();
    }
}
