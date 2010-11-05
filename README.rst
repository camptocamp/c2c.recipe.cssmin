=================
c2c.recipe.cssmin
=================

Requirements
------------
Requires zc.buildout and `cssmin <http://pypi.python.org/pypi/cssmin>`_

Usage
-----
Create a buildout.cfg file which contains the following::

    [buildout]
    parts = cssmin

    [cssmin]
    recipe = c2c.recipe.cssmin
    input = foo/bar/file1.css
            foo/bar/file2.css
            foo/baz/file3.css
    output = foo/build/output.min.css
    compress = true

Path are relative to the buildout directory, absolute path are also allowed.
