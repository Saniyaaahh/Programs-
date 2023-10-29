//  Q17) Write a simple java program to understand class and object method

class Info {
    int x;
    int y;
}

public class Sample {
    public static void main(String args[]) {
        int z;
        Info i = new Info();
        i.x = 38;
        i.y = 29;
        z = i.x + i.y;
        System.out.println("The sum of " + i.x + " and " + i.y + " is " + z);
    }
}
