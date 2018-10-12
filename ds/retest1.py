import re

search_string="1."
pattern="\d+.\d?"

if re.match(pattern,search_string):
    print("It's matched")
else:
    print("Not matched")