N=int(input())
print("|")
for i in range(1,N):
    hallow=" "*i
    print("|"+hallow+"\\") #backslash
for j in range(1,N):
    hollow=" "*(N-j-1)
    print("| "+hollow+"/")
print("|")

"""
input:4
output:
|
| \
|  \
|   \
|   /
|  /
| /
|

"""
