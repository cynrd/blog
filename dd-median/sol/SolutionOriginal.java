package sol;

import java.util.Scanner;

public class SolutionOriginal {
    
    public static void find(int[] a, int min, int max, int med) {
        int pivot = a[max];
        int curr = min;
        int hi = -1;
        while (curr < max) {
            if (a[curr] > pivot && hi == -1) {
                hi = curr;
            } else if (a[curr] < pivot && hi != -1) {
                int tmp = a[hi];
                a[hi] = a[curr];
                a[curr] = tmp;
                hi++;
            } 
            curr++;
        }
        if (hi == med) {
            System.out.println(pivot);
        } else if (hi != -1) {
            a[max] = a[hi];
            a[hi] = pivot;
            if (hi > med) {
                find(a, min, hi-1, med);
            } else {
                find(a, hi+1, max, med);
            }
        } else {
            find(a, min, max-1, med);            
        }
        
    }

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; ++i) {
            a[i] = scan.nextInt();
        }
        
        find(a, 0, n-1, n/2);
        scan.close();
    }
}