import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_empty_node(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_single_prop_node(self):
        node = HTMLNode("div", props={"class": "container"})
        self.assertEqual(node.props_to_html(), ' class="container"')
    
    def test_multiple_props_node(self):
        node = HTMLNode("div", props={"class": "container", "id": "main"})
        self.assertEqual(node.props_to_html(), ' class="container" id="main"')

    def test_children_nodes(self):
        child1 = HTMLNode("p", value="First child")
        child2 = HTMLNode("p", value="Second child")
        parent = HTMLNode("div", children=[child1, child2])
        self.assertEqual(len(parent.children), 2)
        self.assertEqual(parent.children[0].value, "First child")
        self.assertEqual(parent.children[1].value, "Second child")

    def test_children_nodes_and_props(self):
        child1 = HTMLNode("p", value="First child", props={"class": "paragraph", "id": "p1"})
        child2 = HTMLNode("p", value="Second child", props={"class": "paragraph", "id": "p2"})
        parent = HTMLNode("div", 
                        children=[child1, child2],
                        props={"class": "container", "id": "main"})
        
        # Test parent properties
        self.assertEqual(parent.props_to_html(), ' class="container" id="main"')
        
        # Test children properties and values
        self.assertEqual(len(parent.children), 2)
        self.assertEqual(parent.children[0].value, "First child")
        self.assertEqual(parent.children[0].props["class"], "paragraph")
        self.assertEqual(parent.children[0].props["id"], "p1")
        self.assertEqual(parent.children[1].value, "Second child")
        self.assertEqual(parent.children[1].props["class"], "paragraph")
        self.assertEqual(parent.children[1].props["id"], "p2")
        
    def test_none_parameters(self):
        node = HTMLNode(None, None, None, None)
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_repr_output(self):
        node = HTMLNode("div", "text", None, {"class": "container"})
        # Assert that __repr__ contains all the important information
        repr_str = repr(node)
        self.assertIn("div", repr_str)
        self.assertIn("text", repr_str)
        self.assertIn("container", repr_str)

    def test_value_only_node(self):
        node = HTMLNode(value="Just some text")
        self.assertIsNone(node.tag)
        self.assertEqual(node.value, "Just some text")

    def test_props_special_chars(self):
        node = HTMLNode("a", props={"href": "https://example.com?key=value&name=test"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com?key=value&name=test"')

    def test_empty_children_list(self):
        node = HTMLNode("div", children=[])
        self.assertEqual(len(node.children), 0)
    
    def test_different_props(self):
        node1 = HTMLNode("div", props={"class": "container"})
        node2 = HTMLNode("div", props={"class": "wrapper"})
        self.assertNotEqual(node1.props_to_html(), node2.props_to_html())

    def test_different_values(self):
        node1 = HTMLNode("p", value="First")
        node2 = HTMLNode("p", value="Second")
        self.assertNotEqual(node1.value, node2.value)

    def test_different_children_count(self):
        parent1 = HTMLNode("div", children=[HTMLNode("p", value="child")])
        parent2 = HTMLNode("div", children=[
            HTMLNode("p", value="child1"),
            HTMLNode("p", value="child2")
        ])
        self.assertNotEqual(len(parent1.children), len(parent2.children))

if __name__ == "__main__":
    unittest.main()