import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(None, None, None, {"href" : "https://www.google.com", "target" : "_blank"})

        self.assertEqual(node.props_to_html(), "href=\"https://www.google.com\" target=\"_blank\"")

        node2 = HTMLNode(None, None, None, None)

        self.assertEqual(node2.props_to_html(), "")

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )
        
    def test_repr(self):
        node = HTMLNode("p", "I am a test HTML Node", None, None)

        self.assertEqual(repr(node), "HTML NODE: tag: p, value: I am a test HTML Node, children: None, props: None")