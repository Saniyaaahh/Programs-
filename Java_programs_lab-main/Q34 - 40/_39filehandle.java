// Q39) Try exceptions

public class _39filehandle {
    public static void main (String args[]) {
        int d, a;
        try {
            d = 0;
            a = 38/d;
            System.out.println("This will not be printed");

        }

        catch (ArithmeticException e)
        {
            System.out.println("Division by zero");
        }
        System.out.println("After catch statment");
    }
    
}
