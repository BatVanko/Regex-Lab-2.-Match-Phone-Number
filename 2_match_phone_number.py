import re

text = input()

matches = re.findall(r"\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}", text)
print(" ".join(matches))
