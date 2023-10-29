// Q12) write a java program to initialise an array and find the sum of an array

public class array {
    public static void main(String[] args) {
        int[] arr = {11, 22, 33, 44, 55};
        int sum = 0;

        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
        }

        System.out.println("The sum of the array is " + sum);
    }
    
}
