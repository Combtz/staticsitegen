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
        