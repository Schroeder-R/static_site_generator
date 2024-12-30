import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("Hello, World!", "p")
        self.assertEqual(node.to_html(), "<p>Hello, World!</p>")

    def test_no_tag(self):
        node = LeafNode("Hello, World!")
        self.assertEqual(node.to_html(), "Hello, World!")
    
    def test_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode(None, "p")
    
    def test_props(self):
        node = LeafNode("Hello, World!", "p", props={"class": "intro"})
        self.assertEqual(node.to_html(), '<p class="intro">Hello, World!</p>')

    def test_multiple_props(self):
        node = LeafNode("Click me!", "a", props={"href": "https://example.com", "class": "link"})
        self.assertEqual(node.to_html(), '<a href="https://example.com" class="link">Click me!</a>')
    
    def test_special_characters(self):
        node = LeafNode("Hello & goodbye", "p")
        self.assertEqual(node.to_html(), "<p>Hello & goodbye</p>")

    def test_empty_string_value(self):
        node = LeafNode("", "p")
        self.assertEqual(node.to_html(), "<p></p>")

if __name__ == "__main__":
    unittest.main()