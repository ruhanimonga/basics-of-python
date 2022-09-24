import re
txt = "My students are less"
x=re.search("^the My",txt)
if x:
    print("match")
else:
    print("not matched")
