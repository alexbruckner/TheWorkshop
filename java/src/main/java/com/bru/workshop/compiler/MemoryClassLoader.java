package com.bru.workshop.compiler;

import javax.tools.JavaCompiler;
import javax.tools.JavaFileObject;
import javax.tools.ToolProvider;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;

/**
 * User: alexb
 * Date: 20/05/12
 * Time: 13:46
 */
public class MemoryClassLoader extends ClassLoader {
    private final JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();
    private final MemoryFileManager manager = new MemoryFileManager(this.compiler);

    public MemoryClassLoader(String classname, String filecontent) {
        this(Collections.singletonMap(classname, filecontent));
    }

    public MemoryClassLoader(Map<String, String> map) {
        List<Source> list = new ArrayList<Source>();
        for (Map.Entry<String, String> entry : map.entrySet()) {
            list.add(new Source(entry.getKey(), JavaFileObject.Kind.SOURCE, entry.getValue()));
        }
        this.compiler.getTask(null, this.manager, null, null, null, list).call();
    }

    @Override
    protected Class<?> findClass(String name) throws ClassNotFoundException {
        synchronized (this.manager) {
            Output mc = this.manager.getMap().remove(name);
            if (mc != null) {
                byte[] array = mc.toByteArray();
                return defineClass(name, array, 0, array.length);
            }
        }
        return super.findClass(name);
    }
}
