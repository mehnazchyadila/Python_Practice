# Search And Replace
"""
sub(pattern,replace,string)

"""

import re

pattern = r"Colour"

text1 = "Red is a colour I love Red colour "
text2 = re.sub(pattern,"Color", text1)

print(text2)


text1 = "Red is a colour I love Red colour "
text2 = re.sub(pattern,"Color", text1,count=1)

print(text2)
