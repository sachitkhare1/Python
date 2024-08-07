import re

text ="sachit khare bittoo khare "

pattern = "khare"

print(re.search(pattern,text))

print (re.findall(pattern,text))

l = "s ksd kd dds dsdg dshfhdfjhkldk"

p = re.search(r'\w\w\w',l)

print (p)

# Starting the RegEx fuctions 

pattern1="amazing"

r = re.compile(pattern1)
text = "This Toturial is amazing"
m1=r
print ("match :", m1)

# match function 
# pattern2="amazing"

# match= re.match(pattern2,"This Toturial is amazing")

# print (match)

# # print (m1.start())

# # print (m1.span())

# print("hello",match.end())

e= "Learn Python through tutorials on javatpoint"    

match12 = re.match(r'.w* (.w?) (.w*?)',e , re.M|re.I)

if match12:
    print ("Match Correct.",match12.group())
    print ("Match Correct.",match12.group(1))
    print ("Match Correct.",match12.group(2))
else:
    print ("not match.")

match3 = re.search(r'.*t? (.*t?) (.*t?)',e)

if match3 :
    print ("search Object :", match3.group())
    print ("search Object group 1 :", match3.group(1))
    print ("search Object group 2 :", match3.group(2))

else:
    print ("not match !")

#  sub() function 

pa11 = "javatpoint"

repl = "Python Point"

new_text = re.sub(pa11, repl ,e)
# new_text = re.sub(pal1 , repl , e, Index) we can also give index number of specific work 

print (e)

print (new_text)

# re.subn(pattern, repl, string, count=0, flags=0 is same as sub () 

h= "hello world"
 
print ( re.fullmatch("hello",h))
print (re.fullmatch("hello world",h))
# if it match inside the fullmatch function then it does not return any value 
# or does not match it return none