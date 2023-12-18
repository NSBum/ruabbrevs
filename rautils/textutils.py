import re


def extract_number(input_string):
    """
    Extracts numbers from a string that starts with a vertical bar '|' followed by numerals.

    Args:
    input_string (str): The input string to process.

    Returns:
    str: The extracted number as a string, or an empty string if the format is incorrect.
    """
    match = re.search(r'\|(\d+)', input_string)
    return match.group(1) if match else ''


def extract_template_name(input_string):
    match = re.search(r'\|([^\}]+)', input_string)
    return match.group(1) if match else ''


def extract_wikilink_alias(input_string):
    match = re.search(r'\|([^\]]+)', input_string)
    return match.group(1) if match else ''


def extract_wikilinks(text):
    """
    Extracts and substitutes wikilinks in a given text.
    Wikilinks are in the format [[link|alias]] or [[link]].
    The function replaces them with 'alias' if it exists, otherwise with 'link'.

    Args:
    text (str): The input text containing wikilinks.

    Returns:
    str: The text with wikilinks substituted.
    """
    def replace_wikilink(match):
        # Split the match into link and alias, if the alias exists
        parts = match.group(1).split('|')
        # Return the alias if it exists, otherwise return the link
        return parts[-1]

    # Use regex to find all wikilinks and substitute them using the replace_wikilink function
    return re.sub(r'\[\[([^\]]+)\]\]', replace_wikilink, text)
