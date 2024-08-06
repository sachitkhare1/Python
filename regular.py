import re

txt = "collection is the root interface of java collection framework"

x = re.findall("framework$")

if x :
    print("yes, its Ends with framework")