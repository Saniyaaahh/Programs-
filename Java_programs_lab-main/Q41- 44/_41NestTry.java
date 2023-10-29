class _41NestTry {
    public static void main (String args []) {
        try {
            int a = 0;
            int b = 38 / a;
            System.out.println("a = " + a);

            try {
                if (a == 1)
                a = a / (a - a);

                if (a == 2)
                {
                    int c[] = {1};
                    c[38] = 89;
                }
            }
            catch(ArrayIndexOutOfBoundsException e)
            {
                System.out.println("Array index out of bounds = " + e);
            }
        }
        catch(ArithmeticException e)
        {
            System.out.println("Divide by zero " + e);
        }
        System.out.println("Continuation of program...");
    }
}