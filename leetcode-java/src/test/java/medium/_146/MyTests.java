package medium._146;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;


public class MyTests {
    @Test
    public void justAnExample() {
        var cache = new LRUCache(2);
        cache.put(1, 1);
        cache.put(2, 2);
        var result = cache.get(1);
        assertEquals(1, result);
        cache.put(3,3);
        result = cache.get(2);
        assertEquals(-1, result);
        cache.put(4, 4);
        result = cache.get(1);
        assertEquals(-1, result);
        result = cache.get(3);
        assertEquals(3, result);
        result = cache.get(4);
        assertEquals(4, result);

    }

    @Test
    public void anotherTestCase() {
        var cache = new LRUCache(2);
        var result = cache.get(2);
        assertEquals(-1, result);
        cache.put(2, 6);
        result = cache.get(1);
        assertEquals(-1, result);
        cache.put(1, 5);
        cache.put(1,2);
        result = cache.get(1);
        assertEquals(2, result);
        result = cache.get(2);
        assertEquals(6, result);
    }

    @Test
    public void testCase3() {
        var cache = new LRUCache(2);
        cache.put(2, 1);
        cache.put(1, 1);
        cache.put(2, 3);
        cache.put(4, 1);

        var result = cache.get(1);
        assertEquals(-1, result);
        result = cache.get(2);
        assertEquals(3, result);
    }
}
