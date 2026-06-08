import sys
args = sys.argv
if len(args) > 1:
    file = args[1]
else:
    file = input("Path to file: ")


with open(file) as f:
    content = f.read()

content_parsed = content.replace("\\n\n","\n")
content_final = content_parsed.replace("\n","\\n\n")

with open(file, 'w') as g:
    g.write(content_final)

