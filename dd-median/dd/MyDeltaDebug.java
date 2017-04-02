package dd;

import java.util.LinkedList;
import java.util.List;

public class MyDeltaDebug extends DeltaDebug {

    @Override
    protected <E> List<E> difference(List<E> a, List<E> b) {
        List<E> result = new LinkedList<E>();
        
        int i = 0;
        int j = 0;
        while (i < a.size() && j < b.size()) {
            E ai = a.get(i);
            if (ai.equals(b.get(j))) {
                i++;
                j++;
            } else {
                result.add(ai);
                i++;
            }
        }
        while (i < a.size()) {
            E ai = a.get(i);
            result.add(ai);
            i++;
        }
        
        return result;
    }

}
