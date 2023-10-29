class A {
    void Display()
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


public class Single {
    public static void main (String args[])
    {
        B objB = new B();
        objB.Display();
        objB.Print();
    }
}
