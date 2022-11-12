title = input()
content = input()

comments = []

while True:
    comment = input()
    if comment == 'end of comments':
        break
    comments.append(comment)

print('<h1>')
print('\t' + title)
print('</h1>')
print('<article>')
print('\t' + content)
print('</article>')
for comment in comments:
    print('<div>')
    print('\t' + comment)
    print('</div>')
