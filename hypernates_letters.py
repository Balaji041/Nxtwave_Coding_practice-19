W=input()
ans=""
for char in W:
    ans+=char+"-"
print(ans[:len(ans)-1])
"""
input:hello
output:H-e-l-l-o
"""
