// Q15) write a java program to initialise 2 arrays of 5 elements and find their sum of correspondings in simple way

public class ArraySum {
    public static void main(String[] args) {
        int[] array1 = { 1, 2, 3, 4, 5 };
        int[] array2 = { 6, 7, 8, 9, 10 };
        int[] result = new int[5];
        int i;

        for (i = 0; i < 5; i++){

            result[i] = array1[i] + array2[i];
            System.out.println(result[i]);
        }
        
       
    }
}


