// Q33) WAJP to understand constructor overloading concept

class Sample{
    int a,b,c;

    Sample()
    {
        System.out.println("default parameter");
    }
    {
        System.out.println(a);
    }

    Sample(int b, int c)
    {
        System.out.println(b + c);
    }
}

public class consover {
    public static void main (String args[])
    {
        Sample s1 = new Sample();
        Sample s2 = new Sample(10);
        Sample s3 = new Sample(20,30);
         
    }
    
}
