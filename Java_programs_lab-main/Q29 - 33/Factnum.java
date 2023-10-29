// Q31) WAJP to find a factorial of a number using default constructor

import java.util.*;

class Factorial {
    int i, n, fact;

    Factorial() {
        fact = 1;
    }

    void calc() {
        for (i = 1; i <= n; i++) {
            fact = fact * i;
        }
    }

    void accept() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the n value = ");
        n = sc.nextInt();
    }

    void show() {
        System.out.println("The factorial of " + n + " is  = " + fact);
    }
}

public class Factnum {
    public static void main(String args[]) {
        Factorial f = new Factorial();
        f.accept();
        f.calc();
        f.show();
    }
}