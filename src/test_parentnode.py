import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_parent_node(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    )
        
        node2 = ParentNode("div", [node])

        node3 = ParentNode("div", [node], {"test" : "test"})


        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
        self.assertEqual(node2.to_html(), "<div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div>")
        self.assertEqual(node3.to_html(), "<div test=\"test\"><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div>")



    def test_parent_node_value_error(self):
        node = ParentNode(None , [LeafNode("b", "Test")] )

        with self.assertRaises(ValueError):
            node.to_html()

        node2 = ParentNode("div", [])

        with self.assertRaises(ValueError):
            node2.to_html()