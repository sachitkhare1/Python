import re

# text = "The price is $100"
# match = re.search(r"\$\d+", text)
# if match:
#     print(match.group())  # Output: "$100"

# text = "Today is 2024-08-21"
# new_text = re.sub(r"\d{4}-\d{2}-\d{2}", "DATE", text)
# print(new_text)  # Output: "Today is DATE"

# text = "abc123def456"
# matches = re.findall(r"\d+", text)
# print(matches)  # Output: ['123', '456']

# text = "abc123def456"
# for match in re.finditer(r"\d+", text):
#     print(match.group())  # Output: "123", then "456"

# text = "one1two2three3"
# split_text = re.split(r"\d", text)
# print(split_text)  # Output: ['one', 'two', 'three', '']

text = "John Doe, 25 years old"
match = re.search(r"(\w+) (\w+), (\d+) years old", text)
if match:
    first_name = match.group(1)  # "John"
    last_name = match.group(2)   # "Doe"
    age = match.group(3)         # "25"
    print(f"Name: {first_name} {last_name}, Age: {age}")

