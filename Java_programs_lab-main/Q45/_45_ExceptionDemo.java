class MyException extends Exception
{
    private int detail;
    MyException(int a)
    {
        detail = a;
    }
    public String toString()
    {
        return "MyExcetion[" + detail + "]";
    }
}
class _45_ExceptionDemo
{
    static void compute(int a) throws MyException
    {
        System.out.println("called compute(" + a + ")");
        if (a > 10)
        throw new MyException(a);
        System.out.println("Normal Exit");
    }
    public static void main(String args[])
    {
        try
        {
            compute(1);
            compute(20);
        }
        catch (MyException e)
        {
            System.out.println("Caught " + e);
        }
    }
}