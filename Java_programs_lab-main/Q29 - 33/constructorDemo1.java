// Q29) Wajp to understand constructor concept

class Sample
{
    int x,y,z;
    Sample()
    {
        x = 38;
        y = 45;
    }

    void calc()
    {
        z = x+y;
    }

    void show()
    {
        System.out.println(z);
    }
}

public class constructorDemo1
{
    public static void main (String args[]){
        Sample s = new Sample();
        s.calc();
        s.show(); 
    }
}
