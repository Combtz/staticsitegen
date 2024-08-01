from functools import reduce


class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props == None:
            return ""
        props_html = " ".join(map(lambda kv: f"{kv[0]}=\"{kv[1]}\"", self.props.items()))

        return " " + props_html


    def __repr__(self):
        return f"HTML NODE: tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        if self.props != None:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if(self.tag == None):
            raise ValueError("Parent Node has no tag")
        
        if(len(self.children) == 0):
            raise ValueError("Parent Node contains no children")
        
        return f"<{self.tag}{self.props_to_html()}>" + reduce(lambda acc, x: acc + x.to_html(), self.children, "") + f"</{self.tag}>"

        