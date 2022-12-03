import re


def add_email(username, domain):
    """
    This function adds new domain in valid_emails dict if it does not exist. If domain exists in dict, func checks
    if username exists in current domain ignor it.
    :param username: str
    :param domain: str
    """
    global valid_emails

    if domain not in valid_emails:
        valid_emails[domain] = []
        valid_emails[domain].append(username)
    else:
        if username not in valid_emails[domain]:
            valid_emails[domain].append(username)


def email_validation(current_email):
    """
    This function receives string from console input and validates if it is pass following conditions:
    - username should be at least 5 characters long and consist only of uppercase and lowercase Latin letters.
    - username should be followed immediately by ‘@’.
    - The domain part should consist of two parts: mail server, which should contain only lowercase Latin letters
    and should be at least 3 letters long; top-level domain, which can be one of the following: .com, .bg or .org
    If current_email pass all conditions function calls add_email funcion.
    :param current_email: str
    """
    pattern = r'^(?P<username>[A-Za-z]{5,})@(?P<domain>[a-z]{3,}(\.org|\.bg|\.com))$'
    match = re.search(pattern, current_email)

    if match:
        username = match['username']
        domain = match['domain']
        add_email(username, domain)


def output():
    """
    This function order the domains by the counts of usernames in the domain in descending order.
    If they are equal, print them in the order, in which they were received.
    At the end print sorted dict.
    """
    global valid_emails
    for domain, usernames in sorted(valid_emails.items(), key=lambda kvp: -len(kvp[1])):
        print(f'{domain}:')
        for username in usernames:
            print(f'### {username}')


number_of_emails = int(input())

# create dict to store valid emails with following structure (key -> domain, value -> username)
valid_emails = {}

for _ in range(number_of_emails):
    email = input()
    email_validation(email)

output()
