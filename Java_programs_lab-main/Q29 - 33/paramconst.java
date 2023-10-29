// Q30) Wajp to understand constructor concept using parameters

class Sample{
    int x,y,z;
    Sample(int a, int b)
    {
        x = a;
        y = b;
    }

    void calc()
    {
        z = x + y;
    }

    void show()
    {
        System.out.println(x + " + " + y + " = " + z);
    }
}

public class paramconst
{
    public static void main (String args[])
    {
        Sample s = new Sample(20,30);
        s.calc();
        s.show();
    }
}