// Q23) write a java program to understand methods concept using parameters

import java.util.Scanner;

public class MethodDemo {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // taking user input
        System.out.print("Enter the first number: ");
        int a = input.nextInt();

        System.out.print("Enter the second number: ");
        int b = input.nextInt();

        // calling the add() method with user input values as parameters
        int sum = add(a, b);

        System.out.println("Sum of " + a + " and " + b + " is " + sum);

        input.close();
    }

    // method that takes two integer parameters and returns their sum
    public static int add(int x, int y) {
        int sum = x + y;
        return sum;
    }
}

