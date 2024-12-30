import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_one_child(self):
        node = ParentNode("p", [LeafNode("Hello, World!")])
        self.assertEqual(node.to_html(), "<p>Hello, World!</p>")
    
    def test_mulitiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text"),  # Correctly aligned with your class signature
                LeafNode("italic text", "i"),
                LeafNode("Normal text"),  # Again, correctly positioned
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    
    def test_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("Hello, World!")])
    
    def test_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("p", None)

    def test_children_props(self):
        child_node = LeafNode("Hello, World!", "p", props={"class": "intro"})
        node = ParentNode("div", [child_node])
        self.assertEqual(node.to_html(), '<div><p class="intro">Hello, World!</p></div>')
    
    def test_repr(self):
        node = ParentNode("p", [LeafNode("Hello, World!")])
        self.assertEqual(str(node), "ParentNode(p, [LeafNode(None, Hello, World!, None)], None)")

    def test_grand_children(self):
        grandchild_node = LeafNode("Grandchild text", "span")
        child_hode = ParentNode("h2", [grandchild_node])
        parent_node = ParentNode("div", [child_hode])
        self.assertEqual(parent_node.to_html(), '<div><h2><span>Grandchild text</span></h2></div>')

    def test_empty_child_content(self):
        node = ParentNode("p", [LeafNode("")])
        self.assertEqual(node.to_html(), "<p></p>")

    def test_deep_nesting(self):
        deep_node = LeafNode("Deep text", "em")
        middle_node = ParentNode("span", [deep_node])
        top_node = ParentNode("div", [middle_node])
        self.assertEqual(top_node.to_html(), '<div><span><em>Deep text</em></span></div>')

    def test_whitespace_handling(self):
        node = ParentNode("p", [LeafNode("  ")])
        self.assertEqual(node.to_html(), "<p>  </p>")
    
    def test_multiple_props(self):
        node = LeafNode("Styled text", "p", props={"class": "styled", "id": "intro"})
        self.assertEqual(node.to_html(), '<p class="styled" id="intro">Styled text</p>')

    def test_special_characters(self):
        # Test with content that includes special HTML characters
        node = ParentNode("div", [
            LeafNode("Using <b>bold</b> tags & ampersands safely")
        ])
        # Assume that text in LeafNode is trusted and doesn't need escaping
        # Expected output relies on content being rendered as-is
        self.assertEqual(node.to_html(), "<div>Using <b>bold</b> tags & ampersands safely</div>")

if __name__ == "__main__":
    unittest.main()