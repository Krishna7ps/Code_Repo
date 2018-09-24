import re

text_to_search='''Interestingly, the previous example shows already a "favourite" example for a mistake, frequently made not only by beginners and novices but also by advanced users of regular expressions. 

The idea of this example is to match strings containing the word "cat". We are successful with this, but unfortunately we are matching a lot of other words as well. 

If we match "cats" in a string that might be still okay, but what about all those words containing this character sequence "cat"? We match words like "education", "communicate", "falsification", "ramifications", "cattle" and many more. 

This is a case of "over matching", i.e. we receive positive results, which are wrong according to the problem we want to solve.

ha1 ha2 haha3

abcdefgh
ABCDEFGH
12345678
^*$.?/|[]{}()
Laura Jefferson
516-555-4615
890 Main St., Pythonville LA 29947
laurajefferson@bogusemail.com

Maria Johnson
127-555-1867
884 High St., Braavos‎ ME 43597
mariajohnson@bogusemail.com

Michael Arnold
608-555-4938
249 Elm St., Quahog OR 90938
michaelarnold@bogusemail.com

Michael Smith
568-555-6051
619 Park St., Winterfell VA 99000
michaelsmith@bogusemail.com

Erik Stuart
292-555-1875
220 Cedar St., Lakeview NY 87282
robertstuart@bogusemail.com

Laura Martin
900-555--3205
391 High St., Smalltown WY 28362
lauramartin@bogusemail.com

end
'''
sentence='Start the text with something similar'

pattern=re.compile(r"[ha]{2}")
# matches=pattern.finditer(text_to_search)

matches=pattern.finditer(text_to_search)

for i in matches:
    print(i)