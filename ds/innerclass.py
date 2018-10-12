def for_str(strn,formatter=None):
    class def_format:
        def format(self,strn):
            return str(strn).title()
    
    if not formatter:
        d=def_format()
    return d.format(strn)

s="hello, world"
print("Input:",s)
print("output:",for_str(s))