public class app {

    // method to add two integers
    public int add(int num1, int num2) {
        return num1 + num2;
    }

    // method to add three integers
    public int add(int num1, int num2, int num3) {
        return num1 + num2 + num3;
    }

    // method to add two doubles
    public double add(double num1, double num2) {
        return num1 + num2;
    }
  
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        
        // calling the add method with two integers
        int result1 = calc.add(5, 10);
        System.out.println("Result of adding 5 and 10: " + result1);
        
        // calling the add method with three integers
        int result2 = calc.add(5, 10, 15);
        System.out.println("Result of adding 5, 10, and 15: " + result2);
        
        // calling the add method with two doubles
        double result3 = calc.add(3.14, 2.71);
        System.out.println("Result of adding 3.14 and 2.71: " + result3);
    }
}
