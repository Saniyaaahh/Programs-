// Q38 WAJP to find palindrome of a string

public class _38palindrome {
    public static void main (String args[]) {
        String S1 = "racecar";
        StringBuffer Sb = new StringBuffer(S1);
        Sb.reverse();
        String S2 = Sb.toString();

        if (S2.equals(S1))
        {
            System.out.println("Yes it is a palindrome");
        }
        else 
        {
            System.out.println("NO it is not a palindrome");
        }
    }
    
}
