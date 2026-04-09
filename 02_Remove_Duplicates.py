#You are given a string, remove all the duplicates and print the unique string.Use loop in the python.

word=input()
result=""
for i in word:
    if i in result:
        continue
    else:
        result+=i
print(result)
