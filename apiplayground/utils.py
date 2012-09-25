import re

def tokenize_url_parameters(url):
    pattern = re.compile("(\{([a-z-]+)\})")
    return pattern.findall(url) or ()