package dd;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

import sol.SolutionOriginal;

public class MedianDD {
    
    private static TestHarness<Integer> harness = new TestHarness<Integer>() {
        
        @Override
        public int run(List<Integer> input) {
            if (input.size() % 2 == 0) return PASS;
            
            int[] a = new int[input.size()];
            int index = 0;
            for (Integer i: input) {
                a[index++] = i.intValue();
            }
           
            try {
                SolutionOriginal.find(a, 0, a.length-1, a.length/2);
            } catch (Exception e) {
                return FAIL;
            }
           
            return PASS;
           
        }
    };
    
    public static void main(String[] args) throws FileNotFoundException {
        Scanner scan = new Scanner(new File("input.txt"));
        int n = scan.nextInt();
        List<Integer> input = new LinkedList<Integer>();
        for (int i = 0; i < n; ++i) {
            input.add(scan.nextInt());
        }
        System.out.println(new MyDeltaDebug().ddmin(input, harness));

    }

}
