import unittest
from c2c.recipe.cssmin.buildout import relocate_urls

class TestCssminRecipe(unittest.TestCase):
    def test_relocate_urls(self):
        
        data = [(("url( 'foo.png')", "/a/b/src.css", "/a/b/dest.css"), "url('foo.png')"),
                (("url( 'foo.png' )", "b/src.css", "b/dest.css"), "url('foo.png')"),
                (("url('foo.png' )", "/a/b/src.css", "/a/c/dest.css"), "url('../b/foo.png')"),
                (("url('http://www.example.com/foo.png')", "/a/b/src.css", "/a/c/dest.css"), "url('http://www.example.com/foo.png')"),
                (("foo('foo.png' )", "/a/b/src.css", "/a/c/dest.css"), "foo('foo.png' )")]

        [self.assertEqual(relocate_urls(*input), output) for input, output in data]

if __name__ == '__main__':
    unittest.main()
