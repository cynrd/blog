package examples;


public class Example {
	
    public static void main (String[] args) {
		foo(-2, 1);
    }
    
	public static int foo(int x, int y){
		if (x > y){
			System.out.println("First");
			return x;
		}else{
			System.out.println("Second");
			return y;
		}
	}

}
