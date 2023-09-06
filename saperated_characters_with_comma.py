Name=input()
string=""
for i in Name:
    string+=i+"," #compound assignment operator
print(string[:len(string)-1])

"""
input:wonder
output:w,o,n,d,e,r
"""
