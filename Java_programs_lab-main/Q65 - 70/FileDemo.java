import java.io.File;

class FileDemo {
    static void p(String s) {
        System.out.println(s);
    }

    public static void main(String args[]) {
        File f1 = new File("h.java");
        p("File Name: " + f1.getName());
        p("Abs Path: " + f1.getAbsolutePath());
        p(f1.exists() ? "exists" : "does not exist");
        p(f1.canWrite() ? "is writeable" : "is not writeable");
        p(f1.canRead() ? "is readable" : "is not readable");
        p("is " + (f1.isDirectory() ? "" : "not") + " a directory");
        p("File last modified: " + f1.lastModified());
        // System.out.println(Instant.ofEpochMilli(f1.lastModified()));
        p("File size: " + f1.length() + " Bytes");
    }
}
