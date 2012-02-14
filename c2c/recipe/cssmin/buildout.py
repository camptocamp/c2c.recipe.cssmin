# -*- coding: utf-8 -*-
# buildout recipe for cssmin
#
import re
import os
import logging

# backport os.path.relpath if python < 2.6
try:
    from os.path import relpath
except ImportError:
    def relpath(path, start=os.curdir):
        if not path:
            raise ValueError("no path specified")
        start_list = os.path.abspath(start).split(os.path.sep)
        path_list = os.path.abspath(path).split(os.path.sep)
        # Work out how much of the filepath is shared by start and path.
        i = len(os.path.commonprefix([start_list, path_list]))
        rel_list = [os.path.pardir] * (len(start_list)-i) + path_list[i:]
        if not rel_list:
            return os.curdir
        return os.path.join(*rel_list)

from cssmin import cssmin

class CssMin(object):
    def __init__(self, buildout, name, options):
        basedir = buildout['buildout']['directory']
        self.logger = logging.getLogger(name)
        self.input = [os.path.join(basedir, f) for f in options['input'].split()]
        self.output = os.path.join(basedir, options['output'])
        self.compress = options.query_bool('compress', 'true')
        self.wrap = options.get('wrap', None)

    def install(self):
        dir = os.path.dirname(self.output)
        if not os.path.exists(dir):
            os.makedirs(dir)
        output = open(self.output, 'w')
        for f in self.input:
            css = relocate_urls(open(f).read(), f, self.output)
            if self.compress:
                output.write(cssmin(css, wrap=self.wrap))
            else:
                output.write(css)
        output.close()

        self.logger.debug("merging %s to %s"%(self.input, self.output))
        return self.output

    update = install

def relocate_urls(css, src, dest):
    """ Relocate all relative urls """
    # matches relative files only
    regex = re.compile(r"url\(\s?[\'\"]?([^:'\"]+)[\'\"]?\s?\)")
    return regex.sub(relative(src, dest), css)

def relative(src, dest):
    """ Return the relocator function """
    srcdir = os.path.dirname(src)
    destdir = os.path.dirname(dest)

    def _relative(m):
        if m is not None:
            abspath = os.path.normpath(os.path.join(srcdir, m.group(1)))
            # force '/' as path separator
            return "url('%s')" % '/'.join(relpath(abspath, destdir).split(os.sep))

    return _relative

