package com.bru.workshop.compiler;

import javax.tools.*;
import java.util.HashMap;
import java.util.Map;

/**
 * User: alexb
 * Date: 20/05/12
 * Time: 13:44
 * http://weblogs.java.net/blog/malenkov/archive/2008/12/how_to_compile.html
 */
class MemoryFileManager extends ForwardingJavaFileManager<JavaFileManager> {
    private final Map<String, Output> map = new HashMap<String, Output>();

    MemoryFileManager(JavaCompiler compiler) {
        super(compiler.getStandardFileManager(null, null, null));
    }

    @Override
    public Output getJavaFileForOutput
            (Location location, String name, JavaFileObject.Kind kind, FileObject source) {
        Output mc = new Output(name, kind);
        this.map.put(name, mc);
        return mc;
    }

    public Map<String, Output> getMap() {
        return map;
    }
}