from notebook import Note, Notebook

n1=Notebook()
n2=Notebook()

n1.new_note('first memo','f1')
n1.new_note("ending memo",'f2')

print(n1.list_notes())
n1.modify(2,"this is the test memo")
print(n1.list_notes())
print(n1.lastid_info())
print(n1.temp_value) 
print(  )