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

def split_nodes_delimiter(old_nodes, delimiter, text_type):
        new_nodes = []
        for node in old_nodes:
                if node.text_type != TextType.TEXT:
                        new_nodes.append(node)
                else:
                        delimiter_count = node.text.count(delimiter)
                        if delimiter_count % 2 != 0:
                                raise ValueError(f"Delimiter '{delimiter}' not balanced in text node: {node}")
                        split_text = node.text.split(delimiter)
                        for i, text in enumerate(split_text):
                                if i % 2 == 0:
                                        new_nodes.append(TextNode(text, TextType.TEXT))
                                else:
                                        new_nodes.append(TextNode(text, text_type))
        return new_nodes