package com.bru.workshop;

import com.bru.workshop.compiler.MemoryClassLoader;
import py4j.GatewayServer;

import java.io.IOException;

/**
 * User: alexb
 * Date: 19/05/12
 * Time: 20:42
 */
public class Application {

    public int addition(int first, int second) {
        System.out.format("adding %s to %s\n", first, second);
        return first + second;
    }

    public Object compileAndExecute(String className, String classContent) {
        System.out.format("Compiling class %s:\n%s\n", className, classContent);
        MemoryClassLoader mcl = new MemoryClassLoader(className, classContent);
        try {
            System.out.format("Calling method execute.");
            return mcl.loadClass(className).getMethod("execute").invoke(null);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    public static void main(String[] args) throws IOException, InterruptedException {
        // http://py4j.sourceforge.net/
        System.out.println("starting application...");
        new GatewayServer(new Application()).start();
        System.out.println("application started.");
    }
}
