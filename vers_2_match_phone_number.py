import re

text = input()

matches = re.finditer(r"\+359([ -])2\1\d{3}\1\d{4}|\+359-2-\d{3}-\d{4}\b", text)

result = []
for match in matches:
    result.append(match)
    
print(", ".join(result))
