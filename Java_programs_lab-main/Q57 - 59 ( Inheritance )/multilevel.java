class A {
    void Print()
    {
        System.out.println("I am method from class A");
    }
}

class B extends A {
    void Show()
    {
        System.out.println("I am method from class B");
    }
}

class C extends B {
    void Display()
    {
        System.out.println("I am method from class C");
    }
}

public class multilevel {
    public static void main (String args[])
    {
        C obj = new C();
        obj.Print();
        obj.Show();
        obj.Display();
    }
    
}
