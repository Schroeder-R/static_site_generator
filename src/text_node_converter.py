from textnode import TextNode, TextType
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    if text_node is None:
        raise ValueError("Text node cannot be None.")

    match text_node.text_type:
        case TextType.TEXT:
                return LeafNode(text_node.text)
        case TextType.BOLD:
                return LeafNode(text_node.text, "b")
        case TextType.ITALIC:
                return LeafNode(text_node.text, "i")
        case TextType.CODE:
                return LeafNode(text_node.text, "code")
        case TextType.LINK:
                return LeafNode(text_node.text, "a", {"href": text_node.url})
        case TextType.IMAGE:
                return LeafNode("", "img", {"src": text_node.url, "alt": text_node.text})
        case _:
                raise ValueError(f"Unsupported text type: {text_node.text_type}")