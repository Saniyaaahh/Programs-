public class _43ThrowsDemo {
    static void throwOne() throws IllegalAccessException
    {
        System.out.println("Inside throwONe");
        throw new IllegalAccessException("demo");

    }
    public static void main (String args[])
    {
        try {
            throwOne();
        }
        catch (IllegalAccessException e)
        {
            System.out.println("caught "+ e);
        }
        System.out.println("continuation of program");
    }
    
}
