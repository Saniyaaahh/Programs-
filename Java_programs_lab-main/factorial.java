// Q11) Java program to find factorial of a number

public class factorial {
    public static void main(String[] args) {
        int number = 5; 
        int factorial = 1;

        for (int i = 1; i <= number; i++) {
            factorial *= i;
        }

        System.out.println("The factorial of " + number + " is " + factorial);
    }
    
}
