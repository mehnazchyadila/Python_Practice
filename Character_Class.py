 # Character Class

import re

p = r"[aeiou]"
if re.match(p,"a"):
    print("Match")

else:
    print("Not Matched")

p = r"[A-Z][a-z][0-9]"
if re.match(p,"My name is Adila "):
    print("Match")

else:
    print("Not Matched")

p = r"[A-Z][a-z][0-9]"
if re.match(p,"Aa0"):
    print("Match")

else:
    print("Not Matched")