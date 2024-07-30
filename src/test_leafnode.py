import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a test paragraph")

        self.assertEqual(node.to_html(), "<p>This is a test paragraph</p>")

    def test_value_error(self):
        node =  LeafNode("a")

        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
