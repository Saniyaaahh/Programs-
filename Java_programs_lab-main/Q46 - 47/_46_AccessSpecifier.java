class Protection {
    int n = 1;
    private int n_pri = 2;
    protected int n_pro = 3;
    public int n_pub = 4;
    public Protection()
    {
        System.out.println("Base constructor");
        System.out.println("n = " + n);
        System.out.println("n_pri =  " + n_pri);
        System.out.println("n_pro =  " + n_pro);
        System.out.println("n_pub = " + n_pub);
    }
}

class Derived extends Protection
{
    Derived()
    {
        System.out.println("derived constructor");
        System.out.println("n = " + n);

        // System.out.println("n_pri =  " 4 + n_pri);
        System.out.println("n_pro =  " + n_pro);
        System.out.println("n_pub = " + n_pub);
    }
}

public class _46_AccessSpecifier {
    public static void main (String args [])
    {
        Protection ob1 = new Protection();
        Derived ob2 = new Derived();
    }
}