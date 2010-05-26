import unittest
from c2c.recipe.cssmin.buildout import relocate_urls

class TestCssminRecipe(unittest.TestCase):
    def test_relocate_urls(self):
        # Same directory:
        self.assertEqual(relocate_urls("url( 'foo.png')", "/a/b/src.css", "/a/b/dest.css"), "url('foo.png')")
        # Same directory, relative path:
        self.assertEqual(relocate_urls("url( 'foo.png' )", "b/src.css", "b/dest.css"), "url('foo.png')")
        # Different directory:
        self.assertEqual(relocate_urls("url( 'foo.png' )", "/a/b/src.css", "/a/c/dest.css"), "url('../b/foo.png')")
        # Only handle url rules:
        self.assertEqual(relocate_urls("foo('foo.png' )", "/a/b/src.css", "/a/c/dest.css"), "foo('foo.png' )")
        

if __name__ == '__main__':
    unittest.main()
