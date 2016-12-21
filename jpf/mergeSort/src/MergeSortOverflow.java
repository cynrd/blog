
public class MergeSortOverflow {
    public static int binarySearch(byte[] a, byte key) {
        int low = 0;
        int high = a.length - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            int midVal = a[mid];
            if (midVal < key)
                low = mid + 1;
            else if (midVal > key)
                high = mid - 1;
            else
                return mid; // key found
        }
        return -(low + 1);  // key not found.
    }
    
  /*  public static void main (String[] args) {
        byte[] b = new byte[1100000000];
        b[b.length - 1] = 1;
        int index = binarySearch(b, (byte)1);
        System.out.println("index = " + index);
    }*/
}
