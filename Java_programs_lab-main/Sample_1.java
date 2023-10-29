// Q18) Wajp to understand method concept by adding 2 numbers

class Info {
    int x;
    int y;
    int z;

    void calc() {
        x = 38;
        y = 29;
        z = 33;
    }

    void show() {
        int sum = x + y;
        System.out.println("The sum of " + x + " and " + y + " is " + sum);
    }
}

public class Sample_1 {
    public static void main(String args[]) {
        Info i = new Info();
        i.calc();
        i.show();
    }
}

