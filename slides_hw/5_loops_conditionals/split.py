import re

text = "Hello, world!   This... is a test."
words = re.split(r"[\s\W]+", text)
words = [w for w in words if w]   # remove empty strings
print(words)

