package com.bru.workshop.compiler;

import javax.tools.SimpleJavaFileObject;
import java.net.URI;

/**
 * User: alexb
 * Date: 20/05/12
 * Time: 13:40
 * http://weblogs.java.net/blog/malenkov/archive/2008/12/how_to_compile.html
 */
class Source extends SimpleJavaFileObject {
    private final String content;

    Source(String name, Kind kind, String content) {
        super(URI.create("memo:///" + name.replace('.', '/') + kind.extension), kind);
        this.content = content;
    }

    @Override
    public CharSequence getCharContent(boolean ignore) {
        return this.content;
    }
}
