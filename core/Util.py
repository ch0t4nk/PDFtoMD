def remove_markdown_warp(text, language="markdown"):
    """
    Remove the warp of ```language and ```
    """
    text = text.strip()
    if text.startswith("```" + language):
        text = text[len("```" + language) :]
    if text.endswith("```"):
        text = text[: -len("```")]
    return text.strip()
