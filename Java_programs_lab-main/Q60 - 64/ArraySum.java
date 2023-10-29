// write a java program to accept 2 arrays and find sum of corresponding elements using buffer reader

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ArraySum {
    public static void main(String[] args) {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        try {
            // Accept the size of the arrays
            System.out.print("Enter the size of the arrays: ");
            int size = Integer.parseInt(reader.readLine());

            // Create the arrays
            int[] array1 = new int[size];
            int[] array2 = new int[size];

            // Accept elements for array1
            System.out.println("Enter elements for Array 1:");
            for (int i = 0; i < size; i++) {
                System.out.print("Enter element " + (i + 1) + ": ");
                array1[i] = Integer.parseInt(reader.readLine());
            }

            // Accept elements for array2
            System.out.println("Enter elements for Array 2:");
            for (int i = 0; i < size; i++) {
                System.out.print("Enter element " + (i + 1) + ": ");
                array2[i] = Integer.parseInt(reader.readLine());
            }

            // Calculate the sum of corresponding elements
            int[] sumArray = new int[size];
            for (int i = 0; i < size; i++) {
                sumArray[i] = array1[i] + array2[i];
            }

            // Display the result
            System.out.println("Sum of corresponding elements:");
            for (int i = 0; i < size; i++) {
                System.out.println(sumArray[i]);
            }

        } catch (IOException e) {
            e.printStackTrace();
        } catch (NumberFormatException e) {
            System.out.println("Invalid input! Please enter integers only.");
        }
    }
}

