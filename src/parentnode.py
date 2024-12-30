from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("Parent nodes must have a tag.")
        if children is None:
            raise ValueError("Parent nodes must have children.")
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        props_str = self.props_to_html()
        child_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{props_str}>{child_html}</{self.tag}>"

    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"