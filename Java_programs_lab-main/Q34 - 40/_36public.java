// Q36) wajp TO Demonstare static and public method

public class _36public
{
    public static void main (String args[])
    {
        Sample s1 = new Sample();
        s1.showData();
        Sample s2 = new Sample();
        s2.showData();
    }
}

class Sample
{
    int a = 1;
    static int b = 2;
    Sample()
    {
        b++;
    }
    public void showData()
    {
        System.out.println("value of a - " + a);
        System.out.println("value of b - " + b);
    }
}