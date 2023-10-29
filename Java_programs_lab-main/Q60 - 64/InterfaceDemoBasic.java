interface InterfaceOne {
    void methodOne();
}

class ImplementClass implements InterfaceOne {
    public void methodOne() {
        System.out.println("Text from methodOne...");
    }
}

public class InterfaceDemoBasic {
    public static void main(String[] args) {
        ImplementClass obj = new ImplementClass();
        obj.methodOne();
    }
}
