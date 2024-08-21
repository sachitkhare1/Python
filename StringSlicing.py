s = "abcdefgh"
slice_str = s[::2]  # Every second character: "aceg"
reverse_str = s[::-1]  # Reverse the string: "hgfedcba"

# --------Slicing with Negative Indices------------------------
s = "abcdefgh"
last_two_chars = s[-2:]  # "gh"

# ---------Removes whitespace or specified characters-------
s = "  Hello  "
stripped = s.strip()  # "Hello"

# ---replace------
s = "Hello World"
new_s = s.replace("World", "Python")  # "Hello Python"

s = "Hello World"
index = s.find("o")  # 4
rindex = s.rfind("o")  # 7

# ---- String Encoding and Decoding-------------

s = "Hello World"
encoded_s = s.encode('utf-8')  # b'Hello World'

encoded_s = b'Hello World'
decoded_s = encoded_s.decode('utf-8')  # "Hello World"

name = "Alice"
greeting = "Hello"
formatted_str = "{greeting}, {name}!".format(**locals())
print(formatted_str)  # Output: "Hello, Alice!"
