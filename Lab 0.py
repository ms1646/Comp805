#Create a list
t = [1, 2, 3, 4, 5]
#Find the length of the list with builtin library function call len()
len(t)
#Find the sum of the numbers in the list with builtin library function call sum()
sum(t)
#What's the type of the return value of the sum() call? How does Python know?
type(sum(t))
#What's the type of list builtin data structure?
type(list)
#What modules are imported by default in the Python session?
dir()
#What's in __builtins__ module?
dir(__builtins__)
#What's the signature (API) of th sum() function and its description (docstring)?
help(sum)
#What's the signature (API) and description(docstring) of list?
 help(list)
#Meathod def
 def find_common_characters(msg1,msg2):
    strng=""
    flag=0
    length1=len(msg1)
    length2=len(msg2)
    for i in range (0,length1):
        for j in range (0,length2):
            if(msg1[i]!=" "):
                if(msg1[i]==msg2[j]):
                    if(strng.count(msg1[i])==0):
                        strng=strng+msg1[i]
                        flag=flag+1
    if(flag!=0):
        return strng
    else:
        return -1

msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
