"""
Utility Functions - Helper functions for markdown processing

Original MarkPDFDown Project
Copyright (c) MarkPDFDown Team
Licensed under the Apache License, Version 2.0
Original project: https://github.com/MarkPDFdown/markpdfdown

Enhanced by Joseph Wright (github: ch0t4nk) for enterprise use
Copyright (c) 2025 Joseph Wright (github: ch0t4nk)
Licensed under the Apache License, Version 2.0
"""


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
