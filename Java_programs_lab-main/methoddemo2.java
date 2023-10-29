// Q24) write a java program to understand methods concept using parameters and return a value

import java.util.Scanner;

public class methoddemo2 {
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // taking user input
        System.out.print("Enter the first number: ");
        int a = input.nextInt();

        System.out.print("Enter the second number: ");
        int b = input.nextInt();

        // calling the add() method with user input values as parameters
        int sum = add(a, b);

        // calling the multiply() method with the sum as parameter
        int product = multiply(sum);

        System.out.println("Product of the sum of " + a + " and " + b + " is " + product);

        input.close();
    }

    // method that takes two integer parameters and returns their sum
    public static int add(int x, int y) {
        int sum = x + y;
        return sum;
    }

    // method that takes an integer parameter and returns its product with 10
    public static int multiply(int x) {
        int product = x * 10;
        return product;
    }
    
}
