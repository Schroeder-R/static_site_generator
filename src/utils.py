from textnode import TextNode, TextType
from leafnode import LeafNode
import re

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

def split_nodes_image(old_nodes):
        new_nodes = []
        for old_node in old_nodes:
                if old_node.text_type != TextType.TEXT:
                        new_nodes.append(old_node)
                        continue
                original_text = old_node.text
                images = extract_markdown_images(original_text)
                if len(images) == 0:
                        new_nodes.append(old_node)
                        continue
                for image in images:
                        sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
                        if len(sections) != 2:
                                raise ValueError(f"Invalid markdown, image section not closed")
                        if sections[0] != "":
                                new_nodes.append(TextNode(sections[0], TextType.TEXT))
                        new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
                        original_text = sections[1]
                if original_text != "":
                        new_nodes.append(TextNode(original_text, TextType.TEXT))
        return new_nodes

def split_nodes_link(old_nodes):
        new_nodes = []
        for old_node in old_nodes:
                if old_node.text_type!= TextType.TEXT:
                        new_nodes.append(old_node)
                        continue
                original_text = old_node.text
                links = extract_markdown_links(original_text)
                if len(links) == 0:
                        new_nodes.append(old_node)
                        continue
                for link in links:
                        sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
                        if len(sections)!= 2:
                                raise ValueError(f"Invalid markdown, link section not closed")
                        if sections[0]!= "":
                                new_nodes.append(TextNode(sections[0], TextType.TEXT))
                        new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
                        original_text = sections[1]
                if original_text!= "":
                        new_nodes.append(TextNode(original_text, TextType.TEXT))
        return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches