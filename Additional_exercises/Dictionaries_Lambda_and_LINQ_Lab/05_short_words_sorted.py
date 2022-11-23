import re

text = input().lower()

pattern = r'\b([a-z0-9\-\#\@\$\%\&\*\_]{1,4})[\.\,\:\;\(\)\[\]\"\'\/\!\?\s\\]'
matches = re.findall(pattern, text)

sorted_matches = sorted(set(matches))
print(', '.join(sorted_matches))

# TODO
