import re


def extract_title(current_html):
    """
    This function parse all between <title> and </title> and returns requested string
    :param current_html: str
    :return: str
    """
    pattern = r'(?P<title>(?<=\<title>).*(?=<\/title>))'
    current_title = re.search(pattern, current_html)
    return current_title.group('title')


def extract_body(current_html):
    """
    This function parse all between <body> and </body> returns string which can't still used for end result
    :param current_html: str
    :return: str
    """
    pattern = r'(?P<body>(<body>.*<\/body>))'
    current_content = re.search(pattern, current_html)
    return current_content.group('body')


def remove_tags(current_body):
    """
    This function received result from extract_body() removes all tags and '\n'.
    Returns requested contest.
    :param current_body: str
    :return: str
    """
    pattern = r'>([^><]*)<'
    current_body = re.findall(pattern, current_body)

    cleaned_body = []
    for word in current_body:
        if '\\n' in word:
            word = word.replace('\\n', '')
        cleaned_body.append(word)
    cleaned_body = ''.join(cleaned_body)

    return cleaned_body


html = input()

title = extract_title(html)
body = extract_body(html)
content = remove_tags(body)

print(f'Title: {title}')
print(f'Content: {content}')
