class A {
    void Show()
    {
        System.out.println("I am method from class A");
    }
}

class B extends A {
    void Print()
    {
        System.out.println("I am method from class B");
    }
}

class C extends A {
    void Display()
    {
        System.out.println("I am method from class C");
    }
}

public class Hierarichal {
    public static void main (String args[])
    {
        B obj = new B();
        obj.Print();
        obj.Show();
        
        C oc = new C();
        oc.Display();
        oc.Show();

    }
    
}
