import static org.junit.Assert.*;

import java.util.Iterator;
import java.util.NoSuchElementException;

import org.junit.Test;

public class DequeTest {

    @Test
    public void testEmptyDeque() {
        Deque<Integer> d = new Deque<Integer>();
        assertTrue(d.isEmpty());
        assertEquals(0, d.size());
    }

    @Test
    public void testAddFirst() {
        Deque<Integer> d = new Deque<Integer>();
        d.addFirst(5);
        assertFalse(d.isEmpty());
        assertEquals(1, d.size());
        Iterator<Integer> it = d.iterator();
        assertNotNull(it);
        assertTrue(it.hasNext());
        assertEquals(new Integer(5), it.next());
        assertFalse(it.hasNext());
    }

    @Test(expected=NullPointerException.class)
    public void testAddFirstNull() {
        Deque<Integer> d = new Deque<Integer>();
        d.addFirst(null);
    }

    
    @Test
    public void testTwoAddFirst() {
        Deque<Integer> d = new Deque<Integer>();
        d.addFirst(5);
        d.addFirst(3);
        assertFalse(d.isEmpty());
        assertEquals(2, d.size());
        Iterator<Integer> it = d.iterator();
        assertNotNull(it);
        assertTrue(it.hasNext());
        assertEquals(new Integer(3), it.next());
        assertTrue(it.hasNext());
        assertEquals(new Integer(5), it.next());
        assertFalse(it.hasNext());
    }

    @Test
    public void testRemoveFirst() {
        Deque<Integer> d = new Deque<Integer>();
        d.addFirst(5);
        Integer x = d.removeFirst();
        assertNotNull(x);
        assertEquals(new Integer(5), x);
        assertTrue(d.isEmpty());
        assertEquals(0, d.size());
    }

    @Test(expected=NoSuchElementException.class)
    public void testRemoveFirstEmpty() {
        Deque<Integer> d = new Deque<Integer>();
        d.removeFirst();
    }

    @Test
    public void testTwoRemoveFirst() {
        Deque<Integer> d = new Deque<Integer>();
        d.addFirst(5);
        d.addFirst(3);
        Integer x = d.removeFirst();
        assertNotNull(x);
        assertEquals(new Integer(3), x);
        x = d.removeFirst();
        assertNotNull(x);
        assertEquals(new Integer(5), x);
        assertTrue(d.isEmpty());
        assertEquals(0, d.size());
    }

    @Test
    public void testAddLast() {
        Deque<Integer> d = new Deque<Integer>();
        d.addLast(5);
        assertFalse(d.isEmpty());
        assertEquals(1, d.size());
        Iterator<Integer> it = d.iterator();
        assertNotNull(it);
        assertTrue(it.hasNext());
        assertEquals(new Integer(5), it.next());
        assertFalse(it.hasNext());
    }

    @Test(expected=NullPointerException.class)
    public void testAddLastNull() {
        Deque<Integer> d = new Deque<Integer>();
        d.addLast(null);
    }

    
    @Test
    public void testTwoAddLast() {
        Deque<Integer> d = new Deque<Integer>();
        d.addLast(5);
        d.addLast(3);
        assertFalse(d.isEmpty());
        assertEquals(2, d.size());
        Iterator<Integer> it = d.iterator();
        assertNotNull(it);
        assertTrue(it.hasNext());
        assertEquals(new Integer(5), it.next());
        assertTrue(it.hasNext());
        assertEquals(new Integer(3), it.next());
        assertFalse(it.hasNext());
    }

    @Test
    public void testRemoveLast() {
        Deque<Integer> d = new Deque<Integer>();
        d.addLast(5);
        Integer x = d.removeLast();
        assertNotNull(x);
        assertEquals(new Integer(5), x);
        assertTrue(d.isEmpty());
        assertEquals(0, d.size());
    }

    @Test(expected=NoSuchElementException.class)
    public void testRemoveLastEmpty() {
        Deque<Integer> d = new Deque<Integer>();
        d.removeLast();
    }
    
    @Test
    public void testTwoRemoveLast() {
        Deque<Integer> d = new Deque<Integer>();
        d.addLast(5);
        d.addLast(3);
        Integer x = d.removeLast();
        assertNotNull(x);
        assertEquals(new Integer(3), x);
        x = d.removeLast();
        assertNotNull(x);
        assertEquals(new Integer(5), x);
        assertTrue(d.isEmpty());
        assertEquals(0, d.size());
    }

    @Test(expected=NoSuchElementException.class)
    public void testIteratorNoNext() {
        Deque<Integer> d = new Deque<Integer>();
        Iterator<Integer> it = d.iterator();
        it.next();
    }

    @Test(expected=UnsupportedOperationException.class)
    public void testIteratorRemove() {
        Deque<Integer> d = new Deque<Integer>();
        Iterator<Integer> it = d.iterator();
        it.remove();
    }

}
