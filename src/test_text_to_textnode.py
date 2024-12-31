import unittest
from textnode import TextNode, TextType
from utils import *

class TestTextToTextnodes(unittest.TestCase):
    def test_text_to_textnodes_simple(self):
        text = "Hello world"
        nodes = text_to_textnodes(text)
        assert len(nodes) == 1
        assert nodes[0].text == "Hello world"
        assert nodes[0].text_type == TextType.TEXT

    def test_text_to_textnodes_bold(self):
        text = "This is **bold** text"
        nodes = text_to_textnodes(text)
        assert len(nodes) == 3
        assert nodes[0].text == "This is "
        assert nodes[0].text_type == TextType.TEXT
        assert nodes[1].text == "bold"
        assert nodes[1].text_type == TextType.BOLD
        assert nodes[2].text == " text"
        assert nodes[2].text_type == TextType.TEXT

    def test_text_to_textnodes_italic(self):
        text = "This is *italic* text"
        nodes = text_to_textnodes(text)
        assert len(nodes) == 3
        assert nodes[0].text == "This is "
        assert nodes[0].text_type == TextType.TEXT
        assert nodes[1].text == "italic"
        assert nodes[1].text_type == TextType.ITALIC
        assert nodes[2].text == " text"
        assert nodes[2].text_type == TextType.TEXT

    def test_text_to_textnodes_code(self):
        text = "This is `code` text"
        nodes = text_to_textnodes(text)
        assert len(nodes) == 3
        assert nodes[0].text == "This is "
        assert nodes[0].text_type == TextType.TEXT
        assert nodes[1].text == "code"
        assert nodes[1].text_type == TextType.CODE
        assert nodes[2].text == " text"
        assert nodes[2].text_type == TextType.TEXT
    
    def test_text_to_textnodes_link(self):
        text = "Visit [Google](https://www.google.com)"
        nodes = text_to_textnodes(text)
        # print(f"Nodes: {len(nodes)}")
        # for i, node in enumerate(nodes):
        #     print(f"Node {i}: text='{node.text}', type={node.text_type}")
        assert len(nodes) == 2
        assert nodes[0].text == "Visit "
        assert nodes[0].text_type == TextType.TEXT
        assert nodes[1].text == "Google"
        assert nodes[1].text_type == TextType.LINK
        assert nodes[1].url == "https://www.google.com"

    def test_text_to_textnodes_image(self):
        text = "Image:![Image](https://example.com/image.jpg)"
        nodes = text_to_textnodes(text)
        # print(f"Nodes: {len(nodes)}")
        # for i, node in enumerate(nodes):
        #     print(f"Node {i}: text='{node.text}', type={node.text_type}")
        assert len(nodes) == 2
        assert nodes[0].text == "Image:"
        assert nodes[0].text_type == TextType.TEXT
        assert nodes[1].text == "Image"
        assert nodes[1].text_type == TextType.IMAGE
        assert nodes[1].url == "https://example.com/image.jpg"

    def test_text_to_textnodes_bold_italic_code_link_image(self):
        text = "This is **bold**, *italic*, `code`, [link](https://www.example.com), and an image:![Image](https://example.com/image.jpg)"
        nodes = text_to_textnodes(text)
        print(f"Nodes: {len(nodes)}")
        for i, node in enumerate(nodes):
            print(f"Node {i}: text='{node.text}', type={node.text_type}")
        assert len(nodes) == 10
        assert nodes[0].text == "This is "
        assert nodes[0].text_type == TextType.TEXT
        assert nodes[1].text == "bold"
        assert nodes[1].text_type == TextType.BOLD
        assert nodes[2].text == ", "
        assert nodes[2].text_type == TextType.TEXT
        assert nodes[3].text == "italic"
        assert nodes[3].text_type == TextType.ITALIC
        assert nodes[4].text == ", "
        assert nodes[4].text_type == TextType.TEXT
        assert nodes[5].text == "code"
        assert nodes[5].text_type == TextType.CODE
        assert nodes[6].text == ", "
        assert nodes[6].text_type == TextType.TEXT
        assert nodes[7].text == "link"
        assert nodes[7].text_type == TextType.LINK
        assert nodes[7].url == "https://www.example.com"
        assert nodes[8].text == ", and an image:"
        assert nodes[8].text_type == TextType.TEXT
        assert nodes[9].text == "Image"
        assert nodes[9].text_type == TextType.IMAGE
        assert nodes[9].url == "https://example.com/image.jpg"



if __name__ == "__main__":
    unittest.main()