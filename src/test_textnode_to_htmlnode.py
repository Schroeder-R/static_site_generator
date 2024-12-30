import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from text_node_converter import text_node_to_html_node

class TestTextNodeToHTMLNode(unittest.TestCase):

    def test_invalid_text_type(self):
        text_node = TextNode("This is a test", None)
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)
    
    def test_bold_text(self):
        text_node = TextNode("This is a test", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.value, "This is a test")
        self.assertEqual(html_node.tag, "b")
        self.assertIsNone(html_node.props)

    def test_italic_text(self):
        text_node = TextNode("This is a test", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.value, "This is a test")
        self.assertEqual(html_node.tag, "i")
        self.assertIsNone(html_node.props)

    def test_code_text(self):
        text_node = TextNode("This is a test", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.value, "This is a test")
        self.assertEqual(html_node.tag, "code")
        self.assertIsNone(html_node.props)

    def test_link_text(self):
        text_node = TextNode("Visit Boots", TextType.LINK, "https://www.boots.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.value, "Visit Boots")
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "https://www.boots.com"})

    def test_image_text(self):
        text_node = TextNode("Logo", TextType.IMAGE, "https://www.boots.com/logo.png")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "https://www.boots.com/logo.png", "alt": "Logo"})

    def test_text(self):
        text_node = TextNode("This is a test", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.value, "This is a test")
        self.assertIsNone(html_node.tag)
        self.assertIsNone(html_node.props)

if __name__ == "__main__":
    unittest.main()