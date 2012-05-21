package com.bru.workshop.compiler;

import junit.framework.Assert;
import org.junit.Test;

/**
 * User: alexb
 * Date: 20/05/12
 * Time: 13:50
 */
public class MemoryClassLoaderTest {

    private static final String CLASS = "Test";
    private static final String METHOD = "execute";
    private static final String EXPRESSION = "Math.cos(Math.PI/6)";
    private static final String CONTENT
            = "public class " + CLASS + " {"
            + "    public static Object " + METHOD + "() {"
            + "        return " + EXPRESSION + ";"
            + "    }"
            + "}";

    @Test
    public void testInMemoryLoadedClass() throws Exception {
        MemoryClassLoader mcl = new MemoryClassLoader(CLASS, CONTENT);
        Assert.assertEquals(0.8660254037844387, mcl.loadClass(CLASS).getMethod(METHOD).invoke(null));
    }

}
