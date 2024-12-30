from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        if value is None:
            raise ValueError("Leaf nodes must have a value.")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag is None:
            return str(self.value)
        props_str = self.props_to_html()
        if props_str:
            return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"

        