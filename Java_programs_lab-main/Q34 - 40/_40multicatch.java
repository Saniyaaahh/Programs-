// Q40) Try exceptions

public class _40multicatch {
    public static void main(String args []) {
        try 
        {
            int a = 0;
            System.out.println("a = " + a);
            int b = 42 / a;
            int c[] = {1};
            c[42] = 99;
        }

        catch(ArithmeticException e)
        {
            System.out.println("Divide by 0: " + e); 
        }
        catch (ArrayIndexOutOfBoundsException e)
        {
            System.out.println("Array index of b: " + e);

        }

            System.out.println("After try/catch blocks ");
    }

}
