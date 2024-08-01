from htmlnode import HTMLNode
from functools import reduce

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if(self.tag == None):
            raise ValueError("Parent Node has no tag")
        
        if(len(self.children) == 0):
            raise ValueError("Parent Node contains no children")
        
        return f"<{self.tag}{self.props_to_html()}>" + reduce(lambda acc, x: acc + x.to_html(), self.children, "") + f"</{self.tag}>"