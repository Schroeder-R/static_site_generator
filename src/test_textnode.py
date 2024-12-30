import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a test", TextType.BOLD)
        node2 = TextNode("This is a test", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a test", TextType.BOLD)
        node2 = TextNode("This is a different test", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a test", TextType.BOLD)
        node2 = TextNode("This is a test", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq4(self):
        node = TextNode("This is a test", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a test", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_eq5(self):
        node = TextNode("This is a test", TextType.BOLD)
        node2 = TextNode("This is a test", TextType.BOLD, "https://www.boot.com")
        self.assertNotEqual(node, node2)

    def test_eq6(self):
        node = TextNode("This is a test", TextType.BOLD, "https://www.boots.com")
        node2 = TextNode("This is a test", TextType.BOLD, "https://www.boot.com")
        self.assertNotEqual(node, node2)

    def test_eq7(self):
        node = TextNode("This is a test", TextType.BOLD, url=None)
        node2 = TextNode("This is a test", TextType.BOLD, "https://www.boot.com")
        self.assertNotEqual(node, node2)

    def test_eq8(self):
        node = TextNode("This is a test", TextType.BOLD, url=None)
        node2 = TextNode("This is a test", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq9(self):
        node = TextNode("This is a test", TextType.BOLD, url=None)
        node2 = TextNode("This is a test", TextType.BOLD, url=None)
        self.assertEqual(node, node2)

    def test_empty_text(self):
        node = TextNode("", TextType.BOLD)
        node2 = TextNode("", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_long_text(self):
        long_text = "x" * 10000
        node = TextNode(long_text, TextType.BOLD)
        node2 = TextNode(long_text, TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_special_chars(self):
        node = TextNode("🧙‍♂️ *&^%$#@!", TextType.BOLD)
        node2 = TextNode("🧙‍♂️ *&^%$#@!", TextType.BOLD)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()