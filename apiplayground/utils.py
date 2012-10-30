import re

def tokenize_url_parameters(url):
    """
    A function that tokenize parameters from the provided url.

    >>> tokenize_url_parameters("/test/{object_id}")
    [('{object_id}', 'object_id')]

    >>> tokenize_url_parameters("/tests/")
    []
    """
    pattern = re.compile("(\{([a-z-_]+)\})")
    return pattern.findall(url) or []