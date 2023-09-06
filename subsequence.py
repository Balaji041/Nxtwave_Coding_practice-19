string=input()
sub_string=input()
index=0
l=len(sub_string)
for char in string:
    if char==sub_string[index]: #subsquemces
        index+=1
        if index==l:
            break
    
if index==l:
    print("Yes")
else:
    print("No")
"""
input:
abcde
ace
output:yes
"""
