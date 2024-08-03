block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_type(block):
    lines = block.split("\n")
    # Headings
    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return block_type_heading
    # Code Block
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    # Quote Block
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    # Unordered List
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    # Unordered List
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    # Ordered List
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph
