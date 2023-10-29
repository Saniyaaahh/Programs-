// Q13) write a java program to initialise a single array of 5 elements and check all the elements are even or odd

public class sing {
    public static void main(String[] args) {
        int[] nums = {2, 4, 5, 8, 10}; 

        for (int num : nums) {
            if (num % 2 == 0) {
                System.out.println(num + " is even.");
            } else {
                System.out.println(num + " is odd.");
            }
        }

       
    }
    
}
