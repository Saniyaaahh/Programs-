// Q32 WAJP to understand method over riding concept

class Sample {
    int x, y, z;
    float t;
    
    void show(int a) {
        x = a;
    }
    
    void show(int b, int c) {
        y = b;
        z = c;
    }

    void show(float d) {
        t = d;
    }

    void display() {
        System.out.println(x);
        System.out.println(y);
        System.out.println(z);
        System.out.println(t);
    }
}

public class overriding {
    public static void main(String[] args) {
        Sample s = new Sample();
        s.show(10);
        s.show(10, 20);
        s.show(4.5f);
        s.display();
    }
}