import re
txt = "the rain in spain falls mainly in the plain"
x = re.findall("falls|the|plain",txt)


if x:
    print("=======match found=====")
    print(x)
else:
    print("not found")
