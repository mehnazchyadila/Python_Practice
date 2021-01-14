 # Regular expressions

""" What is regular expression ?
 Regular expression are tools for manipulating string
 
 Why do you need regular expression ?
 - Verifying that strings match a pattern 
 - Performing substitutions in a string 
 Regular expression can be accessed using the re module  
  - match() : matches at the beginning of a string  
  - search() : finds a match of a pattern anywhere in the pattern 
  - findall() : returns a string of a substrings that match a pattern 
  
 """
import re
p = r"color"
if re.match(p,"Red is a color I love Red color"):
    print("Match")

else:
    print("Not Matched")

p = r"color"
if re.search(p,"Red is a color I love Red color"):
    print("Match")

else:
    print("Not Matched")

p = r"col"
if re.search(p,"Red is a color I love Red color"):
    print("Match")

else:
    print("Not Matched")

print(re.findall(p,"Red is a color I love Red color"))