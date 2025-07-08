# regular expression
# regex
# strings
# import re
# validate the input

#1: match(pattern, string, flags)

import re
pattern="apple"
if re.match(pattern,"appleandapple"):
    print("TRUE")
else:
    print("FALSE")

#2: findall (pattern,string, flags)

import re
pattern="AmanPatel"
string=re.findall("Aman",pattern)
print(string)