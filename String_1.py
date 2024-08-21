name = "Alice"
age = 25
message = f"My name is {name} and I am {age} years old."
print(message)  # Output: "My name is Alice and I am 25 years old."

# Including expressions
result = f"5 + 5 = {5 + 5}"
print(result)  # Output: "5 + 5 = 10"

# ------------------Formatted String Literals -----------------------
template = "Hello, {}. You have {} unread messages."
formatted_string = template.format("Bob", 5)
print(formatted_string)  # Output: "Hello, Bob. You have 5 unread messages."

template = "Name: {name}, Age: {age}"
formatted_string = template.format(name="Charlie", age=30)
print(formatted_string)  # Output: "Name: Charlie, Age: 30"

# ------------------------------------------

name = "Diana"
age = 28
message = "My name is %s and I am %d years old." % (name, age)
print(message)  # Output: "My name is Diana and I am 28 years old."

# -------------------------
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)  # Output: "Python is awesome"

# -----------------Padding and Alignment------------------------

text = "Align"
formatted_str = f"{text:<10}"   # Left-align within 10 spaces
print(formatted_str)
formatted_str = f"{text:>10}"   # Right-align within 10 spaces
print(formatted_str)
formatted_str = f"{text:^10}"   # Center-align within 10 spaces
print(formatted_str)


