import re

text = "Hello, world!   This... is a test."
words = re.split(r"[\s\W]+", text)
print(words)
# ['Hello', 'world', 'This', 'is', 'a', 'test', '']
