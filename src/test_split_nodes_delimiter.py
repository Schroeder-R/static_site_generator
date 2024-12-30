import unittest
from textnode import TextNode, TextType
from text_node_converter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        # Test 1: Basic split with code
        node = TextNode("This is `code` text", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        assert len(nodes) == 3
        assert nodes[0].text == "This is "
        assert nodes[0].text_type == TextType.TEXT
        assert nodes[1].text == "code"
        assert nodes[1].text_type == TextType.CODE
        assert nodes[2].text == " text"
        assert nodes[2].text_type == TextType.TEXT

    def test_split_nodes_delimiter_no_delimiter(self):
        # Test 2: No delimiters should return unchanged
        node = TextNode("This is a text", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        assert len(nodes) == 1
        assert nodes[0].text == "This is a text"
        assert nodes[0].text_type == TextType.TEXT

    def test_split_nodes_delimiter_with_delimiter_pass_through(self):
        # Test 3: Node that's already bold/italic/code should pass through
        node = TextNode("This is **bold** text", TextType.BOLD)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        assert len(nodes) == 1
        assert nodes[0].text == "This is **bold** text"
        assert nodes[0].text_type == TextType.BOLD
    
    def test_split_nodes_delimiter_with_delimiter_multiple_pairs(self):
        # Test 4: Multiple delimiter pairs
        node = TextNode("This is **bold** and **more bold**", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        assert len(nodes) == 5
        assert nodes[0].text == "This is "
        assert nodes[0].text_type == TextType.TEXT
        assert nodes[1].text == "bold"
        assert nodes[1].text_type == TextType.BOLD
        assert nodes[2].text == " and "
        assert nodes[2].text_type == TextType.TEXT
        assert nodes[3].text == "more bold"
        assert nodes[3].text_type == TextType.BOLD
        assert nodes[4].text == ""
        assert nodes[4].text_type == TextType.TEXT

    def test_split_nodes_delimiter_with_delimiter_invalid(self):
        # Test 5: Invalid/unmatched delimiters should raise ValueError
        node = TextNode("This **bold** has **another start", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)


if __name__ == "__main__":
    unittest.main()