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


#2: search (pattern,string, flags)
import re
pattern="apple"
if re.search(pattern,"andapple"):
    print("TRUE")
else:
    print("FALSE")
#3: sub (pattern,repl,string,count,flags)
import re
string = "I am Aman Patel"
pattern="Aman"
print(re.sub(pattern,"Ananya",string,count=0,flags=0))