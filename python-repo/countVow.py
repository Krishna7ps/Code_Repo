text=input("enter text for vowel counting: ")
print(text)
count=0
for c in text:
    if c in ['a','e','i','o','u']:
        count+=1

print("the number of vowels is ", count)
