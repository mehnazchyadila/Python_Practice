#  Meta Characters
"""
. dot (Any Character)
^$
*(0 or more)
+(1 or more)
? (0 or 1)
{and}
"""
import re

p = r"colo.r"
if re.match(p,"coloar"):
    print("Match")

else:
    print("Not Matched")

p = r"colo..r"
if re.match(p,"coloaar"):
    print("Match")

else:
    print("Not Matched")

p = r"^colo..r$"
if re.match(p, "coloaa"):
        print("Match")

else:
        print("Not Matched")

p = r"a*"
if re.match(p,"aaacoloaar"):
    print("Match")

else:
    print("Not Matched")

p = r"(ab)*"
if re.match(p,"coloaar"):
    print("Match")

else:
    print("Not Matched")

p = r"a*b"
if re.match(p,"coloaar"):
    print("Match")

else:
    print("Not Matched")

p = r"a*b"
if re.match(p,"abcoloaar"):
    print("Match")

else:
    print("Not Matched")

p = r"a+b"
if re.match(p,"coloaar"):
    print("Match")

else:
    print("Not Matched")

p = r"ice(-)?cream"
if re.match(p,"icecream"):
    print("Match")

else:
    print("Not Matched")

p = r"a{1,3}$"
if re.match(p,"aaa"):
    print("Match")

else:
    print("Not Matched")

p = r"a{1,3}$"
if re.match(p,"a"):
    print("Match")

else:
    print("Not Matched")


