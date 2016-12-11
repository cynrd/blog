import gov.nasa.jpf.symbc.Debug;
import gov.nasa.jpf.vm.Verify;

public class FruitPuzzle {

	static public final int MIN_INT = -20;
	static public final int MAX_INT = 20;

	public boolean test1(int apples, int bananas, int coconuts) {
		return (3*apples == 30);
	}
	
	public boolean test2(int apples, int bananas, int coconuts) {
		return (apples + 2*bananas == 18);
	}

	public boolean test3(int apples, int bananas, int coconuts) {
		return (bananas - coconuts == 2);
	}

	public boolean test(int apples, int bananas, int coconuts) {
		return (test1(apples, bananas, coconuts) &&
		    test2(apples, bananas, coconuts) &&
		    test3(apples, bananas, coconuts) ) ;
	}

	static public void main(String[] args){
		/*
		int apples = Verify.getInt(MIN_INT, MAX_INT);
		int bananas = Verify.getInt(MIN_INT, MAX_INT);
		int coconuts = Verify.getInt(MIN_INT, MAX_INT);
		*/
		int apples = 1; 
		int bananas = 1;
		int coconuts = 1;
		FruitPuzzle fp = new FruitPuzzle();
		if (fp.test(apples, bananas, coconuts)) {
			//System.out.println("Eq result = " + Integer.toString(apples+bananas+coconuts));
			Debug.printPC("\n Path condition: ");
			//throw new RuntimeException("found solution");
		}
	}
}
